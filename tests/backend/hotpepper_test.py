# -*- coding: utf-8 -*-
import unittest

from dialogue_system.backend.apis.hotpepper import HotPepperGourmetAPI, AreaNotFoundException


class HotPepperAPITest(unittest.TestCase):

    def setUp(self):
        self.api = HotPepperGourmetAPI()

    def tearDown(self):
        pass

    def test_areaname_to_areacode(self):
        area_code = self.api.area_name2area_code(keyword='西新宿')
        self.assertEqual(area_code, 'XA02')
        try:
            area_code = self.api.area_name2area_code(keyword='バビロニア')
        except AreaNotFoundException:
            self.assertEqual(True, True)

    def test_foodname_to_foodcode(self):
        food_code = self.api.food_name2food_code(keyword='ラーメン')
        self.assertEqual(food_code, 'R038')
        #food_code = self.api.food_name2food_code(keyword='テラワロス')

    def test_search_budget(self):
        budget_code = self.api.to_budget_code('2000')
        self.assertEqual(budget_code, 'B001')
        budget_code = self.api.to_budget_code('3000')
        self.assertEqual(budget_code, 'B002')
        budget_code = self.api.to_budget_code('4000')
        self.assertEqual(budget_code, 'B003')
        budget_code = self.api.to_budget_code('5000')
        self.assertEqual(budget_code, 'B008')
        budget_code = self.api.to_budget_code('7000')
        self.assertEqual(budget_code, 'B004')
        budget_code = self.api.to_budget_code('10000')
        self.assertEqual(budget_code, 'B005')
        budget_code = self.api.to_budget_code('10001')
        self.assertEqual(budget_code, 'B006')

    def test_search_restaurant(self):
        response = self.api.search_restaurant(area='西新宿', food='ラーメン', budget='1000')
        import pprint
        pprint.pprint(response)