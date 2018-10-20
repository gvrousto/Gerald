import requests, os, json, scrapy
from lxml import html
from bs4 import BeautifulSoup
script_dir = os.path.dirname(__file__)

base_url = "https://www.instagram.com/"

def scrape_account (account_tag):
    url = base_url + account_tag
    page_request = requests.get(url)
    soup = BeautifulSoup(page_request.text, 'html.parser')
    body = soup.find('body')
    script_tag = body.find('script')
    raw_string = script_tag.text.strip().replace('window._sharedData =', '').replace(';', '')

    data = json.loads(raw_string)
    tree = html.fromstring(page_request.content)
    print(tree)
    user = data['entry_data']['ProfilePage'][0]['graphql']['user']
    user_images = user['edge_owner_to_timeline_media']['edges']
    for i in range(len(user_images)):
        user_images[i] = user_images[i]['node']['thumbnail_src']
    return user_images
