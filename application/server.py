# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import tornado.websocket

from dialogue_system.bot import Bot


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('Hello World!')


class MessageServer(tornado.websocket.WebSocketHandler):
    bots = {}

    def check_origin(self, origin):
        return True

    def open(self):
        print('on open')
        self.bots[self] = Bot()
        self.write_message('料理のジャンルや場所をおっしゃってください。')

    def on_message(self, message):
        print('on message')
        print(message)
        bot = self.bots[self]
        self.write_message(bot.reply(message))

    def on_close(self):
        print('on close')
        del self.bots[self]

application = tornado.web.Application([
    (r'/', IndexHandler),
    (r'/ws', MessageServer)
    ])

if __name__ == '__main__':
    application.listen(8080)
    tornado.ioloop.IOLoop.current().start()