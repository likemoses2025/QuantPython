import pandas as pd

#! 제무제표 다운로드

from yahooquery import Ticker
import numpy as np

data = Ticker("AAPL")
# @ print(data.asset_profile)   기업정보
# {'AAPL': {'address1': 'One Apple Park Way', 'city': 'Cupertino', 'state': 'CA', 'zip': '95014',
#           'country': 'United States', 'phone': '408 996 1010', 'website': 'https://www.apple.com',
#           'industry': 'Consumer Electronics', 'industryKey': 'consumer-electronics', 'industryDisp': 'Consumer Electronics',
#           'sector': 'Technology', 'sectorKey': 'technology', 'sectorDisp': 'Technology',
#           'longBusinessSummary': 'Apple Inc. designs, manufactures, and markets smartphones, personal computers,
#           'fullTimeEmployees': 161000,
#           'companyOfficers': [{'maxAge': 1, 'name': 'Mr. Timothy D. Cook', 'age': 61,
#                             'title': 'CEO & Director', 'yearBorn': 1961, 'fiscalYear': 2022,
#                             'totalPay': 16425933, 'exercisedValue': 0, 'unexercisedValue': 0},
#                             {'maxAge': 1, 'name': 'Mr. Luca  Maestri', 'age': 59, 'title': 'CFO & Senior VP', 'yearBorn': 1963,
#                                 'fiscalYear': 2022, 'totalPay': 5019783, 'exercisedValue': 0, 'unexercisedValue': 0},
#                             {'maxAge': 1, 'name': 'Mr. Jeffrey E. Williams', 'age': 58, 'title': 'Chief Operating Officer',
#                                 'yearBorn': 1964, 'fiscalYear': 2022, 'totalPay': 5018337, 'exercisedValue': 0, 'unexercisedValue': 0},
#                                 {'maxAge': 1, 'name': 'Ms. Katherine L. Adams', 'age': 58, 'title': 'Senior VP, General Counsel & Secretary',
#                                 'yearBorn': 1964, 'fiscalYear': 2022, 'totalPay': 5015208, 'exercisedValue': 0, 'unexercisedValue': 0},
#                                 {'maxAge': 1, 'name': "Ms. Deirdre  O'Brien", 'age': 55, 'title': 'Senior Vice President of Retail', 'yearBorn': 1967,
#                                 'fiscalYear': 2022, 'totalPay': 5019783, 'exercisedValue': 0, 'unexercisedValue': 0},
#                                 {'maxAge': 1, 'name': 'Mr. Chris  Kondo', 'title': 'Senior Director of Corporate Accounting', 'fiscalYear': 2022,
#                                 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. James  Wilson',
#                                 'title': 'Chief Technology Officer', 'fiscalYear': 2022, 'exercisedValue': 0, 'unexercisedValue': 0},
#                                 {'maxAge': 1, 'name': 'Suhasini  Chandramouli', 'title': 'Director of Investor Relations', 'fiscalYear': 2022,
#                                 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Greg  Joswiak',
#                                 'title': 'Senior Vice President of Worldwide Marketing', 'fiscalYear': 2022, 'exercisedValue': 0, 'unexercisedValue': 0},
#                                 {'maxAge': 1, 'name': 'Mr. Adrian  Perica', 'age': 48, 'title': 'Head of Corporate Development', 'yearBorn': 1974,
#                                 'fiscalYear': 2022, 'exercisedValue': 0, 'unexercisedValue': 0}], 'auditRisk': 4, 'boardRisk': 1, 'compensationRisk': 6,
#                                 'shareHolderRightsRisk': 1, 'overallRisk': 1, 'governanceEpochDate': '2023-12-01 09:00:00',
#                                 'compensationAsOfEpochDate': '2022-12-31 09:00:00', 'maxAge': 86400}}

# @print(data.summary_detail)  가격 배당 벨류에이션
# {
#     "AAPL": {
#         "maxAge": 1,
#         "priceHint": 2,
#         "previousClose": 194.68,
#         "open": 195.18,
#         "dayLow": 192.97,
#         "dayHigh": 195.41,
#         "regularMarketPreviousClose": 194.68,
#         "regularMarketOpen": 195.18,
#         "regularMarketDayLow": 192.97,
#         "regularMarketDayHigh": 195.41,
#         "dividendRate": 0.96,
#         "dividendYield": 0.005,
#         "exDividendDate": "2023-11-10 09:00:00",
#         "payoutRatio": 0.1533,
#         "fiveYearAvgDividendYield": 0.82,
#         "beta": 1.308,
#         "trailingPE": 31.530947,
#         "forwardPE": 29.830511,
#         "volume": 37149570,
#         "regularMarketVolume": 37149570,
#         "averageVolume": 54135890,
#         "averageVolume10days": 61144720,
#         "averageDailyVolume10Day": 61144720,
#         "bid": 0.0,
#         "ask": 0.0,
#         "bidSize": 1100,
#         "askSize": 1300,
#         "marketCap": 3011022159872,
#         "fiftyTwoWeekLow": 124.17,
#         "fiftyTwoWeekHigh": 199.62,
#         "priceToSalesTrailing12Months": 7.8558307,
#         "fiftyDayAverage": 185.3988,
#         "twoHundredDayAverage": 178.6491,
#         "trailingAnnualDividendRate": 0.94,
#         "trailingAnnualDividendYield": 0.0048284368,
#         "currency": "USD",
#         "fromCurrency": None,
#         "toCurrency": None,
#         "lastMarket": None,
#         "coinMarketCapLink": None,
#         "algorithm": None,
#         "tradeable": False,
#     }
# }

# @print(data.history().head())
#                         open        high         low       close     volume    adjclose  dividends
# symbol date
# AAPL   2023-01-03  130.279999  130.899994  124.169998  125.070000  112117500  124.374802        0.0
#        2023-01-04  126.889999  128.660004  125.080002  126.360001   89113600  125.657639        0.0
#        2023-01-05  127.129997  127.769997  124.760002  125.019997   80962700  124.325081        0.0
#        2023-01-06  126.010002  130.289993  124.889999  129.619995   87754700  128.899490        0.0
#        2023-01-09  130.470001  133.410004  129.889999  130.149994   70790800  129.426559        0.0

data_y = data.all_financial_data(frequency="a")
# print(data_y)
#          asOfDate periodType currencyCode  AccountsPayable  ...  TotalRevenue  TradeandOtherPayablesNonCurrent  TreasurySharesNumber  WorkingCapital
# symbol                                                      ...
# AAPL   2020-09-30        12M          USD     4.229600e+10  ...  2.745150e+11                     2.817000e+10                   NaN    3.832100e+10
# AAPL   2021-09-30        12M          USD     5.476300e+10  ...  3.658170e+11                     2.468900e+10                   NaN    9.355000e+09
# AAPL   2022-09-30        12M          USD     6.411500e+10  ...  3.943280e+11                     1.665700e+10                   NaN   -1.857700e+10
# AAPL   2023-09-30        12M          USD     6.261100e+10  ...  3.832850e+11                              NaN                   0.0   -1.742000e+09

# [4 rows x 158 columns]

# ? 인덱스 초기화
data_y.reset_index(inplace=True)
# ? 불필요한 열 제거
data_y = data_y.loc[:, ~data_y.columns.isin(["periodType", "currencyCode"])]
# ? melt()함수를 통해 세로로 긴 형태로 만든다
data_y = data_y.melt(id_vars=["symbol", "asOfDate"])
# ? nan을 None으로 변경한다.
data_y = data_y.replace([np.nan], None)
# ? freq열에 y를 입력
data_y["freq"] = "y"
# ? 열이름 변경
data_y.columns = ["ticker", "date", "account", "value", "freq"]

# @ print(data_y.head())
#   ticker       date             account          value freq
# 0   AAPL 2020-09-30     AccountsPayable  42296000000.0    y
# 1   AAPL 2021-09-30     AccountsPayable  54763000000.0    y
# 2   AAPL 2022-09-30     AccountsPayable  64115000000.0    y
# 3   AAPL 2023-09-30     AccountsPayable  62611000000.0    y
# 4   AAPL 2020-09-30  AccountsReceivable  16120000000.0    y

# @ 분기별 제무제표는 frequency = "q" 로 바꿈
data_q = data.all_financial_data(frequency="q")
data_q.reset_index(inplace=True)
data_q = data_q.loc[:, ~data_q.columns.isin(["periodType", "currencyCode"])]
data_q = data_q.melt(id_vars=["symbol", "asOfDate"])
data_q = data_q.replace([np.nan], None)
data_q["freq"] = "q"
data_q.columns = ["ticker", "date", "account", "value", "freq"]
# @ print(data_q.head())
#   ticker       date          account          value freq
# 0   AAPL 2022-09-30  AccountsPayable  64115000000.0    q
# 1   AAPL 2022-12-31  AccountsPayable  57918000000.0    q
# 2   AAPL 2023-03-31  AccountsPayable  42945000000.0    q
# 3   AAPL 2023-06-30  AccountsPayable  46699000000.0    q
# 4   AAPL 2023-09-30  AccountsPayable  62611000000.0    q
