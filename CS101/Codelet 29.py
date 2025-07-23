# Install beautifulsoup4 (bs4) and requests using Tools / Manage Packages

import requests
from bs4 import BeautifulSoup
import nltk


def main():
    url = "https://www.thehugoawards.org/hugo-history/2022-hugo-awards/"
    source_code = requests.get(url).text
    parsed_code = BeautifulSoup(source_code, "html.parser")
    winners_code = parsed_code.find_all("li", class_="winner")
    for i in range(5):
        winner = winners_code[i]
        print(winner.text)
 
    

    
main()
