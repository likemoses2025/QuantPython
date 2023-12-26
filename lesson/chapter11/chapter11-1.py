# import pandas as pd

# ! 해외 티커 수집하기 - 미국의 보통주 전종목 크롤링

from pytest import console_main
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import math
import pandas as pd

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(
    options=options, service=Service(ChromeDriverManager().install())
)
url = "https://www.investing.com/stock-screener/?sp=country::5|sector::a|industry::a|equityType::ORD%3Ceq_market_cap;1"
driver.get(url)

# * HTML 정보 가져오기
html = BeautifulSoup(driver.page_source, "lxml")
print("HTML", html)

print(html.find(class_="js-search-input inputDropDown")["value"])  # type: ignore
html_table = html.select("table.genTbl.openTbl.resultsStockScreenerTbl.elpTbl")
print(html_table[0])

df_table = pd.read_html(html_table[0].prettify())
df_table_result = df_table[0]

df_table_select = df_table[0][["Name", "Symbol", "Exchange", "Sector", "Market Cap"]]
print(df_table_select.head())
#          Name Symbol Exchange              Sector Market Cap
# 0       Apple   AAPL   NASDAQ          Technology      3.08T
# 1   Microsoft   MSFT   NASDAQ          Technology      2.76T
# 2  Alphabet C   GOOG   NASDAQ          Technology      1.68T
# 3  Alphabet A  GOOGL   NASDAQ          Technology      1.66T
# 4  Amazon.com   AMZN   NASDAQ  Consumer Cyclicals      1.56T

end_num = driver.find_element(By.CLASS_NAME, value="js-total-results").text
print(math.ceil(int(end_num) / 50))  # 166

driver.quit()
