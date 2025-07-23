# Install beautifulsoup4 (bs4) and requests using Tools / Manage Packages

import requests
from bs4 import BeautifulSoup

def main():
    # requests.get(site) allows Python to interact with the given site:
    page = requests.get("https://www.sportingnews.com/us/soccer/news/world-cup-squads-2022-team-rosters-official-fifa-qatar/kjcagctfesjt0zpjxctbdqha")

    # BeautifulSoup gets and returns the underlying HTML from the requested page:
    soup = BeautifulSoup(page.content, 'html.parser')
    argentina_soccer = soup.find("table")
    ba=list(argentina_soccer.find_all("td"))
    names=[]
    for entry in range(len(ba)):
        if ba[entry].text=="Goalkeeper" :
            names.append(ba[entry+1].text)
    for i in names:
        print(i)


    
main()