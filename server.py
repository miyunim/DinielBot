#-*- coding: utf-8 -*-
import requests
import xmltodict, json
from flask import Flask
app = Flask(__name__)

client_id = ""
client_secret = ""
IMAGE_SEARCH_URL = 'https://openapi.naver.com/v1/search/image.json'

def search():
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret
    }

    payload = {
        'sort': 'date',
        'query': '강다니엘',
    }

    response = requests.get(IMAGE_SEARCH_URL, params=payload, headers=headers)
    data = response.json()
    return map(lambda x: x['link'], data['items'])


@app.route("/")
def hello():
    imgs = search()

    html = ''
    for img in imgs:
        print(img)
        html += '<img src="' + img + '" /><br>'

    return html

if __name__ == "__main__":
    app.run()
