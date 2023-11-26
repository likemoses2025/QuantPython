import json
import requests as rq
import pandas as pd
import time
from tqdm import tqdm
from bs4 import BeautifulSoup
import re

# ! WICS 기준 섹터 정보 크롤링

url = f"""https://www.wiseindex.com/Index/GetIndexComponets?ceil_yn=0&dt=20231123&sec_cd=G10"""
data = rq.get(url).json()

print(type(data))
# <class 'dict'>

print(data.keys())
# dict_keys(['info', 'list', 'sector', 'size'])

print(data["list"][0])
# {
#     "IDX_CD": "G10",
#     "IDX_NM_KOR": "WICS 에너지",
#     "ALL_MKT_VAL": 23129368,
#     "CMP_CD": "096770",
#     "CMP_KOR": "SK이노베이션",
#     "MKT_VAL": 8043587,
#     "WGT": 34.78,
#     "S_WGT": 34.78,
#     "CAL_WGT": 1.0,
#     "SEC_CD": "G10",
#     "SEC_NM_KOR": "에너지",
#     "SEQ": 1,
#     "TOP60": 3,
#     "APT_SHR_CNT": 56367116,
# }

print(data["sector"])
# [
#     {"SEC_CD": "G25", "SEC_NM_KOR": "경기관련소비재", "SEC_RATE": 9.8, "IDX_RATE": 0},
#     {"SEC_CD": "G35", "SEC_NM_KOR": "건강관리", "SEC_RATE": 9.09, "IDX_RATE": 0},
#     {"SEC_CD": "G50", "SEC_NM_KOR": "커뮤니케이션서비스", "SEC_RATE": 6.41, "IDX_RATE": 0},
#     {"SEC_CD": "G40", "SEC_NM_KOR": "금융", "SEC_RATE": 7.94, "IDX_RATE": 0},
#     {"SEC_CD": "G10", "SEC_NM_KOR": "에너지", "SEC_RATE": 1.89, "IDX_RATE": 100.0},
#     {"SEC_CD": "G20", "SEC_NM_KOR": "산업재", "SEC_RATE": 12.12, "IDX_RATE": 0},
#     {"SEC_CD": "G55", "SEC_NM_KOR": "유틸리티", "SEC_RATE": 0.95, "IDX_RATE": 0},
#     {"SEC_CD": "G30", "SEC_NM_KOR": "필수소비재", "SEC_RATE": 2.22, "IDX_RATE": 0},
#     {"SEC_CD": "G15", "SEC_NM_KOR": "소재", "SEC_RATE": 9.48, "IDX_RATE": 0},
#     {"SEC_CD": "G45", "SEC_NM_KOR": "IT", "SEC_RATE": 40.11, "IDX_RATE": 0},
# ]

# ? list부분의 데이터를 데이터프레임 형태로 변경 json_normalize는 jason을 DataFrame으로 변경한다.
data_pd = pd.json_normalize(data["list"])
print(data_pd.head())

url = "https://finance.naver.com/"
data = rq.get(url)
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

sector_code = ["G25", "G35", "G50", "G40", "G10", "G20", "G55", "G30", "G15", "G45"]
data_sector = []
for i in tqdm(sector_code):
    url = f"""https://www.wiseindex.com/Index/GetIndexComponets?ceil_yn=0&dt={biz_day}&sec_cd={i}"""
    data = rq.get(url).json()
    data_pd = pd.json_normalize(data["list"])

    data_sector.append(data_pd)
    time.sleep(2)

kor_sector = pd.concat(data_sector, axis=0)
kor_sector = kor_sector[["IDX_CD", "CMP_CD", "CMP_KOR", "SEC_NM_KOR"]]
kor_sector["기준일"] = biz_day
kor_sector["기준일"] = pd.to_datetime(kor_sector["기준일"])

print(kor_sector)
#     IDX_CD  CMP_CD      CMP_KOR SEC_NM_KOR        기준일
# 0      G25  005380          현대차    경기관련소비재 2023-11-24
# 1      G25  000270           기아    경기관련소비재 2023-11-24
# 2      G25  012330        현대모비스    경기관련소비재 2023-11-24
# 3      G25  090430       아모레퍼시픽    경기관련소비재 2023-11-24
# 4      G25  161390  한국타이어앤테크놀로지    경기관련소비재 2023-11-24
# ..     ...     ...          ...        ...        ...
# 662    G45  127980        화인써키트         IT 2023-11-24
# 663    G45  372800       아이티아이즈         IT 2023-11-24
# 664    G45  424760          벨로크         IT 2023-11-24
# 665    G45  065690          파커스         IT 2023-11-24
# 666    G45  033200          모아텍         IT 2023-11-24

# @ mysql 삽입

import pymysql

con = pymysql.connect(
    user="root", passwd="!!akswhr23", host="127.0.0.1", db="stock_db", charset="utf8"
)
mycursor = con.cursor()
query = f"""
    insert into kor_sector (IDX_CD, CMP_CD, CMP_KOR, SEC_NM_KOR, 기준일)
    values (%s,%s,%s,%s,%s) as new
    on duplicate key update
    IDX_CD = new.IDX_CD, CMP_KOR=new.CMP_KOR, SEC_NM_KOR=new.SEC_NM_KOR
"""
args = kor_sector.values.tolist()
mycursor.executemany(query, args)
con.commit()
con.close()
