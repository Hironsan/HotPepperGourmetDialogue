# -*- coding: utf-8 -*-
import os
import requests


class HotPepperGourmetAPI(object):

    BASE_URL = 'http://webservice.recruit.co.jp/hotpepper/{0}/v1/'

    def __init__(self, api_key=None):
        self.__api_key = os.environ.get('HOTPEPPER_API_KEY', api_key)

    def search_restaurant(self, **kwargs):
        # 指定するリクエストパラメータ
        # key, small_area, food, budget
        params = {'key': self.__api_key}
        params.update(kwargs)
        url = self.BASE_URL.format('gourmet')
        try:
            response = requests.get(url, params).json()
        except Exception:
            print('Error has occured.')
            raise

        return response

    def search_area_name(self):
        pass

    def search_food_name(self):
        pass

    def search_budget(self):
        pass

    # エリア名、料理名、予算額を与えると、それぞれ対応するコードに変換するメソッドが必要？
    # エリア名に関してはsmall_areaAPIに名前を与えるとコードを返してくれる
    # 料理名も同様
    # 予算に関してはなさそうなので、対応させるロジックを組む必要がある


if __name__ == '__main__':
    api = HotPepperGourmetAPI()
    api.search_restaurant()