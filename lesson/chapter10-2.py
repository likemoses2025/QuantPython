import _pickle


# ! 수정주가 크롤링
# @ 수정주가가 필요한 이유?
# @ 삼성전자 2018년5월 1주를 50주로 나누는 액면분할 실시
# @ 265만원에서 5만3천원으로 변경
# @ 가격으로만 보면 -98% 손실로 보임
# @ 액면불할전 모든 주가를 50으로 나누어 연속성을 갖게함 => 수정주가

# ! 개별종목 주가 크롤링

import pandas as pd
from io import BytesIO
import requests as rq
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from dateutil.relativedelta import relativedelta
from datetime import date

engine = create_engine("mysql+pymysql://root:!!akswhr23@127.0.0.1:3306/stock_db")
query = """
    select * from kor_ticker
    where 기준일 = (select max(기준일) from kor_ticker)
    and 종목구분 = "보통주";
"""
ticker_list = pd.read_sql(query, con=engine)
# print(ticker_list.head())

i = 0
ticker = ticker_list["종목코드"][i]
print("TICKER", ticker)
fr = (date.today() + relativedelta(years=-5)).strftime("%Y%m%d")
to = (date.today()).strftime("%Y%m%d")
print("FR", fr)
print("TO", to)

url = f"""
    https://fchart.stock.naver.com/siseJson.nhn?symbol={ticker}&requestType=1&startTime={fr}&endTime={to}&timeframe=day
"""
data = rq.get(url).content


data_price = pd.read_csv(BytesIO(data), sep="\t", encoding_errors="ignore")
print(data_price)
