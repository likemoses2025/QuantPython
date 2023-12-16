import pandas as pd

# ! 주가 다운로드
import yfinance as yf

price = yf.download("AAPL")
# * print(price.head())
#                 Open      High       Low     Close  Adj Close     Volume
# Date
# 1980-12-12  0.128348  0.128906  0.128348  0.128348   0.099319  469033600
# 1980-12-15  0.122210  0.122210  0.121652  0.121652   0.094137  175884800
# 1980-12-16  0.113281  0.113281  0.112723  0.112723   0.087228  105728000
# 1980-12-17  0.115513  0.116071  0.115513  0.115513   0.089387   86441600
# 1980-12-18  0.118862  0.119420  0.118862  0.118862   0.091978   73449600

price = yf.download("AAPL", start="2000-01-01", progress=False)
# * print(price.head())
#                 Open      High       Low     Close  Adj Close     Volume
# Date
# 2000-01-03  0.936384  1.004464  0.907924  0.999442   0.847207  535796800
# 2000-01-04  0.966518  0.987723  0.903460  0.915179   0.775779  512377600
# 2000-01-05  0.926339  0.987165  0.919643  0.928571   0.787131  778321600
# 2000-01-06  0.947545  0.955357  0.848214  0.848214   0.719014  767972800
# 2000-01-07  0.861607  0.901786  0.852679  0.888393   0.753073  460734400

# @ 미국이 아닌 다른 나라의 경우는 국가코드를 같이 넣어줘야한다. 미국은 티커만 넣은면 오케이
price = yf.download("8035.T", progress=False)  # ? 종목코드 8035 , 일본 국가코드 T
# * print(price)
#                Open     High      Low    Close     Adj Close   Volume
# Date
# 2000-01-04  13800.0  14000.0  12890.0  13010.0  11240.479492   231000
# 2000-01-05  11510.0  12140.0  11020.0  11950.0  10324.649414   672000
# 2000-01-06  12000.0  12600.0  11000.0  11020.0   9521.147461   688000
# 2000-01-07  10800.0  11530.0  10530.0  10920.0   9434.748047  1203000
# 2000-01-10  10920.0  10920.0  10920.0  10920.0   9434.748047        0
# ...             ...      ...      ...      ...           ...      ...
# 2023-12-11  22730.0  23080.0  22605.0  23005.0  23005.000000  2969700
# 2023-12-12  23850.0  24020.0  23260.0  23345.0  23345.000000  2947300
# 2023-12-13  23675.0  24715.0  23650.0  24445.0  24445.000000  5393200
# 2023-12-14  24800.0  25065.0  23990.0  24035.0  24035.000000  4493500
# 2023-12-15  24365.0  24960.0  24285.0  24370.0  24370.000000  4307400
