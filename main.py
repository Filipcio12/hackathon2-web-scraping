from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import requests
import json
import re


def main():
    read_uni_site()


def read_gov_api():
    response_API = requests.get(
        "https://api.dane.gov.pl/media/resources/20150312/lodzkie.xls")
    data = response_API.text
    parse_json = json.loads(data)
    print(parse_json)


def read_gov_site():
    html = urlopen("https://www.gov.pl/web/edukacja-i-nauka/wykaz-uczelni-publicznych-nadzorowanych-przez-ministra-wlasciwego-ds-szkolnictwa-wyzszego-publiczne-uczelnie-akademickie")
    bs = BeautifulSoup(html.read(), 'html.parser')
    unis = bs.find_all("a", {"class": "js-external-link"})
    links = list()
    for uni in unis:
        links.append(uni.get("href"))
    print(links)


def read_uni_site():
    # Have to find subpage with majors
    link = "https://www.uj.edu.pl/"
    html = urlopen(link)
    bs = BeautifulSoup(html.read(), "html.parser")
    subpages = bs.find_all("a")
    links = list()
    for subpage in subpages:
        links.append(subpage.get("href"))
    for link in links:
        match_obj = None
        try:
            match_obj = re.search("studia", link)
        except:
            pass
        if match_obj is not None:
            print(link)


if __name__ == "__main__":
    main()
