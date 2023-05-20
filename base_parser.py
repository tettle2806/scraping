import requests
from bs4 import BeautifulSoup
import json


class BaseParser:
    def __init__(self):
        self.url = 'https://www.creditasia.uz/'
        self.host = 'https://www.creditasia.uz'


    def get_html(self, url=None):
        if url:
            return requests.get(url).text
        else:
            return requests.get(self.url).text

    def get_soup(self, html):
        return BeautifulSoup(html, 'html.parser')

    # Это метод, который не зависит от объекта класса
    # Метод можно вызывать из чертежа класса
    @staticmethod
    def save_json(filename, data):
        with open(f'{filename}.json', mode='w', encoding='UTF-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

