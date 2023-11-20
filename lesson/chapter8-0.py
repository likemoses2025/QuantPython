import requests as rq

#! 크롤링

url = "https://quotes.toscrape.com/"
quote = rq.get(url)

print(quote)  # <Response [200] >
print(quote.content[:1000])
# b'<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<title>Quotes to Scrape</title>\n    <link rel="stylesheet" href="/static/bootstrap.min.css">\n    <link rel="stylesheet" href="/static/main.css">\n</head>\n<body>\n    <div class="container">\n        <div class="row header-box">\n            <div class="col-md-8">\n                <h1>\n                    <a href="/" style="text-decoration: none">Quotes to Scrape</a>\n                </h1>\n            </div>\n            <div class="col-md-4">\n                <p>\n                \n                    <a href="/login">Login</a>\n                \n                </p>\n            </div>\n        </div>\n    \n\n<div class="row">\n    <div class="col-md-8">\n\n    <div class="quote" itemscope itemtype="http://schema.org/CreativeWork">\n        <span class="text" itemprop="text">\xe2\x80\x9cThe world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.\xe2\x80\x9d</span>\n        <span>by <small class="author" it'

# @ BeautifulSoup() 함수를 이용하여 HTML 객체에 접근
from bs4 import BeautifulSoup

quote_html = BeautifulSoup(quote.content, "html.parser")
print(quote_html.head)
# <head>
# <meta charset="utf-8"/>
# <title>Quotes to Scrape</title>
# <link href="/static/bootstrap.min.css" rel="stylesheet"/>
# <link href="/static/main.css" rel="stylesheet"/>
# </head>

# @ find 함수
quote_div = quote_html.find_all("div", class_="quote")
print(quote_div[0])
# <div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
# <span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>
# <span>by <small class="author" itemprop="author">Albert Einstein</small>
# <a href="/author/Albert-Einstein">(about)</a>
# </span>
# <div class="tags">
#             Tags:
#             <meta class="keywords" content="change,deep-thoughts,thinking,world" itemprop="keywords"/>
# <a class="tag" href="/tag/change/page/1/">change</a>
# <a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>
# <a class="tag" href="/tag/thinking/page/1/">thinking</a>
# <a class="tag" href="/tag/world/page/1/">world</a>
# </div>
# </div>
quote_span = quote_div[0].find_all("span", class_="text")
print(quote_span)
# [<span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>]

print(quote_span[0].text)
# “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”

quote_div = quote_html.find_all("div", class_="quote")

[print(i.find_all("span", class_="text")[0].text) for i in quote_div]
# “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
# “It is our choices, Harry, that show what we truly are, far more than our abilities.”
# “There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”
# “The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”
# “Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”
# “Try not to become a man of success. Rather become a man of value.”
# “It is better to be hated for what you are than to be loved for what you are not.”
# “I have not failed. I've just found 10,000 ways that won't work.”
# “A woman is like a tea bag; you never know how strong it is until it's in hot water.”
# “A day without sunshine is like, you know, night.”


#! select() 함수 크롤링

# @ 명언 크롤링
quote_text = quote_html.select("div.quote > span.text")
print(quote_text)
# [<span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>, <span class="text" itemprop="text">“It is our choices, Harry, that show what we truly are, far more than our abilities.”</span>, <span class="text" itemprop="text">“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”</span>, <span class="text" itemprop="text">“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”</span>, <span class="text" itemprop="text">“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”</span>, <span class="text" itemprop="text">“Try not to become a man of success. Rather become a man of value.”</span>, <span class="text" itemprop="text">“It is better to be hated for what you are than to be loved for what you are not.”</span>, <span class="text" itemprop="text">“I have not failed. I've just found 10,000 ways that won't work.”</span>, <span class="text" itemprop="text">“A woman is like a tea bag; you never know how strong it is until it's in hot water.”</span>, <span class="text" itemprop="text">“A day without sunshine is like, you know, night.”</span>]

quote_text_list = [i.text for i in quote_text]
print(quote_text_list)
# [
#     "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”",
#     "“It is our choices, Harry, that show what we truly are, far more than our abilities.”",
#     "“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”",
#     "“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”",
#     "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”",
#     "“Try not to become a man of success. Rather become a man of value.”",
#     "“It is better to be hated for what you are than to be loved for what you are not.”",
#     "“I have not failed. I've just found 10,000 ways that won't work.”",
#     "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”",
#     "“A day without sunshine is like, you know, night.”",
# ]

# @ 명언 저자 크롤링
quote_author = quote_html.select("div.quote> span> small.author")
print(quote_author)
# [<small class="author" itemprop="author">Albert Einstein</small>, <small class="author" itemprop="author">J.K. Rowling</small>, <small class="author" itemprop="author">Albert Einstein</small>, <small class="author" itemprop="author">Jane Austen</small>, <small class="author" itemprop="author">Marilyn Monroe</small>, <small class="author" itemprop="author">Albert Einstein</small>, <small class="author" itemprop="author">André Gide</small>, <small class="author" itemprop="author">Thomas A. Edison</small>, <small class="author" itemprop="author">Eleanor Roosevelt</small>, <small class="author" itemprop="author">Steve Martin</small>]
quote_author_list = [i.text for i in quote_author]
print(quote_author_list)
# [
#     "Albert Einstein",
#     "J.K. Rowling",
#     "Albert Einstein",
#     "Jane Austen",
#     "Marilyn Monroe",
#     "Albert Einstein",
#     "André Gide",
#     "Thomas A. Edison",
#     "Eleanor Roosevelt",
#     "Steve Martin",
# ]

# @ 저자에 대한 정보 주소링크 크롤링
quote_author_link = quote_html.select("div.quote>span>a")
print(quote_author_link)
# [<a href="/author/Albert-Einstein">(about)</a>, <a href="/author/J-K-Rowling">(about)</a>, <a href="/author/Albert-Einstein">(about)</a>, <a href="/author/Jane-Austen">(about)</a>, <a href="/author/Marilyn-Monroe">(about)</a>, <a href="/author/Albert-Einstein">(about)</a>, <a href="/author/Andre-Gide">(about)</a>, <a href="/author/Thomas-A-Edison">(about)</a>, <a href="/author/Eleanor-Roosevelt">(about)</a>, <a href="/author/Steve-Martin">(about)</a>]
print(quote_author_link[0]["href"])
# /author/Albert-Einstein
quote_author_link_list = [i["href"] for i in quote_author_link]
print(quote_author_link_list)
# [
#     "/author/Albert-Einstein",
#     "/author/J-K-Rowling",
#     "/author/Albert-Einstein",
#     "/author/Jane-Austen",
#     "/author/Marilyn-Monroe",
#     "/author/Albert-Einstein",
#     "/author/Andre-Gide",
#     "/author/Thomas-A-Edison",
#     "/author/Eleanor-Roosevelt",
#     "/author/Steve-Martin",
# ]

# ? 완전한 주소 만들기
complete_link = ["https://quotes.toscrape.com" + i["href"] for i in quote_author_link]  # type: ignore
print(complete_link)
# [
#     "https://quotes.toscrape.com/author/Albert-Einstein",
#     "https://quotes.toscrape.com/author/J-K-Rowling",
#     "https://quotes.toscrape.com/author/Albert-Einstein",
#     "https://quotes.toscrape.com/author/Jane-Austen",
#     "https://quotes.toscrape.com/author/Marilyn-Monroe",
#     "https://quotes.toscrape.com/author/Albert-Einstein",
#     "https://quotes.toscrape.com/author/Andre-Gide",
#     "https://quotes.toscrape.com/author/Thomas-A-Edison",
#     "https://quotes.toscrape.com/author/Eleanor-Roosevelt",
#     "https://quotes.toscrape.com/author/Steve-Martin",
# ]
