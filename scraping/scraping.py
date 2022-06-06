import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

print("type what you want to search")
subject = input()
links_title = []
description_title = []
Prix = []
Links = []
Products = []
num_page = 1
while True:
    resultat = requests.get(
        f"https://www.flipkart.com/search?q={subject}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={num_page}")
    resultats = requests.get(
        f"https://www.flipkart.com/search?q={subject}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=2")

    src = resultat.content
    srcs = resultats.content
    soup = BeautifulSoup(src, "lxml")
    soups = BeautifulSoup(srcs, "lxml")
    page_fin = soups.find("div", {"class": "_2MImiq"}).span.text.split()
    # print(int(page_fin[3]))
    if num_page > (int(page_fin[3])):
        print("page endeed")
        break
    # print(soup)
    links = soup.find_all("div", {"class": "_2kHMtA"})

    for i in range(len(links)):
        links_title.append(links[i].find("a").attrs['href'])

    num_page += 1

    print("page switched")
for i in range(len(links_title)):

    result = requests.get(f"https://www.flipkart.com{links_title[i]}")

    s = result.content
    sp = BeautifulSoup(s, "lxml")

    try:

        title = sp.find("span", {"class": "B_NuCI"}).text
        prix = sp.find("div", {"class": "_30jeq3 _16Jk6d"}).text
        table1 = sp.find('table', class_='_14cfVK')
        tr = table1.find_all("tr")



    except:
        title = "title not existe"
        prix = "prix not existe"

        # offres =[]
    product = {
        'title': title,
        'price': prix,
        'link': links_title[i]
    }
    print(product)
    description_title.append(title)
    Prix.append(prix)
    Links.append(links_title[i])
    Products.append(product)
pricesdf = pd.DataFrame(Products)
pricesdf.to_csv('produit.csv', index=False)

