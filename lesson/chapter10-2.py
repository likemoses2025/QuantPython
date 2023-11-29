import _pickle


# ! 수정주가 크롤링
# @ 수정주가가 필요한 이유?
# @ 삼성전자 2018년5월 1주를 50주로 나누는 액면분할 실시
# @ 265만원에서 5만3천원으로 변경
# @ 가격으로만 보면 -98% 손실로 보임
# @ 액면불할전 모든 주가를 50으로 나누어 연속성을 갖게함 => 수정주가

# ! 개별종목 주가 크롤링

# 패키지 불러오기
import pymysql
from sqlalchemy import create_engine
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta
import requests as rq
import time
from tqdm import tqdm
from io import BytesIO

# DB 연결
engine = create_engine("mysql+pymysql://root:!!akswhr23@127.0.0.1:3306/stock_db")
con = pymysql.connect(
    user="root", passwd="!!akswhr23", host="127.0.0.1", db="stock_db", charset="utf8"
)
mycursor = con.cursor()

# 티커리스트 불러오기
ticker_list = pd.read_sql(
    """
select * from kor_ticker
where 기준일 = (select max(기준일) from kor_ticker) 
	and 종목구분 = '보통주';
""",
    con=engine,
)

print("TICKER_LIST", ticker_list)
#     종목코드        종목명   시장구분        종가          시가총액         기준일     EPS   선행EPS       BPS   주당배당금 종목구분
# 0     000020       동화약품  KOSPI    9690.0  2.706560e+11  2023-11-24   736.0     NaN   13165.0   180.0  보통주
# 1     000040      KR모터스  KOSPI     526.0  5.056880e+10  2023-11-24     NaN     NaN     345.0     0.0  보통주
# 2     000050         경방  KOSPI    8520.0  2.335780e+11  2023-11-24   177.0     NaN   30304.0   125.0  보통주
# 3     000070      삼양홀딩스  KOSPI   68700.0  5.883650e+11  2023-11-24  9173.0     NaN  240995.0  3500.0  보통주
# 4     000080      하이트진로  KOSPI   22850.0  1.602550e+12  2023-11-24  1250.0  1230.0   16906.0   950.0  보통주
# ...      ...        ...    ...       ...           ...         ...     ...     ...       ...     ...  ...
# 2396  457190  이수스페셜티케미컬  KOSPI  146800.0  8.219000e+11  2023-11-24     NaN     NaN       NaN     0.0  보통주
# 2397  460850       동국씨엠  KOSPI    7260.0  2.170640e+11  2023-11-24     NaN  1483.0       NaN     0.0  보통주
# 2398  460860       동국제강  KOSPI   11340.0  5.625550e+11  2023-11-24     NaN  7958.0       NaN     0.0  보통주
# 2399  462520       조선내화  KOSPI   24850.0  2.946010e+11  2023-11-24     NaN     NaN       NaN     0.0  보통주
# 2400  465770   STX그린로지스  KOSPI   11710.0  8.397280e+10  2023-11-24     NaN     NaN       NaN     0.0  보통주

# DB 저장 쿼리
query = """
    insert into kor_price (날짜, 시가, 고가, 저가, 종가, 거래량, 종목코드)
    values (%s,%s,%s,%s,%s,%s,%s) as new
    on duplicate key update
    시가 = new.시가, 고가 = new.고가, 저가 = new.저가,
    종가 = new.종가, 거래량 = new.거래량;
"""

# 오류 발생시 저장할 리스트 생성
error_list = []

# 전종목 주가 다운로드 및 저장
for i in tqdm(range(0, len(ticker_list))):
    # 티커 선택
    ticker = ticker_list["종목코드"][i]

    # 시작일과 종료일
    fr = (date.today() + relativedelta(years=-5)).strftime("%Y%m%d")
    to = (date.today()).strftime("%Y%m%d")

    # 오류 발생 시 이를 무시하고 다음 루프로 진행
    try:
        # url 생성
        url = f"""https://fchart.stock.naver.com/siseJson.nhn?symbol={ticker}&requestType=1
        &startTime={fr}&endTime={to}&timeframe=day"""

        # 데이터 다운로드
        data = rq.get(url).content
        data_price = pd.read_csv(BytesIO(data))

        # 데이터 클렌징
        price = data_price.iloc[:, 0:6]
        price.columns = ["날짜", "시가", "고가", "저가", "종가", "거래량"]
        price = price.dropna()
        price["날짜"] = price["날짜"].str.extract("(\d+)")
        price["날짜"] = pd.to_datetime(price["날짜"])
        price["종목코드"] = ticker

        # 주가 데이터를 DB에 저장
        args = price.values.tolist()
        mycursor.executemany(query, args)
        con.commit()

    except:
        # 오류 발생시 error_list에 티커 저장하고 넘어가기
        print(ticker)
        error_list.append(ticker)

    # 타임슬립 적용
    time.sleep(2)

# DB 연결 종료

con.close()
