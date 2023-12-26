import requests as rq
from bs4 import BeautifulSoup
import time

# @ 모든 페이지 크롤링하기 (pagnation 적용된 값 가져오기)

text_list = []
author_list = []
infor_list = []

for i in range(1, 100):
    url = f"https://quotes.toscrape.com/page/{i}"
    quote = rq.get(url)
    quote_html = BeautifulSoup(quote.content, "html.parser")

    quote_text = quote_html.select("div.quote>span.text")
    quote_text_list = [i.text for i in quote_text]

    quote_author = quote_html.select("div.quote>span>small.author")
    quote_author_list = [i.text for i in quote_author]

    quote_link = quote_html.select("div.quote>span>a")
    quote_link_list = [
        "https://quotes.toscrape.com" + i["href"] for i in quote_link  # type:ignore
    ]

    if len(quote_text_list) > 0:
        text_list.extend(quote_text_list)
        author_list.extend(quote_author_list)
        infor_list.extend(quote_link_list)
        time.sleep(1)
    else:
        break

# print("text list", text_list)
# print("author list", author_list)
# print("infor list", infor_list)

# ? 데이터프레임으로 변경하기
import pandas as pd

df_quotes = pd.DataFrame(
    {"text": text_list, "author": author_list, "infor": infor_list}
)
print(df_quotes)
#                                                  text              author                                              infor
# 0   “The world as we have created it is a process ...     Albert Einstein  https://quotes.toscrape.com/author/Albert-Eins...
# 1   “It is our choices, Harry, that show what we t...        J.K. Rowling     https://quotes.toscrape.com/author/J-K-Rowling
# 2   “There are only two ways to live your life. On...     Albert Einstein  https://quotes.toscrape.com/author/Albert-Eins...
# 3   “The person, be it gentleman or lady, who has ...         Jane Austen     https://quotes.toscrape.com/author/Jane-Austen
# 4   “Imperfection is beauty, madness is genius and...      Marilyn Monroe  https://quotes.toscrape.com/author/Marilyn-Monroe
# ..                                                ...                 ...                                                ...
# 95  “You never really understand a person until yo...          Harper Lee      https://quotes.toscrape.com/author/Harper-Lee
# 96  “You have to write the book that wants to be w...   Madeleine L'Engle  https://quotes.toscrape.com/author/Madeleine-L...
# 97  “Never tell the truth to people who are not wo...          Mark Twain      https://quotes.toscrape.com/author/Mark-Twain
# 98        “A person's a person, no matter how small.”           Dr. Seuss        https://quotes.toscrape.com/author/Dr-Seuss
# 99  “... a mind needs books as a sword needs a whe...  George R.R. Martin  https://quotes.toscrape.com/author/George-R-R-...

# [100 rows x 3 columns]
