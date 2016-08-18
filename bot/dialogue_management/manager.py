# -*- coding: utf-8 -*-
from bot.dialogue_management.state import DialogueState
from bot.backend.apis.hotpepper import HotPepperGourmetAPI


class DialogueManager(object):

    def __init__(self):
        self.dialogue_state = DialogueState()

    def update_dialogue_state(self, dialogue_act):
        self.dialogue_state.update(dialogue_act)

    def select_action(self, dialogue_act):
        from copy import deepcopy
        sys_act = deepcopy(dialogue_act)
        if not self.dialogue_state.has('LOCATION'):
            sys_act['sys_act_type'] = 'REQUEST_LOCATION'
        elif not self.dialogue_state.has('GENRE'):
            sys_act['sys_act_type'] = 'REQUEST_GENRE'
        elif not self.dialogue_state.has('MAXIMUM_AMOUNT'):
            sys_act['sys_act_type'] = 'REQUEST_BUDGET'
        else:
            api = HotPepperGourmetAPI()
            area = self.dialogue_state.get_area()
            food = self.dialogue_state.get_food()
            budget = self.dialogue_state.get_budget()
            restaurant = api.search_restaurant(area=area, food=food,budget=budget)
            sys_act['sys_act_type'] = 'INFORM_RESTAURANT'
            sys_act['restaurant'] = restaurant

        return sys_act