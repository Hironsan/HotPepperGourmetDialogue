# -*- coding: utf-8 -*-
import unittest
from modules.BackEnd.APIs.hotpepper import HotPepperGourmetAPI, AreaNotFoundException


class HotPepperAPITest(unittest.TestCase):

    def setUp(self):
        self.api = HotPepperGourmetAPI()

    def tearDown(self):
        pass

    def test_areaname_to_areacode(self):
        area_code = self.api.area_name2area_code(keyword='銀座')
        self.assertEqual(area_code, 'X005')
        try:
            area_code = self.api.area_name2area_code(keyword='バビロニア')
        except AreaNotFoundException:
            self.assertEqual(True, True)

    def test_foodname_to_foodcode(self):
        food_code = self.api.food_name2food_code(keyword='ラーメン')
        self.assertEqual(food_code, 'R038')
        food_code = self.api.food_name2food_code(keyword='テラワロス')
