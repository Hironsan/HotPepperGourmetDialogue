# -*- coding: utf-8 -*-
import os

import requests


class AreaNotFoundException(BaseException):
    pass


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

    def search_restaurant(self, area, food, budget):
        # 指定するリクエストパラメータ
        # key, small_area, food, budget
        area_code = self.area_name2area_code(keyword=area)
        food_code = self.food_name2food_code(keyword=food)
        budget_code = self.to_budget_code(budget)
        response = self.__search('gourmet', food=food_code, budget=budget_code, small_area=area_code)
        if int(response['results']['results_returned']) >= 1:
            return response['results']['shop'][0]
        else:
            return []

    def area_name2area_code(self, **kwargs):
        # keyword 完全一致を優先させる
        response = self.__search('small_area', **kwargs)
        small_areas = response['results']['small_area']
        try:
            area_code = small_areas[0]['code']
        except IndexError:
            raise AreaNotFoundException
        return area_code

    def food_name2food_code(self, **kwargs):
        # keyword 完全一致を優先させる
        response = self.__search('food', **kwargs)
        foods = response['results']['food']
        food_code = foods[0]['code']

        return food_code

    def to_budget_code(self, user_budget):
        response = self.__search('budget')
        for budget in response['results']['budget']:
            name, code = budget['name'], budget['code']
            name = name.replace('円', '')
            if name.startswith('～'):
                upper = name.replace('～', '')
                if int(user_budget) <= int(upper):
                    return code
            elif name.endswith('～'):
                lower = name.replace('～', '')
                if int(user_budget) >= int(lower):
                    return code
            else:
                _, upper = name.split('～')
                if int(user_budget) <= int(upper):
                    return code

    def search_food(self, **kwargs):
        # keyword 完全一致を優先させる
        response = self.__search('food', **kwargs)
        for el in response['results']['food']:
            print(el['name'])


if __name__ == '__main__':
    api = HotPepperGourmetAPI()
    api.search_food()
