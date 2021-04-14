# -*- coding: utf-8 -*-
from json import loads as json_loads

import requests


class HttpClient():
    headers = {'Accept': 'application/json'}

    def get(self, url):
        response = requests.get(f'{self.api_url}/{url}', headers=self.headers)
        return json_loads(response.text)


    def __init__(self, api_url):
        self.api_url = api_url
