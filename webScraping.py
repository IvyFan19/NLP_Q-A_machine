import json
import wikipedia
import requests
from bs4 import BeautifulSoup

def webScraping():
    with open('Kg_API_data.json') as f:
        data = json.load(f)
        url_arr = []
        name_arr = []
        article_arr = ""
        i = 0
        for element in data['itemListElement']:
            print( str(i) + ' - ' +  element['result']['name'])
            # print(element['result']['detailedDescription']['url'])
            print(element['result']['detailedDescription']['articleBody'])

            one_article = element['result']['detailedDescription']['articleBody']
            one_url = element['result']['detailedDescription']['url']

            article_arr += one_article
            url_arr.append(str(element['result']['detailedDescription']['url']))
            name_arr.append(str(element['result']['name']))
            # print("#############")
            # print(wikipedia.summary(element['result']['name'], sentences=10))
            # response = requests.get(one_url)
            # soup = BeautifulSoup(response.content, 'html.parser')
            # page = response.json()
            # print(response)
            # title = soup.find('div', id="bodyContent").p
            # print(title)
            # print("#############")
            print(article_arr)

            i += 1
            
    # print(url_arr)
    # print(name_arr)

    



webScraping()