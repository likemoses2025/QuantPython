import pandas as pd

# ! 수정주가 크롤링
# @ 수정주가가 필요한 이유?
# @ 삼성전자 2018년5월 1주를 50주로 나누는 액면분할 실시
# @ 265만원에서 5만3천원으로 변경
# @ 가격으로만 보면 -98% 손실로 보임
# @ 액면불할전 모든 주가를 50으로 나누어 연속성을 갖게함 => 수정주가

# ! 개별종목 주가 크롤링
url = "https://finance.naver.com/item/sise.naver?code=005930"
