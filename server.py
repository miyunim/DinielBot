#-*- coding: utf-8 -*-

import requests
from flask import Flask
app = Flask(__name__)

client_id = ""
client_secret = ""
IMAGE_SEARCH_URL = 'https://openapi.naver.com/v1/search/image.xml'

def search():
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret
    }

    payload = {
        'query': '강다니엘',
    }

    r = requests.get(IMAGE_SEARCH_URL, params=payload, headers=headers)
    print(r.text)
    

@app.route("/")
def hello():
    search()
    return "Hello World!"

if __name__ == "__main__":
    app.run()
