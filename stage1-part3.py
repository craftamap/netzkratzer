""" This script shows the functionalities of the beautifulsoup library
"""


import requests
import furl
from bs4 import BeautifulSoup


def main():
    url = furl.furl("https://projects.siegelfabian.de/webscraping/users/")

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "lxml")

    print(soup)
    print(soup.header)
    print(soup.header.text)
    print(soup.header.name)

    print()

    print(soup.select_one("a.profile"))
    print(soup.select_one("a")["href"])

    list_items = soup.select("ul li")  # or .find_all()
    print(list_items)
    for list_item in list_items:
        link = list_item.select_one(".profile")["href"]
        name = list_item.select_one(".name").text
        print(name, link)


if __name__ == "__main__":
    main()
