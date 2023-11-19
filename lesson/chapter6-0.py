import pymysql

#! connect
con = pymysql.connect(
    user="root", passwd="!!akswhr23", host="127.0.0.1", db="shop", charset="utf8"
)
# ? cursor는 현재 작업중인 객체를 나타내는 객체이다.
mycursor = con.cursor()


query = """
select * from goods;
"""

mycursor.execute(query)  # 쿼리를 데이터베이스에 보냄
data = mycursor.fetchall()  # fetchone() 한 행씩 추출, fetchmany(size=n) n개의 행을 추출
con.close()  # 서버 종료

print(data)
# (
#     ("0001", "티셔츠", "의류", 1000, 500, datetime.date(2020, 9, 20)),
#     ("0002", "펀칭기", "사무용품", 500, 320, datetime.date(2020, 9, 11)),
#     ("0003", "와이셔츠", "의류", 4000, 2000, None),
#     ("0004", "식칼", "주방용품", 3000, 2000, datetime.date(2020, 9, 20)),
#     ("0005", "압력솥", "주방용품", 6800, 5000, datetime.date(2020, 1, 15)),
#     ("0006", "포크", "주방용품", 500, None, datetime.date(2020, 9, 20)),
#     ("0007", "도마", "주방용품", 880, 790, datetime.date(2020, 4, 28)),
#     ("0008", "볼펜", "주방용품", 100, None, datetime.date(2020, 11, 11)),
# )

#! 데이터 입력, 수정 , 삭제
con = pymysql.connect(
    user="root", passwd="!!akswhr23", host="127.0.0.1", db="shop", charset="utf8"
)
# ? cursor는 현재 작업중인 객체를 나타내는 객체이다.
mycursor = con.cursor()
query = """
insert into goods (
    goods_id, goods_name, goods_classify, sell_price, buy_price, register_date
) values(
    '0009','스테이플러', '사무용품', '2000','1500', '2020-12-30' 
)
"""

# mycursor.execute(query)
# con.commit()  # ? 데이터 확정 및 갱신
# con.close()


#! pandas를 이용한 데이터 일기 및 쓰기
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:!!akswhr23@127.0.0.1:3306/shop")
query = """select * from goods"""


goods = pd.read_sql(query, con=engine)

engine.dispose()  # type: ignore
print(goods.head())
