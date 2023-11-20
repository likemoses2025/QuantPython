import requests as rq
from bs4 import BeautifulSoup

#! 금융 속보 크롤링

url = "https://finance.naver.com/news/news_list.naver?mode=LSS2D&section_id=101&section_id2=258"
news = rq.get(url)

news_html = BeautifulSoup(news.content, "html.parser")
news_html_select = news_html.select("dl>dd.articleSubject>a")
print(news_html_select[0:3])
# [<a href="/news/news_read.naver?article_id=0005217840&amp;office_id=009&amp;mode=LSS2D&amp;type=0§ion_id=101§ion_id2=258§ion_id3=&amp;date=20231120&amp;page=1" title="'큰형님' 잘 둔 현대차·SK그룹 ETF 수익도 든든">'큰형님' 잘 둔 현대차·SK그룹 ETF 수익도 든든</a>, <a href="/news/news_read.naver?article_id=0005217827&amp;office_id=009&amp;mode=LSS2D&amp;type=0§ion_id=101§ion_id2=258§ion_id3=&amp;date=20231120&amp;page=1" title='"에너지·인프라, 글로벌 M&amp;A 위축에도 유망"'>"에너지·인프라, 글로벌 M&amp;A 위축에도 유망"</a>, <a href="/news/news_read.naver?article_id=0004263903&amp;office_id=011&amp;mode=LSS2D&amp;type=0§ion_id=101§ion_id2=258§ion_id3=&amp;date=20231120&amp;page=1" title="[데이터로 보는 증시]채권 수익률 현황(11월 20일)">[데이터로 보는 증시]채권 수익률 현황(11월 20일)</a>]
news_html_select_list = [i.text for i in news_html_select]
print(news_html_select_list)
# [
#     "'큰형님' 잘 둔 현대차·SK그룹 ETF 수익도 든든",
#     '"에너지·인프라, 글로벌 M&A 위축에도 유망"',
#     "[데이터로 보는 증시]채권 수익률 현황(11월 20일)",
#     "스톰테크, 만족스러운 코스닥 데뷔…73% 상승 마감",
#     "비용 감소 호재에 타이어株 랠리",
#     "동화약품 감기약 '판콜에스', 올해 누적 매출 사상 첫 1위",
#     "변동성 커진 국내 증시에…돈 몰리는 ‘美 배당 성장주’ ETF [투자360]",
#     "[올댓차이나] 中 증시, 지원 기대·위안화 강세로 상승 마감…창업판 0.32%↑",
#     "[마감시황]2차전지주 뛰자…코스피도 '미소'",
#     "\"상호 돌봄으로 전쟁·폭력의 시대 마감해야\"...'삼성행복대상' 시상식 개최",
#     "'부가티·람보르기니까지'... 도민저축銀 11년 만에 파산 완료",
#     "뻥튀기 논란 파두 유탄 맞을라…연매출 10억으로 상장하려던 기업 전전긍긍",
#     "'법 개정'에 바람탄 로봇주…두산로보 상장 이래 최고가[핫종목]",
# ]
news_html_select_list2 = [i["title"] for i in news_html_select]
print(news_html_select_list2)
# [
#     "'큰형님' 잘 둔 현대차·SK그룹 ETF 수익도 든든",
#     '"에너지·인프라, 글로벌 M&A 위축에도 유망"',
#     "[데이터로 보는 증시]채권 수익률 현황(11월 20일)",
#     "스톰테크, 만족스러운 코스닥 데뷔…73% 상승 마감",
#     "비용 감소 호재에 타이어株 랠리",
#     "동화약품 감기약 '판콜에스', 1년 누적 매출 사상 첫 1위",
# ]
