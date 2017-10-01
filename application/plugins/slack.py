# -*- coding: utf-8 -*-

from slackbot.bot import respond_to

from dialogue_system.bot import Bot

bots = {}


def create_or_read(user_id):
    return bots[user_id] if user_id in bots else Bot()


def save_bot(bot, user_id):
    bots[user_id] = bot


@respond_to('(.*)')
def food(message, something):
    body = message.body
    text, ts, user_id = body['text'], body['ts'], body['user']
    bot = create_or_read(user_id)
    reply_message = bot.reply(text)
    save_bot(bot, user_id)
    message.reply(reply_message)

