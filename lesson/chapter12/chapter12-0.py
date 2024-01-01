import pandas as pd

#! 투자 참고용 데이터 수집

import keyring
import requests as rq
from io import BytesIO
import zipfile

# 전자공시시스템 API KEY
api_key = ""

codezip_url = f"""https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key={api_key}"""


codezip_data = rq.get(codezip_url)

# ? print(codezip_data.headers)

# {
#     "Cache-Control": "no-cache, no-store",
#     "Connection": "keep-alive",
#     "Set-Cookie": "WMONID=MGsEAWJSwbt; Expires=Tue, 31-Dec-2024 18:12:39 GMT; Path=/",
#     "Pragma": "no-cache",
#     "Expires": "0",
#     "Content-Transfer-Encoding": "binary",
#     "Content-Disposition": ": attachment; filename=CORPCODE.zip",
#     "Date": "Mon, 01 Jan 2024 09:12:39 GMT",
#     "Content-Type": "application/x-msdownload;charset=UTF-8",
#     "Content-Length": "1759598",
# }

# ? print(codezip_data.headers["Content-Disposition"])
# : attachment; filename=CORPCODE.zip

codezip_file = zipfile.ZipFile(BytesIO(codezip_data.content))

# ? print(codezip_file.namelist())
# ["CORPCODE.xml"]

import xmltodict
import json

code_data = codezip_file.read("CORPCODE.xml").decode("utf-8")
data_odict = xmltodict.parse(code_data)  # xml 을 dict로 변경
data_dict = json.loads(json.dumps(data_odict))  # json으로 변경
data = data_dict.get("result").get("list")
corp_list = pd.DataFrame(data)

# ? print(corp_list.head())
#   corp_code          corp_name stock_code modify_date
# 0  00434003                 다코       None    20170630
# 1  00434456               일산약품       None    20170630
# 2  00430964              굿앤엘에스       None    20170630
# 3  00432403               한라판지       None    20170630
# 4  00388953  크레디피아제이십오차유동화전문회사       None    20170630

# ? print(len(corp_list))
# 103782

# @ 비상장종목 필터링
# ? print(corp_list[corp_list["stock_code"].isin([None])].head())
#   corp_code          corp_name stock_code modify_date
# 0  00434003                 다코       None    20170630
# 1  00434456               일산약품       None    20170630
# 2  00430964              굿앤엘에스       None    20170630
# 3  00432403               한라판지       None    20170630
# 4  00388953  크레디피아제이십오차유동화전문회사       None    20170630

import pymysql
from sqlalchemy import create_engine

corp_list = corp_list[~corp_list.stock_code.isin([None])].reset_index(drop=True)

engine = create_engine("mysql+pymysql://root:!!akawhr23@127.0.0.1:3306/stock_db")
corp_list.to_sql(name="dart_code", con=engine, index=True, if_exists="append")
