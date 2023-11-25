import pandas as pd
import requests as rq
from bs4 import BeautifulSoup
import re
from io import BytesIO

# ! 개별종목 크롤링

# @ 최근 영업일 기준 데이터 받기
url = "https://finance.naver.com/"
data = rq.get(url)  # type: ignore
data_html = BeautifulSoup(data.content, "html.parser")
# ID가 "time"인 요소 선택
time_element = data_html.find(id="time")

print(time_element)
# <span id="time"> 2023.11.24<span>장마감</span> </span>

biz_day = None

if time_element:
    # 정규식을 사용하여 날짜 부분 추출
    match = re.search(r"\d{4}.\d{2}.\d{2}", time_element.get_text(strip=True))
    if match:
        extracted_date = match.group()
        biz_day = re.findall("[0-9]+", extracted_date)
        biz_day = "".join(biz_day)

    else:
        print("날짜를 찾을 수 없습니다.")
else:
    print("ID 'time'을 찾을 수 없습니다.")

print("오늘날짜:", biz_day)
