from bs4 import BeautifulSoup
import requests
import nltk

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
#CITE: TA Justin Marler. Use this in requests.get to scrape pages that otherwise block scrapers.
#EX:   requests.get(url, headers=HEADERS).text

### later any time you use requests.get:
# source_code = requests.get(url, headers=HEADERS).text

url = "https://www.imdb.com/search/title/?groups=top_1000"
source_code = requests.get(url, headers=HEADERS).text
parsed_code = BeautifulSoup(source_code, "html.parser")

# bad_guess = parsed_code.find("div", class_="lister-item-content")
# print(bad_guess)

# good_guess = parsed_code.find_all("h3", class_="lister-item-header")
# for entry in good_guess:
#     print(entry.text)

#-----------------------question 6------------------------------------------------
def search_movie(parsed_code, movie_title):
    links = []
    movie_text = []
    good_guess = parsed_code.find_all("h3", class_="lister-item-header")
    for entry in good_guess:
        movie_text.append(entry.text)
    for entry in good_guess:
        for a in entry("a", href = True):
            links.append("https://www.imdb.com"+ a["href"])
    for film in movie_text:
        if movie_title in film:
            location= movie_text.index(film)
    print(movie_text[location])     
    print("This is the link to the IMDB web page:", links[location])
    detail_url = links[location]
    return detail_url
#----------------------question 7-------------------------------------------

def cast_list(detail_url, movie_title):
    cast_url = detail_url[:-15]+"fullcredits?ref_=tt_cl_sm"
    film_source = requests.get(cast_url, headers=HEADERS).text
    film_parsed = BeautifulSoup(film_source, "html.parser")
    cast = film_parsed.find_all("td")
    cast_list = []
    clean_character_list = []
    for actor in cast:
        for a in actor("a", href = True):
            name = nltk.word_tokenize(a.text)
            name2 = " ".join(name)
            clean_character_list.append(name2)
            
            
            
#     print(clean_character_list[3:])
    
    final_actors = []
    final_characters = []
    for entry in range(len(clean_character_list)):
        if entry%3==0:
            final_actors.append(clean_character_list[entry])
        elif entry%3==1:
            final_characters.append(clean_character_list[entry])
    print(final_actors)
    print(final_characters)
        
    

        
    characters = film_parsed.find_all("td", class_= "character")
    character_list = []
    new = []
    for character in characters:
        name = nltk.word_tokenize(character.text)
        name2 = " ".join(name)
        character_list.append(name2)
#     print(character_list)
   
#         character_list.append(character_name)

    
# 
    

def main():
    movie_title = input("What movie?")
    detail_url = search_movie(parsed_code, movie_title)
    cast_list(detail_url, movie_title)
main()