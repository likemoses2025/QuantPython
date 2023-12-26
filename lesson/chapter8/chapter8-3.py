import requests as rq
import pandas as pd

#! 표 크롤링하기

url = "https://en.wikipedia.org/wiki/List_of_countries_by_stock_market_capitalization"
tbl = pd.read_html(url)

print(tbl[0].head)

#            Country Total market cap (in mil. US$)[2]  Total market cap (% of GDP)[3] Number of domestic companies listed[4]  Year
# 0   United States                          44719661                           194.5                                   4266  2020
# 1           China                          13214311                            83.0                                   4154  2020
# 2           Japan                           6718220                           122.2                                   3754  2020
# 3       Hong Kong                           6130420                          1768.8                                   2353  2020
# 4           India                      3,612,985[5]                           103.0                                   5270  2023
# ..            ...                               ...                             ...                                    ...   ...
# 95        Algeria                               371                             0.2                                    ...  2018
# 96       Paraguay                               313                             3.5                                     55  1999
# 97        Uruguay                               284                             1.4                                     17  1996
# 98       Eswatini                               234                             6.8                                      6  2007
# 99        Bermuda                               220                            39.6                                     13  2020

# [100 rows x 5 columns]>
