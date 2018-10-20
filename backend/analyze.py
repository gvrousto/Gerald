
import requests, os, json, scrapy
from lxml import html
from bs4 import BeautifulSoup
from clarifai.rest import ClarifaiApp

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

    return topnum(getAggregateKeyValue(user_images), 10)

class Concept:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def addToValue(self, value):
        self.value = self.value + value

def getAggregateKeyValue(urls):
    app = ClarifaiApp(api_key='a2596d582f04477d847353f2c60e4ed1')
    model = app.models.get("general-v1.3")

    listConcepts = []
    listConceptNames = []
    boringConcepts = ["man", "woman", "boy", "girl", "person", "people", "adult", "portrait", "two", "one", "wear", "child", "group", "three", "facial expression", "no person"]
    for url in urls:
        result = model.predict_by_url(url=url, max_concepts=50)
        concepts = result['outputs'][0]['data']['concepts']
        for i in concepts:
            if i['name'] not in listConceptNames and i['name'] not in boringConcepts:
                c = Concept(i['name'], i['value'])
                listConcepts.append(c)
                listConceptNames.append(i['name'])
            else:
                counter = 0
                for concept in listConcepts:
                    if concept.key == i['name']:
                        concept.addToValue(float(i['value']))
                        counter = counter + 1
    sortedConcepts = sorted(listConcepts, key=lambda c: c.value, reverse=True)
    return sortedConcepts

def topnum(aggregateList, num):
    result = [];
    for akey in aggregateList:
        result.append(akey.key);
        if len(result) >= num:
            return result
    return result
