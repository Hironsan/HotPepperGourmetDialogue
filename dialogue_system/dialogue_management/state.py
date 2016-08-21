# -*- coding: utf-8 -*-


class DialogueState(object):

    def __init__(self):
        self.__state = {'GENRE': None, 'LOCATION': None, 'MAXIMUM_AMOUNT': None}

    def update(self, dialogue_act):
        self.__state['GENRE'] = dialogue_act.get('GENRE', self.__state['GENRE'])
        self.__state['LOCATION'] = dialogue_act.get('LOCATION', self.__state['LOCATION'])
        self.__state['MAXIMUM_AMOUNT'] = dialogue_act.get('MAXIMUM_AMOUNT', self.__state['MAXIMUM_AMOUNT'])

    def has(self, name):
        return self.__state.get(name, None) != None

    def get_area(self):
        return self.__state['LOCATION']

    def get_food(self):
        return self.__state['GENRE']

    def get_budget(self):
        return self.__state['MAXIMUM_AMOUNT']

    def clear(self):
        self.__init__()

    def __str__(self):
        import pprint
        return pprint.pformat(self.__state)