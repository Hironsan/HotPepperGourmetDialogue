# -*- coding: utf-8 -*-
import copy

from dialogue_system.language_understanding.attribute_extraction.rule_based_extractor import RuleBasedAttributeExtractor
from dialogue_system.language_understanding.dialogue_act_type.rule_based_estimator import RuleBasedDialogueActTypeEstimator


class RuleBasedLanguageUnderstanding(object):

    def __init__(self):
        self.__estimator = RuleBasedDialogueActTypeEstimator()
        self.__extractor = RuleBasedAttributeExtractor()

    def execute(self, sent):
        attribute = self.__extractor.extract(sent)
        act_type = self.__estimator.estimate(attribute)

        dialogue_act = {'user_act_type': act_type, 'utt': sent}
        attribute_cp = copy.copy(attribute)
        for k, v in attribute_cp.items():
            if v == '':
                del attribute[k]
        dialogue_act.update(attribute)

        return dialogue_act
