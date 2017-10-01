# -*- coding: utf-8 -*-
import copy

from dialogue_system.language_understanding.attribute_extraction.rule_based_extractor import RuleBasedAttributeExtractor
from dialogue_system.language_understanding.dialogue_act_type.rule_based_estimator import RuleBasedDialogueActTypeEstimator

from dialogue_system.language_understanding.attribute_extraction.ml_based_extractor import MLBasedAttributeExtractor
from dialogue_system.language_understanding.dialogue_act_type.ml_based_estimator import MLBasedDialogueActTypeEstimator, sent2features_
from dialogue_system.language_understanding.utils.utils import sent2features
from training_data_generator.scripts.analyzer import analyze_morph


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


class MLBasedLanguageUnderstanding(object):

    def __init__(self):
        self.__predictor = MLBasedDialogueActTypeEstimator()
        self.__extractor = MLBasedAttributeExtractor()

    def execute(self, sent):
        features = sent2features_(sent)
        act_type = self.__predictor.predict([features])

        surfaces, features = analyze_morph(sent)
        morphed_sent = [[surfaces[i]] + features[i].split(',') for i in range(len(surfaces))]
        features = sent2features(morphed_sent)
        named_entity = self.__extractor.extract(features, morphed_sent)

        dialogue_act = {'user_act_type': act_type, 'utt': sent}
        dialogue_act.update(dict(named_entity))

        return dialogue_act


if __name__ == '__main__':
    sent = 'ラーメンを食べたい'
    language_understanding = MLBasedLanguageUnderstanding()
    language_understanding.execute(sent)
    sent = '西新宿'
    language_understanding.execute(sent)
    sent = '新宿近辺'
    language_understanding.execute(sent)