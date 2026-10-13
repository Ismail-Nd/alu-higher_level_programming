import requests
from bs4 import BeautifulSoup

url = "https://www.rottentomatoes.com/m/black_panther"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)