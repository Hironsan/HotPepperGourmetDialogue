# -*- coding: utf-8 -*-


class DialogueManager(object):

    def __init__(self):
        pass

    def update_dialogue_state(self, dialogue_act, state):
        state.update(dialogue_act)

    def select_action(self, dialogue_act, state, api):
        from copy import deepcopy
        sys_act = deepcopy(dialogue_act)
        if not state.has('LOCATION'):
            sys_act['next'] = 'LOCATION'
        elif not state.has('GENRE'):
            sys_act['next'] = 'GENRE'
        elif not state.has('MAXIMUM_AMOUNT'):
            sys_act['next'] = 'MAXIMUM_AMOUNT'
        else:
            sys_act['next'] = 'API'

        return sys_act