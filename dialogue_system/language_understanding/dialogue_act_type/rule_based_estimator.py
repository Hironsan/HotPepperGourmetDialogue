# -*- coding: utf-8 -*-


class RuleBasedDialogueActTypeEstimator(object):

    def __init__(self):
        pass

    def estimate(self, attribute):
        if attribute['GENRE'] != '':
            return 'INFORM_GENRE'
        elif attribute['LOCATION'] != '':
            return 'INFORM_LOC'
        elif attribute['MAXIMUM_AMOUNT'] != '':
            return 'INFORM_MONEY'
        else:
            return 'OTHER'
