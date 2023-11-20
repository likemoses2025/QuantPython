import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

#! 기업 공시 채널에서 오늘의 공시 불러오기

url = "https://kind.krx.co.kr/disclosure/todaydisclosure.do"
payload = {
    "method": "searchTodayDisclosureSub",
    "currentPageSize": "15",
    "pageIndex": "1",
    "orderMode": "0",
    "orderStat": "D",
    "forward": "todaydisclosure_sub",
    "chose": "S",
    "todayFlag": "N",
    "selDate": "2022-07-27",
}

data = rq.post(url, data=payload)
html = BeautifulSoup(data.content, "html.parser")
print(html)

# @ 데이터프레임 형태로 변형하기
html_unicode = html.prettify
tbl = pd.read_html(html.prettify())
print(tbl[0].head())
#   Unnamed: 0 Unnamed: 1                         Unnamed: 2 Unnamed: 3  Unnamed: 4
# 0      19:08      지나인제약         기타시장안내(상장적격성 실질심사 사유추가 안내)    코스닥시장본부         NaN
# 1      19:00      지나인제약                             최대주주변경      지나인제약         NaN
# 2      18:57      지나인제약        최대주주 변경을 수반하는 주식 담보제공 계약 체결      지나인제약         NaN
# 3      18:45     디딤이앤에프  [정정]  최대주주 변경을 수반하는 주식 담보제공 계약 체결     디딤이앤에프  공시차트  주가차트
# 4      18:39       케이옥션                         추가상장(무상증자)    코스닥시장본부  공시차트  주가차트
