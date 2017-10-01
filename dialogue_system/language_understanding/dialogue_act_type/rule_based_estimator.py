# -*- coding: utf-8 -*-


class RuleBasedDialogueActTypeEstimator(object):

    def __init__(self):
        pass

    def estimate(self, attribute):
        if attribute['GENRE'] != '':
            return 'genre'
        elif attribute['LOCATION'] != '':
            return 'location'
        elif attribute['MAXIMUM_AMOUNT'] != '':
            return 'maximum_amount'
        else:
            return 'other'
