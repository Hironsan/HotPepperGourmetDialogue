# -*- coding: utf-8 -*-
import sys


class LanguageGenerator(object):

    def __init__(self):
        pass

    def generate_sentence(self, dialogue_act):
        sent = ''
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
        elif sys_act_type == 'CHAT':
            sent += dialogue_act['utt']
        elif sys_act_type == 'INFORM_RESTAURANT':
            restaurant = dialogue_act['restaurant']
            if restaurant:
                name, address, access = restaurant['name'], restaurant['address'], restaurant['access']
                lat, lng = restaurant['lat'], restaurant['lng']
                sent += 'では、{0}がおすすめです。\n場所は{1}で{2}です。\n'.format(name, address, access)
                url = 'https://maps.googleapis.com/maps/api/staticmap?center={0},{1}&size=640x480&zoom=14&markers={0},{1}'
                sent += url.format(lat, lng)
            else:
                sent += '申し訳ありません。条件に一致するお店が見つかりませんでした。'
        else:
            print('Error')
            sys.exit(-1)

        return sent