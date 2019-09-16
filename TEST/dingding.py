import json
import random
import time
import os
# import pymongo
import requests
from urllib import request
from bs4 import BeautifulSoup
from lxml import etree


def main():
    url="https://oapi.dingtalk.com/robot/send?access_token=token"

    header = {
         "Content-Type": "application/json"
    }

    data = {
        "msgtype": "text",
        "text": {
            "content": "我就是我, 是不一样的烟火"
        },
        "at": {
            "atMobiles": [
                "156xxxx8827",
                "189xxxx8325"
            ],
            "isAtAll": False
        }
    }


    sendData = json.dumps(data)
    html = requests.post(url, headers=header, data=sendData).text
    print(html)

if __name__ == '__main__':
    main()
