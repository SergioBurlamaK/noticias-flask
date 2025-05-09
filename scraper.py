import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_headlines():
    url = 'https://g1.globo.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = []

    for item in soup.select('a.feed-post-link'):
        title = item.get_text().strip()
        link = item.get('href')
        if link:
            link = urljoin(url, link)
            headlines.append({'title': title, 'link': link})

    return headlines
