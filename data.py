import requests
from bs4 import BeautifulSoup
import pandas as pd

all_quotes = []
page = 1
while True:
    url = "http://quotes.toscrape.com/page/{}/".format(page)

#get request
    response = requests.get(url)
#parse
    soup = BeautifulSoup(response.content,"html.parser")
# find all quote

    quotes = soup.find_all("div", class_="quote")

    if not quotes:
     break



    for quote in quotes:
     text = quote.find("span", class_="text").text
     author = quote.find("small", class_="author").text
     all_quotes.append({"text": text, "author": author})

    page += 1

df = pd.DataFrame(all_quotes )


df.to_csv("quotes.csv", index = False)
print("complete scraping,all quotes saved")