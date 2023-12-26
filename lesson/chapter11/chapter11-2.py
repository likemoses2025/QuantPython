from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
from datetime import datetime
import math
import pandas as pd
import numpy as np
from tqdm import tqdm
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
nationcode = "5"  # 미국 국가 코드
# @ 첫 페이지 생성
url = f"""https://investing.com/stock-screener/?sp=country::
{nationcode}|sector::a|industry::a|equityType::ORD%3Ceq_market_cap;1"""

# @ 셀레니움으로 해당 페이지 열기
driver.get(url)

# ? Screen results에 해당하는 부분은 종목이 들어 있는 표가 로딩된 이후 나타난다.
# ? 따라서 WebDriveWati()함수를 통해 해당 표가 로딩될 때까지 기다린다.
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="resultsTable"]/tbody'))
)

# ? 종목수를 크롤링하고 한페이지에 50개가 나타나므로 50으로 나누어 페이지를 계산한다.
end_num = driver.find_element(By.CLASS_NAME, value="js-total-results").text
end_num = math.ceil(int(end_num) / 50)

# @ for문을 통해 모든 페이지의 데이터를 크롤링
all_data_df = []

for i in tqdm(range(1, end_num + 1)):
    url = f"""https://investing.com/stock-screener/?sp=country::
        {nationcode}|sector::a|industry::a|equityType::ORD%3Ceq_market_cap;{i}"""
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="resultsTable"]/tbody')
            )
        )
    except:
        time.sleep(1)
        driver.refresh()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="resultsTable"]/tbody')
            )
        )

    html = BeautifulSoup(driver.page_source, "lxml")

    html_table = html.select("table.genTbl.openTbl.resultsStockScreenerTbl.elpTbl")
    df_table = pd.read_html(html_table[0].prettify())
    df_table_select = df_table[0][
        ["Name", "Symbol", "Exchange", "Sector", "Market Cap"]
    ]

    all_data_df.append(df_table_select)

    time.sleep(2)

all_data_df_bind = pd.concat(all_data_df, axis=0)

data_country = html.find(class_="js-search-input inputDropDown")["value"]  # type: ignore
all_data_df_bind["country"] = data_country
all_data_df_bind["date"] = datetime.today().strftime("%Y-%m-%d")
all_data_df_bind = all_data_df_bind[~all_data_df_bind["Name"].isnull()]
all_data_df_bind = all_data_df_bind[
    all_data_df_bind["Exchange"].isin(["NASDAQ", "NYSE", "NYSE Amex"])
]
all_data_df_bind = all_data_df_bind.drop_duplicates(["Symbol"])
all_data_df_bind.reset_index(inplace=True, drop=True)
all_data_df_bind = all_data_df_bind.replace({np.nan: None})

# driver.quit()

import pymysql

con = pymysql.connect(
    user="root", passwd="!!akswhr23", host="127.0.0.1", db="stock_db", charset="utf8"
)

mycursor = con.cursor()
query = """
    insert into global_ticker (Name, Symbol, Exchange, Sector, `Market Cap`, country, date)
    values (%s,%s,%s,%s,%s,%s,%s) as new
    on duplicate key update
    name=new.name,Exchange=new.Exchange,Sector=new.Sector,
    `Market Cap`=new.`Market Cap`; 
"""

args = all_data_df_bind.values.tolist()

mycursor.executemany(query, args)
con.commit()

con.close()
