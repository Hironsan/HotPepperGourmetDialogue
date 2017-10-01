# -*- coding: utf-8 -*-
from dialogue_system.bot import Bot


if __name__ == '__main__':
    bot = Bot()

    print('S: 料理のジャンルや場所をおっしゃってください。')
    while True:
        sent = input('U: ')
        if sent == 'ありがとう':
            print('S: どういたしまして')
            break

        reply = bot.reply(sent)
        print('S: {0}'.format(reply))
