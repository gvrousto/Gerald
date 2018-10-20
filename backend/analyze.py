from clarifai.rest import ClarifaiApp
import json

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
    boringConcepts = ["man", "woman", "boy", "girl", "person", "people", "adult", "portrait", "two", "one", "wear", "child", "group", "three", "facial expression"]
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

def topFive(aggregateList):
    return aggregateList[0].key + " " + aggregateList[1].key + " " + aggregateList[2].key + " " + aggregateList[3].key + " " + aggregateList[4].key

if __name__ == "__main__":
    urls = {"https://scontent-ort2-1.cdninstagram.com/vp/0cce14df4cfe0ee40fe9c987bdf38fdd/5C5505D6/t51.2885-15/sh0.08/e35/s640x640/42068899_243218789687751_2248200095345990823_n.jpg","https://scontent-ort2-1.cdninstagram.com/vp/4d10d117923bbb3b2b68b7512cf681ba/5C5CB98C/t51.2885-15/e35/s480x480/43914177_2228428930701824_3145312509417136910_n.jpg", "https://scontent-ort2-1.cdninstagram.com/vp/982431eea19c52fec85c27ad7cafb348/5C66A636/t51.2885-15/sh0.08/e35/s640x640/43914177_2228428930701824_3145312509417136910_n.jpg"}
    aggregateList = getAggregateKeyValue(urls)
    print(topFive(aggregateList))
