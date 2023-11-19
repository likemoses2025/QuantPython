import pandas as pd
from sqlalchemy import create_engine
import pymysql

# try:
#     engine = create_engine("mysql+pymysql://root:!!akswhr23@127.0.0.1:3306/shop")
#     query = """select * from goods"""
#     goods = pd.read_sql(query, con=engine)

# finally:
#     engine.dispose()


engine = create_engine("mysql+pymysql://root:!!akswhr23@127.0.0.1:3306/shop")
query = """select * from goods"""
goods = pd.read_sql(query, con=engine)
engine.dispose()  # type: ignore
print(goods.head())
#   goods_id goods_name goods_classify  sell_price  buy_price register_date
# 0     0001        티셔츠             의류        1000      500.0    2020-09-20
# 1     0002        펀칭기           사무용품         500      320.0    2020-09-11
# 2     0003       와이셔츠             의류        4000     2000.0          None
# 3     0004         식칼           주방용품        3000     2000.0    2020-09-20
# 4     0005        압력솥           주방용품        6800     5000.0    2020-01-15

import seaborn as sns


#! 데이터프레임을 sql에 저장하기
iris = sns.load_dataset("iris")
print(iris.head())
#    sepal_length  sepal_width  petal_length  petal_width species
# 0           5.1          3.5           1.4          0.2  setosa
# 1           4.9          3.0           1.4          0.2  setosa
# 2           4.7          3.2           1.3          0.2  setosa
# 3           4.6          3.1           1.5          0.2  setosa
# 4           5.0          3.6           1.4          0.2  setosa

from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:!!akswhr23@127.0.0.1:3306/shop")
iris.to_sql(name="iris", con=engine, index=False, if_exists="replace")


#! upsert - mysql에서 insert update를 upsert라고 한다
# ? 퀀트투자에  사용할 시계열 데이터는 2가지의 특성이 있다
# ? 1. insert : 데이터 추가       2. update : 데이터 수정

from sqlalchemy_utils import create_database

# create_database("mysql+pymysql://root:!!akswhr23@127.0.0.1:3306/exam")
price = pd.DataFrame(
    {
        "날짜": ["2021-01-02", "2021-01-03"],
        "티커": ["000001", "000001"],
        "종가": [1340, 1315],
        "거래량": [1000, 2000],
    }
)
print(price.head())
#            날짜      티커    종가   거래량
# 0  2021-01-02  000001  1340  1000
# 1  2021-01-03  000001  1315  2000

# @ 데이터프레임을 mysql에 저장하기
engine = create_engine("mysql+pymysql://root:!!akswhr23@127.0.0.1:3306/exam")
# * if_exists="append" --> 테이블이 존재하면 테이블에 데이터를 추가한다.
price.to_sql("price", con=engine, if_exists="append", index=False)
data_sql = pd.read_sql("price", con=engine)

# ? 하루가 지나서 1개의 하루의 데이터가 추가 되었다면
new = pd.DataFrame(
    {
        "날짜": ["2021-01-04"],
        "티커": ["000001"],
        "종가": [1320],
        "거래량": [1500],
    }
)
price = pd.concat([price, new])
print(price.head())
#            날짜      티커    종가   거래량
# 0  2021-01-02  000001  1340  1000
# 1  2021-01-03  000001  1315  2000
# 0  2021-01-04  000001  1320  1500
engine = create_engine("mysql+pymysql://root:!!akswhr23@127.0.0.1:3306/exam")
# * if_exists="append" --> 테이블이 존재하면 테이블에 데이터를 추가한다.
price.to_sql("price", con=engine, if_exists="append", index=False)
data_sql = pd.read_sql("price", con=engine)


# @ upsert (insert + update)
price = pd.DataFrame(
    {
        "날짜": ["2021-01-04", "2021-01-04"],
        "티커": ["000001", "000002"],
        "종가": [1320, 1315],
        "거래량": [2100, 1500],
    }
)

# ? 1. 데이터프레임을 리스트 형태로 변환
args = price.values.tolist()
print(args)
# [['2021-01-04', '000001', 1320, 2100], ['2021-01-04', '000002', 1315, 1500]]

# ? 데이터베이스에 접속
con = pymysql.connect(
    user="root", passwd="!!akswhr23", host="127.0.0.1", db="exam", charset="utf8"
)

query = """
    insert into price_2
    (날짜, 티커, 종가, 거래량)
    values(%s,%s,%s,%s) as new
    on duplicate key update
    종가 = new.종가, 거래량 = new.거래량;
"""
# ? cursor메소드를 통해 데이터베이스의 커서 객체를 가져옴
mycursor = con.cursor()
# ? sql 쿼리를 데이터베이스에 보냄
mycursor.executemany(query, args)
# ? 데이터베이스의 확정을 갱신
con.commit()


#! 예제로 사용된 데이터베이스 삭제하기
con = pymysql.connect(
    user="root", passwd="!!akswhr23", host="127.0.0.1", db="exam", charset="utf8"
)
query = """
    drop database exam;
"""
mycursor = con.cursor()
mycursor.execute(query)
con.commit()
