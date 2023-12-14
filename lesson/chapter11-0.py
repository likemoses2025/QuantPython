import pandas as pd

# ! 유로 데이터 벤더 이용하기 - 팅고 API 키를 넣어야함
# @ 팅고 - Tingo

import keyring

keyring.set_password("tiingo", "BuHoJang", "")
api_key = keyring.get_password("tiingo", "BuHoJang")

from tiingo import TiingoClient
import pandas as pd
import keyring

api_key = keyring.get_password("tiingo", "BuHoJang")
config = {}
config["session"] = True
config["api_key"] = api_key
client = TiingoClient(config)

# @ API의 값은 JSON으로 전달되고 from_records() 매소드로 데이터 프레임으로 변경한다.
tickers = client.list_stock_tickers()
tickers_df = pd.DataFrame.from_records(tickers)

# * print(tickers_df.head())
# ? exchange - 거래소, priceCurrency - 거래 통화
#    ticker exchange assetType priceCurrency   startDate     endDate
# 0    -P-H     NYSE     Stock           USD
# 1    -P-S     NYSE     Stock           USD  2018-08-22  2023-05-05
# 2  000001      SHE     Stock           CNY  2007-01-04  2023-12-13
# 3  000002      SHE     Stock           CNY  2007-01-04  2023-12-13
# 4  000003      SHE     Stock           CNY

# * print(tickers_df.groupby(["exchange", "priceCurrency"])["ticker"].count())
# exchange   priceCurrency
#            USD               2459
# AMEX       USD                 79
# ASX        AUD                169
#            USD               2172
# BATS       USD                 13
# CSE        USD                 32
# EXPM       USD               1861
# LSE        USD                 12
# NASDAQ     USD              12631
# NMFQS      USD                 36
# NYSE       USD               7733
# NYSE ARCA  USD                 83
# NYSE MKT   USD                466
# NYSE NAT   USD                  3
# OTCBB      USD                651
# OTCCE      USD               1104
# OTCGREY    USD               4215
# OTCMKTS    USD               1188
# OTCQB      USD               1257
# OTCQX      USD                788
# PINK       USD              15277
# SHE        CNY               2554
#            HKD                 12
# SHEB       HKD                 42
# SHG        CNY               1933
#            USD                  6
# SHGB       USD                 44
# Name: ticker, dtype: int64

# @ APPLE Data
ticker_metadata = client.get_ticker_metadata("AAPL")
# *print(ticker_metadata)
# {
#     "ticker": "AAPL",
#     "name": "Apple Inc",
#     "description": "Apple Inc. (Apple) designs, manufactures and markets
#     "startDate": "1980-12-12",
#     "endDate": "2023-12-13",
#     "exchangeCode": "NASDAQ",
# }

# @ 기간별 애플 주식 데이터
historical_price = client.get_dataframe(
    "AAPL", startDate="2017-08-01", frequency="daily"
)
# * print(historical_price.head())
#                             close    high       low    open    volume  ...     adjLow    adjOpen  adjVolume  divCash  splitFactor
# date
# 2017-08-01 00:00:00+00:00  150.05  150.22  148.4100  149.10  24725526  ...  34.816656  34.978529   98902104      0.0          1.0
# 2017-08-02 00:00:00+00:00  157.14  159.75  156.1600  159.28  69222793  ...  36.634789  37.366734  276891172      0.0          1.0
# 2017-08-03 00:00:00+00:00  155.57  157.21  155.0200  157.05  26000738  ...  36.367348  36.843581  104002952      0.0          1.0
# 2017-08-04 00:00:00+00:00  156.39  157.40  155.6900  156.07  20349532  ...  36.524528  36.613675   81398128      0.0          1.0
# 2017-08-07 00:00:00+00:00  158.81  158.92  156.6701  157.06  21870321  ...  36.754457  36.845927   87481284      0.0          1.0

# @ get_fundamentals_daily() : 일별 가치지표 받기
fundamentals_daily = client.get_fundamentals_daily("AAPL")
fundamentals_daily_df = pd.DataFrame.from_records(fundamentals_daily)
# * print(fundamentals_daily_df) - marketCap : 시가총액
#                          date     marketCap  enterpriseVal    peRatio    pbRatio  trailingPEG1Y
# 0    2020-12-14T00:00:00.000Z  2.082747e+12   2.104240e+12  36.277836  31.876013     -27.571155
# 1    2020-12-15T00:00:00.000Z  2.187072e+12   2.208565e+12  38.095005  33.472693     -28.952203
# 2    2020-12-16T00:00:00.000Z  2.185875e+12   2.207368e+12  38.074152  33.454371     -28.936355
# 3    2020-12-17T00:00:00.000Z  2.201096e+12   2.222589e+12  38.339280  33.687329     -29.137853
# 4    2020-12-18T00:00:00.000Z  2.166122e+12   2.187615e+12  37.730081  33.152049     -28.674862
# ..                        ...           ...            ...        ...        ...            ...
# 762  2023-12-07T00:00:00.000Z  3.037262e+12   3.086795e+12  31.313596  48.873013       2.244141
# 763  2023-12-08T00:00:00.000Z  3.059776e+12   3.109309e+12  31.545704  49.235277       2.260775
# 764  2023-12-11T00:00:00.000Z  3.020221e+12   3.069754e+12  31.137903  48.598799       2.231550
# 765  2023-12-12T00:00:00.000Z  3.044141e+12   3.093674e+12  31.384518  48.983705       2.249224
# 766  2023-12-13T00:00:00.000Z  3.094953e+12   3.144486e+12  31.908372  49.801316       2.286767


# @ get_fundamentals_statements() : 제무제표 받기
fundamentals_stmnts = client.get_fundamentals_statements(
    "AAPL", startDate="2019-01-01", asReported=True, fmt="csv"
)
print(fundamentals_stmnts)

df_fs = pd.DataFrame([x.split(",") for x in fundamentals_stmnts.split("\n")])
df_fs.columns = df_fs.iloc[0]
df_fs = df_fs[1:]
df_fs.set_index("date", drop=True, inplace=True)
df_fs = df_fs[df_fs.index != ""]

print(df_fs.head())
# 0           year quarter    statementType        dataCode          value
# date
# 2023-11-03  2023       4  incomeStatement          ebitda  30653000000.0
# 2023-11-03  2023       4     balanceSheet     debtCurrent  15807000000.0
# 2023-11-03  2023       4  incomeStatement  netIncComStock  22956000000.0
# 2023-11-03  2023       4         cashFlow            ncfi   2394000000.0
# 2023-11-03  2023       4     balanceSheet       taxAssets            0.0
