import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

URL = "https://www.worldometers.info/coronavirus/country/us/"

# make an HTTP GET request to the URL
response = requests.get(URL)

# parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# find the table with the covid-19 data
table = soup.find("table", id="usa_table_countries_yesterday")

# extract the data from the table
data = []
rows = table.find_all("tr")
for row in rows:
    cols = row.find_all("td")
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

# select only the data from 2020
data = [row for row in data if row[0].split("/")[2] == "20"]

# create a line plot of the total number of cases over time
plt.plot([row[0] for row in data], [row[1] for row in data])

# add axis labels and a title
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.title("COVID-19 Cases in the US in 2020")

# show the plot
plt.show()
