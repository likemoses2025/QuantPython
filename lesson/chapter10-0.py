import pandas as pd
import requests as rq
from bs4 import BeautifulSoup
import re
from io import BytesIO

# ! 국내 주식 데이터 수집

# @ 최근 영업일 기준 데이터 받기
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


# ! 업종분류 현황 크롤링

# @ 1. OTP 받아오기
gen_otp_url = "http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd"
gen_otp_stk = {
    "mktId": "STK",  # 코스피
    "trdDd": biz_day,
    "money": 1,
    "csvxls_isNo": "false",
    "name": "fileDown",
    "url": "dbms/MDC/STAT/standard/MDCSTAT03901",
}
# ? headers에 Referer를 주는 이유는 지나온 과정의 흔적을 보여줌으로 로봇으로 인식을 피하기 위해서이다.
headers = {"Referer": "http://data.krx.co.kr/contents/MDC/MDI/mdiLoader"}
otp_stk = rq.post(gen_otp_url, gen_otp_stk, headers=headers).text
print(otp_stk)
# E3QYxRw+guOeN5kZgZ0Hk4inVFw9fL8jwjRdsL6HTm0RtSksuLS7Bnxpl86F7dAOkunw9BBwugQaSjGAcH15ebJEa8xgQ+kVLs2n1gwo93stBgM+
# EFJCxYg3zco1gIgRZqIo4cIzoURnTI8+MmkJ4m8vFLhSKmM794gFu+ThsO31lY4woqehX8j6OlXFDcfHdV4NbYo4+D2Rwcfj24VnU3Zpq3ik/Dyw3FdyOXhJkBI=

# @ 2. 코스피 OTP를 제출하고 EUC-KR로 인코딩된 데이터 받아오기 (코스피)
down_url = "http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd"
down_sector_stk = rq.post(down_url, {"code": otp_stk}, headers=headers)
# 받은 데이터의 content부분을 BytesIO()를 통해 바이너리 스트림 형태로 변환하고 read_csv()를 통해 데이터를 읽는다.
sector_stk = pd.read_csv(BytesIO(down_sector_stk.content), encoding="EUC-KR")

print(sector_stk.head())
#      종목코드      종목명   시장구분   업종명      종가  대비   등락률           시가총액
# 0  095570   AJ네트웍스  KOSPI  서비스업    4155  -5 -0.12   188025213645
# 1  006840    AK홀딩스  KOSPI  기타금융   17950 -40 -0.22   237793719950
# 2  027410      BGF  KOSPI  기타금융    3535   5  0.14   338358856185
# 3  282330   BGF리테일  KOSPI   유통업  131100   0  0.00  2265920076600
# 4  138930  BNK금융지주  KOSPI  기타금융    7130  20  0.28  2296490562940

# @ 3. 코스닥 OTP를 제출하고 EUC-KR로 인코딩된 데이터 받아오기 (코스닥)
gen_otp_ksq = {
    "mktId": "KSQ",  # 코스피
    "trdDd": biz_day,
    "money": 1,
    "csvxls_isNo": "false",
    "name": "fileDown",
    "url": "dbms/MDC/STAT/standard/MDCSTAT03901",
}

otp_ksq = rq.post(gen_otp_url, gen_otp_ksq, headers=headers).text
# E3QYxRw+guOeN5kZgZ0Hk6yUxzvq9eohKSo7H7GN1LURtSksuLS7Bnxpl86F7dAOkunw9BBwugQaSjGAcH15ebJEa8xgQ+kVLs2n1gwo93v+lNE/
# mS3HSeH9JSPc/lHYZqIo4cIzoURnTI8+MmkJ4m8vFLhSKmM794gFu+ThsO31lY4woqehX8j6OlXFDcfHdV4NbYo4+D2Rwcfj24VnU3Zpq3ik/Dyw3FdyOXhJkBI=
down_sector_ksq = rq.post(down_url, {"code": otp_ksq}, headers=headers)
sector_ksq = pd.read_csv(BytesIO(down_sector_ksq.content), encoding="EUC-KR")
print(sector_ksq.head())
#      종목코드         종목명    시장구분    업종명     종가   대비   등락률          시가총액
# 0  060310          3S  KOSDAQ  기계·장비   2275    0  0.00  110420860550
# 1  054620         APS  KOSDAQ     금융   6540  -60 -0.91  133378205340
# 2  265520       AP시스템  KOSDAQ    반도체  20100 -300 -1.47  307156562100
# 3  211270        AP위성  KOSDAQ   통신장비  14600 -320 -2.14  220201638400
# 4  126600  BGF에코머티리얼즈  KOSDAQ     화학   4260   40  0.95  230181751500

# @ 코스피 , 코스닥 데이터 합치기
# ? concat으로 합치기 , reset_index를 통해 인덱스 리셋, drop=True통해 index 셋팅 열 삭제
krx_sector = pd.concat([sector_stk, sector_ksq]).reset_index(drop=True)
# ? str.strip()을 통해 종목명에 공백을 제거
krx_sector["종목명"] = krx_sector["종목명"].str.strip()
krx_sector["기준일"] = biz_day
print("KRX SECTOR", krx_sector.head())
#    종목코드      종목명   시장구분   업종명      종가  대비   등락률           시가총액       기준일
# 0  095570   AJ네트웍스  KOSPI  서비스업    4155  -5 -0.12   188025213645  20231124
# 1  006840    AK홀딩스  KOSPI  기타금융   17950 -40 -0.22   237793719950  20231124
# 2  027410      BGF  KOSPI  기타금융    3535   5  0.14   338358856185  20231124
# 3  282330   BGF리테일  KOSPI   유통업  131100   0  0.00  2265920076600  20231124
# 4  138930  BNK금융지주  KOSPI  기타금융    7130  20  0.28  2296490562940  20231124

# @ 개별종목 크롤링하기
gen_otp_url = "http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd"
gen_otp_data = {
    "searchType": "1",
    "mktId": "ALL",
    "trdDd": biz_day,
    "csvxls_isNo": "false",
    "name": "fileDown",
    "url": "dbms/MDC/STAT/standard/MDCSTAT03501",
}
headers = {"Referer": "http://data.krx.co.kr/contents/MDC/MDI/mdiLoader"}
otp = rq.post(gen_otp_url, gen_otp_data, headers=headers).text

down_url = "http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd"
krx_ind = rq.post(down_url, {"code": otp}, headers=headers)

krx_ind = pd.read_csv(BytesIO(krx_ind.content), encoding="EUC-KR")
krx_ind["종목명"] = krx_ind["종목명"].str.strip()
krx_ind["기준일"] = biz_day

print(krx_ind.head())
#      종목코드     종목명     종가   대비   등락률     EPS    PER  선행 EPS  선행 PER      BPS   PBR  주당배당금  배당수익률       기준일
# 0  060310      3S   2275    0  0.00    30.0  75.83     NaN     NaN    947.0  2.40      0   0.00  20231124
# 1  095570  AJ네트웍스   4155   -5 -0.12   201.0  20.67   612.0    6.79   8076.0  0.51    270   6.50  20231124
# 2  006840   AK홀딩스  17950  -40 -0.22     NaN    NaN     NaN     NaN  41948.0  0.43    200   1.11  20231124
# 3  054620     APS   6540  -60 -0.91   505.0  12.95     NaN     NaN  10864.0  0.60      0   0.00  20231124
# 4  265520   AP시스템  20100 -300 -1.47  5463.0   3.68  5685.0    3.54  17980.0  1.12    270   1.34  20231124


# @ 데이터 정리하기
# ? 1. 두 데이터에 공통으로 존재하지 않는 종목 찾아내기
# ? symmetric_difference를 통해 하나의 데이터만 있는 종목을 찾는다 (선박펀드,광물펀드,해외종목)
diff = list(set(krx_sector["종목명"]).symmetric_difference(set(krx_ind["종목명"])))
print(diff)
# [
#     "헝셩그룹",
#     "NH올원리츠",
#     "삼성FN리츠",
#     "한화리츠",
#     "한국ANKOR유전",
#     ...
#     "맵스리얼티1",
#     "SK리츠",
#     "프레스티지바이오파마",
#     "이지스밸류리츠",
#     "디앤디플랫폼리츠",
#     "글로벌에스엠",
# ]

# @ 두 데이터를 합치기
# ? merge함수는 on 조건을 기준으로 데이터를 합친다. intersection()메소드는 공통으로 존재하는
# ? [종목코드,종목명,종가,대비,등락률] 열을 기준으로 입력한다. how=outer
kor_ticker = pd.merge(
    krx_sector,
    krx_ind,
    on=krx_sector.columns.intersection(krx_ind.columns).tolist(),
    how="outer",
)

print("KOR TICKER", kor_ticker)
#       종목코드      종목명    시장구분     업종명      종가   대비   등락률           시가총액       기준일      EPS    PER   선행 EPS  선행 PER      BPS   PBR   주당배당금  배당수익률
# 0     095570   AJ네트웍스   KOSPI    서비스업    4155   -5 -0.12   188025213645  20231124    201.0  20.67    612.0    6.79   8076.0  0.51   270.0   6.50
# 1     006840    AK홀딩스   KOSPI    기타금융   17950  -40 -0.22   237793719950  20231124      NaN    NaN      NaN     NaN  41948.0  0.43   200.0   1.11
# 2     027410      BGF   KOSPI    기타금융    3535    5  0.14   338358856185  20231124    247.0  14.31      NaN     NaN  16528.0  0.21   110.0   3.11
# 3     282330   BGF리테일   KOSPI     유통업  131100    0  0.00  2265920076600  20231124  11203.0  11.70  12456.0   10.52  55724.0  2.35  4100.0   3.13
# 4     138930  BNK금융지주   KOSPI    기타금융    7130   20  0.28  2296490562940  20231124   2404.0   2.97   2440.0    2.92  30468.0  0.23   625.0   8.77
# ...      ...      ...     ...     ...     ...  ...   ...            ...       ...      ...    ...      ...     ...      ...   ...     ...    ...
# 2645  024060     흥구석유  KOSDAQ      유통    8310  170  2.09   124650000000  20231124    183.0  45.41      NaN     NaN   5508.0  1.51   150.0   1.81
# 2646  010240       흥국  KOSDAQ   기계·장비    5950    0  0.00    73320041200  20231124    740.0   8.04      NaN     NaN   7971.0  0.75   220.0   3.70
# 2647  189980   흥국에프엔비  KOSDAQ  음식료·담배    2015  -45 -2.18    80877721405  20231124    309.0   6.52    255.0    7.92   2295.0  0.88    40.0   1.99
# 2648  037440       희림  KOSDAQ   기타서비스    8150  -30 -0.37   113468171250  20231124    567.0  14.37      NaN     NaN   5186.0  1.57   150.0   1.84
# 2649  238490       힘스  KOSDAQ     반도체    6490   90  1.41    73416411640  20231124      NaN    NaN      NaN     NaN   5656.0  1.15     0.0   0.00

# ? 일반적인 종목과 스팩, 우선주, 리츠, 기타 주식을 구분한다.
# * contains을 통해 "스팩", "제n호"가 들어가는 종목명을 찾는다
print(kor_ticker[kor_ticker["종목명"].str.contains("스팩[0-9]+호")]["종목명"].values)
# [
#     "엔에이치스팩19호"
#     "DB금융스팩10호"
#     "DB금융스팩11호"
#     "미래에셋드림스팩1호"
#     ...
#     "엔에이치스팩28호"
#     "엔에이치스팩29호"
#     "유진스팩6호"
#     "유진스팩7호"
#     "유진스팩8호"
#     "유진스팩9호"
# ]


# * 국내 종목 중 종목코드 끝이 0이 아닌 종목은 우선주에 해당
print(kor_ticker[kor_ticker["종목코드"].str[-1:] != "0"]["종목명"].values)
# [
#     "BYC우"
#     "CJ4우(전환)"
#     "CJ씨푸드1우"
#     "CJ우"
#     "CJ제일제당 우"
#     ...
#     "흥국화재우"
#     "대호특수강우"
#     "소프트센우"
#     "해성산업1우"
# ]
# ? 리츠 종목은 종목명이 "리츠"로 끝난다. endswith() 메소드를 통해 종목명을 찾는다
print(kor_ticker[kor_ticker["종목명"].str.endswith("리츠")]["종목명"].values)
# [
#     "ESR켄달스퀘어리츠"
#     "KB스타리츠"
#     "NH올원리츠"
#     "NH프라임리츠"
#     ...
#     "코람코더원리츠"
#     "코람코라이프인프라리츠"
#     "한화리츠"
# ]
