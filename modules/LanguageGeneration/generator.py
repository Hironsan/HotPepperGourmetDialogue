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

        sys_act_type = dialogue_act['sys_act_type']
        if sys_act_type == 'REQUEST_LOCATION':
            sent += '場所はどのあたりですか？'
        elif sys_act_type == 'REQUEST_GENRE':
            sent += '料理のジャンルを教えてください。'
        elif sys_act_type == 'REQUEST_BUDGET':
            sent += '予算の上限はどのくらいですか？'
        elif sys_act_type == 'INFORM_RESTAURANT':
            #sent += 'ではこちらの場所はどうでしょうか？\n'
            restaurant = dialogue_act['restaurant']
            name, address, access = restaurant['name'], restaurant['address'], restaurant['access']
            sent += 'では、{0}がおすすめです。場所は{1}で{2}です。'.format(name, address, access)
        else:
            print('Error')
            import sys
            sys.exit(-1)

        return sent