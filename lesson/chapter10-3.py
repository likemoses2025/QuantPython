<<<<<<< HEAD
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

# @ 전체 종목 크롤링

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
engine.dispose()
con.close()
=======
import pandas as pd

# ! 재무재표 크롤링

# @ 삼성전자

from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:!!akswhr23@127.0.0.1:3306/stock_db")
query = """
    select * from kor_ticker
    where 기준일 = (select max(기준일) from kor_ticker) and 종목구분 = "보통주"
"""
ticker_list = pd.read_sql(query, con=engine)

i = 0
ticker = ticker_list["종목코드"][i]

url = f"http://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&gicode=A{ticker}"

# ? read_html을 통해 표 데이터만 가져온다
# ? +버튼을 눌러야 표시되는 항목이 있으므로 displayed_only=False를 통해 다 가져온다
data = pd.read_html(url, displayed_only=False)

# ? 전체 6개의 표를 가져오게 된다
print([item.head(3) for item in data])
# IFRS(연결)  2020/12  2021/12  2022/12  2023/09    전년동기 전년동기(%)
# 0      매출액   2721.0   2930.0   3404.0   2769.0  2560.0     8.2
# 1     매출원가   1334.0   1437.0   1594.0   1330.0  1209.0    10.1
# 2    매출총이익   1387.0   1493.0   1810.0   1438.0  1351.0     6.5,
#
# IFRS(연결)  2022/12  2023/03  2023/06  2023/09   전년동기 전년동기(%)
# 0      매출액    845.0    994.0    900.0    875.0  835.0     4.8
# 1     매출원가    386.0    468.0    438.0    424.0  398.0     6.5
# 2    매출총이익    459.0    526.0    462.0    450.0  436.0     3.2,
#
# IFRS(연결)  2020/12  2021/12  2022/12  2023/09
# 0                  자산   4338.0   4478.0   4611.0   4902.0
# 1  유동자산계산에 참여한 계정 펼치기   2227.0   2202.0   2275.0   2346.0
# 2                재고자산    395.0    362.0    468.0    547.0,
#
# IFRS(연결)  2022/12  2023/03  2023/06  2023/09
# 0                  자산   4611.0   4770.0   4818.0   4902.0
# 1  유동자산계산에 참여한 계정 펼치기   2275.0   2357.0   2317.0   2346.0
# 2                재고자산    468.0    494.0    549.0    547.0,
#
# IFRS(연결)  2020/12  2021/12  2022/12  2023/09
# 0    영업활동으로인한현금흐름    522.0    360.0    292.0    356.0
# 1           당기순손익    287.0    196.0    216.0    267.0
# 2  법인세비용차감전계속사업이익      NaN      NaN      NaN      NaN,
#
# IFRS(연결)  2022/12  2023/03  2023/06  2023/09
# 0    영업활동으로인한현금흐름      9.0    133.0     88.0    136.0
# 1           당기순손익     25.0    129.0     76.0     62.0
# 2  법인세비용차감전계속사업이익      NaN      NaN      NaN      NaN]

print(
    data[0].columns.tolist(),
    "\n",
    data[2].columns.tolist(),
    "\n",
    data[4].columns.tolist(),
    "\n",
)
# ['IFRS(연결)', '2020/12', '2021/12', '2022/12', '2023/09', '전년동기', '전년동기(%)']
#  ['IFRS(연결)', '2020/12', '2021/12', '2022/12', '2023/09']
#  ['IFRS(연결)', '2020/12', '2021/12', '2022/12', '2023/09']

# ? 불필요한 전년동기 , 전년동기(%) 열 삭제하기
data_fs_y = pd.concat(
    [data[0].iloc[:, ~data[0].columns.str.contains("전년동기")], data[2], data[4]]
)

# ? iloc 함수를 사용하여 모든 행 (:)을 선택하고, str.contains 함수를 사용하여 열 이름에 "전년동기"라는 부분
# ? 문자열이 포함되지 않은 열을 선택합니다. ~는 부정 연산자로, 조건을 반대로 만듭니다.

print(data_fs_y)
#                   IFRS(연결)  2020/12  2021/12  2022/12  2023/09
# 0                      매출액   2721.0   2930.0   3404.0   2769.0
# 1                     매출원가   1334.0   1437.0   1594.0   1330.0
# 2                    매출총이익   1387.0   1493.0   1810.0   1438.0
# 3    판매비와관리비계산에 참여한 계정 펼치기   1155.0   1269.0   1511.0   1235.0
# 4                      인건비    415.0    468.0    489.0    455.0
# ..                     ...      ...      ...      ...      ...
# 153        연결범위변동으로인한현금의증가      NaN      NaN      NaN      NaN
# 154                 환율변동효과     -1.0      0.0     -1.0      2.0
# 155            현금및현금성자산의증가    208.0     19.0   -261.0    603.0
# 156             기초현금및현금성자산    378.0    586.0    605.0    343.0
# 157             기말현금및현금성자산    586.0    605.0    343.0    947.0

# ? 첫번째 열 이름을 계정으로 변경
data_fs_y = data_fs_y.rename(columns={data_fs_y.columns[0]: "계정"})
print(data_fs_y.head())
#                       계정  2020/12  2021/12  2022/12  2023/09
# 0                    매출액   2721.0   2930.0   3404.0   2769.0
# 1                   매출원가   1334.0   1437.0   1594.0   1330.0
# 2                  매출총이익   1387.0   1493.0   1810.0   1438.0
# 3  판매비와관리비계산에 참여한 계정 펼치기   1155.0   1269.0   1511.0   1235.0
# 4                    인건비    415.0    468.0    489.0    455.0

# @ 데이터 크롤링
import requests as rq
from bs4 import BeautifulSoup
import re

page_data = rq.get(url)
page_data_html = BeautifulSoup(page_data.content, "html.parser")

fiscal_data = page_data_html.select("div.corp_group1 > h2")
print(fiscal_data)
# [<h2>000020</h2>, <h2>12월 결산</h2>]
fiscal_data_text = fiscal_data[1].text
#  ? 숫자 부분만 추출
fiscal_data_text = re.findall("[0-9]+", fiscal_data_text)

print(fiscal_data_text)
# ['12']

# ! 페이지 250
>>>>>>> 4c12af451286726e0965755adf5471580f79112d
