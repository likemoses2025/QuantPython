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

# @ Page Down - 윈도우에서 가장 하단까지 스크롤 명령어
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)

# @ Page Down - 모든 페이지가 나올때까지 스크롤 다운 실행
# ? 현재의 창높이를 prev_height에 저장
prev_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # ? 셀레니움을 통해 가장 하단까지 스크롤 내림
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    # ? 2초 쉬기
    time.sleep(2)
    # ? 현재의 높이를 curr_height에 저장
    curr_height = driver.execute_script("return document.body.scrollHeight")
    # ? 현재의 높이와 이전의 높이가 같다면(더이상 인피니티스크롤이 없다면) 종료
    if curr_height == prev_height:
        break
    # ? 현재의 높이를 이전 높이로 저장하고 처름부터 실행
    prev_height = curr_height

html = BeautifulSoup(driver.page_source, "lxml")
txt = html.find_all(class_="title_link _cross_trigger")
print("scraping", txt)
# [<a class="title_link _cross_trigger" data-cr-gdid="90000004_00AFDF200003A61F00000000" href="https://cafe.naver.com/vilab/239135?art=ZXh0ZXJuYWwtc2VydmljZS1uYXZlci1zZWFyY2gtY2FmZS1wcg.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjYWZlVHlwZSI6IkNBRkVfVVJMIiwiY2FmZVVybCI6InZpbGFiIiwiYXJ0aWNsZUlkIjoyMzkxMzUsImlzc3VlZEF0IjoxNzAwNzI5MTQ1NjE5fQ.qPn5IITC8S2phjNE_t0Atxk64ESQguoK4MYlKcExu84" onclick="return goOtherCR(this, 'a=rvw*c.link&amp;r=1&amp;i=90000004_00AFDF200003A61F00000000&amp;u='+urlencode(this.href))" target="_blank">투자에 정답을 얻는 책읽기(투자 독서 모임)</a>, <a class="title_link _cross_trigger" data-cr-gdid="90000004_00AFDF200003A5ED00000000" href="https://cafe.naver.com/vilab/239085?art=ZXh0ZXJuYWwtc2VydmljZS1uYXZlci1zZWFyY2gtY2FmZS1wcg.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjYWZlVHlwZSI6IkNBRkVfVVJMIiwiY2FmZVVybCI6InZpbGFiIiwiYXJ0aWNsZUlkIjoyMzkwODUsImlzc3VlZEF0IjoxNzAwNzI5MTQ1NjE5fQ.wDm4l
txt_list = [i.get_text() for i in txt]
print(txt_list[0:10])
# [
#     "투자에 정답을 얻는 책읽기(투자 독서 모임)",
#     "투자의 정답을 얻는 책읽기(투자 독서 모임)",
#     "투자의 정답을 얻는 책읽기(주식 투자 독서 모임 모집)",
#     "투자의 정답을 얻는 책읽기(투자 독서 모임)",
#     "《헤지펀드 열전》(완역 개정판) 맛보기 pdf 파일",
#     "[서평] 과거의 검증, 미래의 투자",
#     "[서평] 과거의 검증, 미래의 투자 (어려운 시기를 이겨내는 최선의 투자법을 찾아서) / 안티 일마넨...",
#     "20231011 멱(冪)파레토 독서법",
#     "Post 형식의 웹 데이터를 크롤링 해보자",
#     "최근 읽은 책 2권",
# ]
# @ 열려있는 창 종료
driver.quit()
