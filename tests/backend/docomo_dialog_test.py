# -*- coding: utf-8 -*-
import unittest
from modules.BackEnd.APIs.docomo_dialogue import DocomoDialogAPI


class DocomoDialogAPITest(unittest.TestCase):

    def setUp(self):
        self.api = DocomoDialogAPI()

    def tearDown(self):
        pass

    def test_areaname_to_areacode(self):
        reply = self.api.reply(text='こんにちは')
        self.assertIsInstance(reply, str)