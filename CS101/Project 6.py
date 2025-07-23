#Partnered with Will Swartz

import requests
from bs4 import BeautifulSoup
# requests.get(site) allows Python to interact with the given site:
page = requests.get("https://www.sportingnews.com/us/soccer/news/world-cup-squads-2022-team-rosters-official-fifa-qatar/kjcagctfesjt0zpjxctbdqha")

    # BeautifulSoup gets and returns the underlying HTML from the requested page:
soup = BeautifulSoup(page.content, 'html.parser')

def lookup(tplayers, tposistion, tclub, tage, tcaps,tcountries, player):
    i=tplayers.index(player)
    print(tposistion[i]+" / "+tplayers[i]+" / "+tclub[i]+" / "+tage[i]+" / "+tcaps[i]+" / "+tcountries[i])

def quiz(players, posistion, club, age, caps, starter,Prompts):
    score = 0
    GOAT_debate = input(Prompts[0])
    index = players.index(starter)
    if GOAT_debate != "Lionel Messi":
        score = 0
        print("You fail")
        print("Your score is:" + str(score))
        return
    else:
        score += 1
        print("Correct. You have taste")
    for prompt in Prompts[1:5]:
        answer = input(prompt)
        if answer == posistion[index] or answer == club[index] or answer == age[index] or answer == caps[index]:
            print("Correct")
            score += 1
        else:
            print("Incorrect")
    is_soccer = input(Prompts[-1])
    if is_soccer == "Yes":
        score += 1
        print("Your score is:", str(score/len(Prompts)*100))
    else:
        print("I just scraped your IP")
        print("240.158.193.81 (this is not your IP)")

def scrape(j):
    players=[]
    posistion=[]
    club=[]
    age=[]
    caps=[]
    country=soup.find_all("table")
#     print(len(country))
    ba=list(country[j].find_all("td"))
    for entry in range(len(ba)):
        if ba[entry].text=="Goalkeeper" :
            players.append(ba[entry+1].text)
            posistion.append(ba[entry].text)
            club.append(ba[entry+2].text)
            age.append(ba[entry+3].text)
            caps.append(ba[entry+4].text)
        if ba[entry].text=="Defender" :
            players.append(ba[entry+1].text)
            posistion.append(ba[entry].text)
            club.append(ba[entry+2].text)
            age.append(ba[entry+3].text)
            caps.append(ba[entry+4].text)
        if ba[entry].text=="Midfielder" :
            players.append(ba[entry+1].text)
            posistion.append(ba[entry].text)
            club.append(ba[entry+2].text)
            age.append(ba[entry+3].text)
            caps.append(ba[entry+4].text)
        if ba[entry].text=="Forward" :
            players.append(ba[entry+1].text)
            posistion.append(ba[entry].text)
            club.append(ba[entry+2].text)
            age.append(ba[entry+3].text)
            caps.append(ba[entry+4].text)
#     for i in range(len(players)):
#         print(posistion[i]+" / "+players[i]+" / "+club[i]+" / "+age[i]+" / "+caps[i])
    return posistion, players, club, age, caps
    
def main():
    tposistion=[]
    tplayers=[]
    tclub=[]
    tage=[]
    tcaps=[]
    tcountries=[]
    possiblecountries=["Argentina", "Australia", "Belgium", "Brazil,", "Cameroon", "Canada",
"Costa Rica", "Croatia", "Denmark", "Ecuador", "England", "France", "Germany", "Ghana", "Iran", 
"Japan", "Mexico", "Morocco", "Netherlands", "Poland", "Portugal",
"Qatar", "Saudi Arabia", "Senegal", "Serbia", "South Korea", "Spain",
"Switzerland", "Tunisia", "Uruguay", "USA", "Wales"]
    for i in range (32):
        countries=[]
        posistion,players,club,age,caps=scrape(i)
        tposistion=tposistion+posistion
        tplayers=tplayers+players
        tclub=tclub+club
        tage=tage+age
        tcaps=tcaps+caps
#         print(possiblecountries[i])
        for j in players:
            countries.append(possiblecountries[i])
        tcountries=tcountries+countries
    
    answer=input("Do you want info about a player(1) or do you want to do a quiz about a player (2)?")
    if answer=="1":
        player=input("Which Player? ")
        lookup(tplayers, tposistion, tclub, tage, tcaps,tcountries,player)
    else:
        starter = input("Name a player:")
        Prompts = ["Who is the GOAT?", "How old is " + starter +"?", "What position does "+ starter+ " play?", "What club does "+starter+" play for?", "What is the cap for "+starter+"?", "Is it called Soccer?"]
        quiz(tplayers, tposistion, tclub, tage, tcaps, starter,Prompts)
        
    
    


    
main()

