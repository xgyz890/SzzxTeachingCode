from bs4 import BeautifulSoup
import requests

url = "https://umggaming.com/leaderboards"

data = requests.get(url)

soup = BeautifulSoup(data.text, "html.parser")

leaderboard = soup.find("table", {"id": "leaderboard-table"})

tbody = leaderboard.find("tbody")

for tr in tbody.find_all("tr"):
    place = tr.find_all("td")[0].text.strip()
    username = tr.find_all("td")[1].find_all("a")[1].text.strip()
    xp = tr.find_all("td")[4].text.strip()
    print(place, username, xp)

