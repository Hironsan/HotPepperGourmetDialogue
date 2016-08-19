# -*- coding: utf-8 -*-
import unittest

from dialogue_system.language_understanding.attribute_extraction.extractor import AttributeExtractor
from dialogue_system.language_understanding.dialogue_act_type.predictor import RuleBasedDialogueActTypeEstimater


class AttributeExtractorTest(unittest.TestCase):

    def setUp(self):
        self.extractor = AttributeExtractor()
        self.estimator = RuleBasedDialogueActTypeEstimater()

    def tearDown(self):
        pass

    def test_extract(self):
        attribute = self.extractor.extract(text='ラーメンを食べたい')
        act_type = self.estimator.estimate(attribute)
        self.assertEqual(act_type, 'genre')
        attribute = self.extractor.extract(text='西新宿のあたり')
        act_type = self.estimator.estimate(attribute)
        self.assertEqual(act_type, 'location')
        attribute = self.extractor.extract(text='1000円以下で')
        act_type = self.estimator.estimate(attribute)
        self.assertEqual(act_type, 'maximum_amount')
        attribute = self.extractor.extract(text='こんにちは')
        act_type = self.estimator.estimate(attribute)
        self.assertEqual(act_type, 'other')