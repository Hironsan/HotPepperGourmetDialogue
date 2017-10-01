# -*- coding: utf-8 -*-
import unittest

from dialogue_system.language_understanding.attribute_extraction.rule_based_extractor import RuleBasedAttributeExtractor


class AttributeExtractorTest(unittest.TestCase):

    def setUp(self):
        self.extractor = RuleBasedAttributeExtractor()

    def tearDown(self):
        pass

    def test_extract(self):
        attribute = self.extractor.extract(text='ラーメンを食べたい')
        self.assertEqual(attribute, {'LOCATION': '', 'GENRE': 'ラーメン', 'MAXIMUM_AMOUNT': ''})
        attribute = self.extractor.extract(text='西新宿のあたり')
        self.assertEqual(attribute, {'LOCATION': '西新宿', 'GENRE': '', 'MAXIMUM_AMOUNT': ''})
        attribute = self.extractor.extract(text='1000円以下で')
        self.assertEqual(attribute, {'LOCATION': '', 'GENRE': '', 'MAXIMUM_AMOUNT': '1000'})