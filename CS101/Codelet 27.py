# Install beautifulsoup4 (bs4) and requests using Tools / Manage Packages

import requests
from bs4 import BeautifulSoup

def main():
    # requests.get(site) allows Python to interact with the given site:
    page = requests.get("https://web.ics.purdue.edu/~gchopra/class/public/pages/webdesign/05_simple.html")

    # BeautifulSoup gets and returns the underlying HTML from the requested page:
    soup = BeautifulSoup(page.content, 'html.parser')
    for a in soup.find_all('a', href = True):
        print(a["href"])

main()