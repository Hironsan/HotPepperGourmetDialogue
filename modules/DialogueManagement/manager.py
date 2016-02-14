# -*- coding: utf-8 -*-


class DialogueManager(object):

    def __init__(self):
        pass

    def update_dialogue_state(self, act_type, named_entities, state):
        state.update(act_type, named_entities)

    def select_action(self, state, api):
        pass