import requests
from bs4 import BeautifulSoup

url = "https://www.rottentomatoes.com/browse/movies_at_home/sort:popular"

response = requests.get(url, timeout=30)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

cards = soup.select("media-info-tile")

# card = cards[0]

for card in cards[:5]:

    title = card.select_one(
        'rt-text[data-qa="discovery-media-list-item-title"]'
    )

    poster = card.select_one(
        'poster-tile rt-img[slot="thumbnail"]'
    )

    score = card.select_one(
        'rt-text[slot="criticsScore"]'
    )

    print("Title:", title.get_text(strip=True))
    print("Image:", poster.get("src"))
    print("Critics:", score.get_text(strip=True))
    print("-" * 50)

# print(card.prettify())

# print("Cards found:", len(cards))