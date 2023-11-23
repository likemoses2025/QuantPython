import requests as rq
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


#! 동적 크롤링과 정규 표현식
# ? 정적 크롤링은 requests를 사용하고 동적 크롤링은 selenium을 사용한다.

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    options=chrome_options, service=Service(ChromeDriverManager().install())
)

url = "https://www.naver.com/"
driver.get(url)
driver.page_source[1:1000]
# html lang="ko" class="fzoom" data-dark="false"><head><script async="" type="text/javascript" src="https://ssl.pstatic.net/tveta/libs/ndpsdk/prod/ndp-core.js"></script> <meta charset="utf-8"> <meta name="Referrer" content="origin"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=1190"> <title>NAVER</title> <meta name="apple-mobile-web-app-title" content="NAVER"> <meta name="robots" content="index,nofollow"> <meta name="description" content="네이버 메인에서 다양한 정보와 유용한 컨텐츠를 만나 보세요"> <meta property="og:title" content="네이버"> <meta property="og:url" content="https://www.naver.com/"> <meta property="og:image" content="https://s.pstatic.net/static/www/mobile/edit/2016/0705/mobile_212852414260.png"> <meta property="og:description" content="네이버 메인에서 다양한 정보와 유용한 컨텐츠를 만나 보세요"> <meta name="twitter:card" content="summary"> <meta name="twitter:title" content=""> <meta name="twitter:url" content="https://www.naver.com/"> <meta name="twitter:image" content="https:/
# driver.find_element(By.LINK_TEXT, value="뉴스").click()
# driver.back()  # ? 뒤로가기
driver.find_element(By.CLASS_NAME, value="search_input").send_keys("퀀트투자 포트폴리오 만들기")
driver.find_element(By.CLASS_NAME, value="btn_search").send_keys(Keys.ENTER)

driver.find_element(By.CLASS_NAME, value="box_window").clear()  # 검색어 삭제
driver.find_element(By.CLASS_NAME, value="box_window").send_keys("이현열 퀀트")  # 검색창 입력
driver.find_element(By.CLASS_NAME, value="bt_search").click()  # 서치 버튼 클릭

# @ XPATH : xml 중 특정 값의 태그나 속성을 찾기 쉽게 만든 주소 //*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[2]/a
# 네이버 View Tab으로 이동
driver.find_element(
    By.XPATH,
    value="/html/body/div[3]/div[1]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]",
).click()


driver.find_element(
    By.XPATH,
    value="/html/body/div[3]/div[2]/div/div[1]/div/div[1]/div/div[2]/a",
).click()

driver.find_element(
    By.XPATH,
    value="/html/body/div[3]/div[2]/div/div[1]/div/div[2]/ul/li[2]/div/div/a[2]",
).click()
#! 213 page부터 하기
