# -*- coding: utf-8 -*-


class LanguageGenerator(object):

    def __init__(self):
        pass

    def generate_sentence(self, dialogue_act):
        sent = 'S: '
        if 'LOCATION' in dialogue_act:
            sent += '場所は{0}ですね。'.format(dialogue_act['LOCATION'])
        if 'GENRE' in dialogue_act:
            sent += '{0}ですね。'.format(dialogue_act['GENRE'])
        if 'MAXIMUM_AMOUNT' in dialogue_act:
            sent += '予算は{0}円ですね。'.format(dialogue_act['MAXIMUM_AMOUNT'])

        if dialogue_act['next'] == 'LOCATION':
            sent += '場所はどのあたりですか？'
        elif dialogue_act['next'] == 'GENRE':
            sent += '料理のジャンルを教えてください。'
        elif dialogue_act['next'] == 'MAXIMUM_AMOUNT':
            sent += '予算の上限はどのくらいですか？'
        else:
            sent += 'ではこちらの場所はどうでしょうか？（HotPepper APIを叩いて場所を出す）'

        return sent