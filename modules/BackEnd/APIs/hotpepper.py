# -*- coding: utf-8 -*-
import os
import requests


class HotPepperGourmetAPI(object):

    BASE_URL = 'http://webservice.recruit.co.jp/hotpepper/{0}/v1/'

    def __init__(self, api_key=None):
        self.__api_key = os.environ.get('HOTPEPPER_API_KEY', api_key)

    def __search(self, api_type, **kwargs):
        params = {'key': self.__api_key, 'format': 'json'}
        params.update(kwargs)
        url = self.BASE_URL.format(api_type)
        response = requests.get(url, params).json()

        return response

    def search_restaurant(self, **kwargs):
        # 指定するリクエストパラメータ
        # key, small_area, food, budget
        response = self.__search('gourmet', **kwargs)

    def area_name2area_code(self, **kwargs):
        # keyword 完全一致を優先させる
        response = self.__search('small_area', **kwargs)
        small_area_code = response['small_area']['code']

        return small_area_code

    def food_name2food_code(self, **kwargs):
        # keyword 完全一致を優先させる
        response = self.__search('food', **kwargs)
        food_code = response['food']['code']

        return food_code

    def search_budget(self, **kwargs):
        response = self.__search('budget', **kwargs)

    # エリア名、料理名、予算額を与えると、それぞれ対応するコードに変換するメソッドが必要？
    # エリア名に関してはsmall_areaAPIに名前を与えるとコードを返してくれる
    # 料理名も同様
    # 予算に関してはなさそうなので、対応させるロジックを組む必要がある


if __name__ == '__main__':
    api = HotPepperGourmetAPI()
    api.search_restaurant()