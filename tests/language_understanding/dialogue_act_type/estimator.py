# -*- coding: utf-8 -*-
import unittest

from dialogue_system.language_understanding.attribute_extraction.rule_based_extractor import RuleBasedAttributeExtractor
from dialogue_system.language_understanding.dialogue_act_type.rule_based_estimator import RuleBasedDialogueActTypeEstimator


class AttributeExtractorTest(unittest.TestCase):

    def setUp(self):
        self.extractor = RuleBasedAttributeExtractor()
        self.estimator = RuleBasedDialogueActTypeEstimator()

    def tearDown(self):
        pass

    def test_extract(self):
        attribute = self.extractor.extract(text='ラーメンを食べたい')
        act_type = self.estimator.estimate(attribute)
        self.assertEqual(act_type, 'INFORM_GENRE')
        attribute = self.extractor.extract(text='西新宿のあたり')
        act_type = self.estimator.estimate(attribute)
        self.assertEqual(act_type, 'INFORM_LOC')
        attribute = self.extractor.extract(text='1000円以下で')
        act_type = self.estimator.estimate(attribute)
        self.assertEqual(act_type, 'INFORM_MONEY')
        attribute = self.extractor.extract(text='こんにちは')
        act_type = self.estimator.estimate(attribute)
        self.assertEqual(act_type, 'OTHER')