import requests
from bs4 import BeautifulSoup

def get_headlines():
    url = "https://www.npr.org/sections/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    headlines = []

    for tag in soup.find_all("h2", class_="title"):
        link_tag = tag.find("a")
        if link_tag:
            title = link_tag.get_text(strip=True)
            link = link_tag.get("href")
            headlines.append((title, link))

    return headlines
