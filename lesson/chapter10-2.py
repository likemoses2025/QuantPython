from dateutil.relativedelta import relativedelta
import requests as rq
from io import BytesIO
from datetime import date
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("mysql+pymysql://root:!!akswhr23@127.0.0.1:3306/stock_db")
query = """
select * from kor_ticker
where 기준일 = (select max(기준일) from kor_ticker) 
	and 종목구분 = '보통주';
"""
ticker_list = pd.read_sql(query, con=engine)
engine.dispose()

ticker_list.head()

i = 0
ticker = ticker_list["종목코드"][i]
fr = (date.today() + relativedelta(years=-5)).strftime("%Y%m%d")
to = (date.today()).strftime("%Y%m%d")

url = f"""https://fchart.stock.naver.com/siseJson.nhn?symbol={ticker}&requestType=1
&startTime={fr}&endTime={to}&timeframe=day"""

data = rq.get(url).content
print(data)
data_price = pd.read_csv(BytesIO(data))

print(data_price.head())
#   [['날짜'    '시가'    '고가'    '저가'    '종가'     '거래량'  '외국인소진율']  Unnamed: 7
# 0  ["20181127"  9450.0  9510.0  9410.0  9430.0   21198.0       8.5]         NaN
# 1  ["20181128"  9480.0  9490.0  9150.0  9320.0  138261.0       8.5]         NaN
# 2  ["20181129"  9410.0  9410.0  9260.0  9360.0   47101.0      8.47]         NaN
# 3  ["20181130"  9370.0  9380.0  9100.0  9110.0  123667.0       8.5]         NaN
# 4  ["20181203"  9230.0  9430.0  9230.0  9370.0   68336.0      8.53]         NaN


import re

# @ 모든 행을 선택하고 열은 6개만 선택
price = data_price.iloc[:, 0:6]
# ? print(price)
#            [['날짜'    '시가'    '고가'    '저가'    '종가'     '거래량'
# 0     ["20181127"  9450.0  9510.0  9410.0  9430.0   21198.0
# 1     ["20181128"  9480.0  9490.0  9150.0  9320.0  138261.0
# 2     ["20181129"  9410.0  9410.0  9260.0  9360.0   47101.0
# 3     ["20181130"  9370.0  9380.0  9100.0  9110.0  123667.0
# 4     ["20181203"  9230.0  9430.0  9230.0  9370.0   68336.0
# ...           ...     ...     ...     ...     ...       ...
# 1230  ["20231122"  9670.0  9690.0  9600.0  9650.0   47903.0
# 1231  ["20231123"  9650.0  9800.0  9630.0  9730.0   60233.0
# 1232  ["20231124"  9800.0  9810.0  9690.0  9690.0   29893.0
# 1233  ["20231127"  9690.0  9720.0  9590.0  9630.0   32587.0
# 1234            ]     NaN     NaN     NaN     NaN       NaN

price.columns = ["날짜", "시가", "고가", "저가", "종가", "거래량"]
# ? NA 데이터 제거
price = price.dropna()
# ? 날짜열에서 숫자만 추출
price["날짜"] = price["날짜"].str.extract("(\d+)")
price["날짜"] = pd.to_datetime(price["날짜"])
price["종목코드"] = ticker

# ? print(price.head())
#           날짜      시가      고가      저가      종가       거래량    종목코드
# 0 2018-11-27  9450.0  9510.0  9410.0  9430.0   21198.0  000020
# 1 2018-11-28  9480.0  9490.0  9150.0  9320.0  138261.0  000020
# 2 2018-11-29  9410.0  9410.0  9260.0  9360.0   47101.0  000020
# 3 2018-11-30  9370.0  9380.0  9100.0  9110.0  123667.0  000020
# 4 2018-12-03  9230.0  9430.0  9230.0  9370.0   68336.0  000020
