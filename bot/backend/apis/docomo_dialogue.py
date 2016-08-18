# -*- coding: utf-8 -*-
import os

import requests


class DocomoDialogAPI(object):
    BASE_URL = 'https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue'

    def __init__(self, api_key=None):
        self.__api_key = os.environ.get('DOCOMO_DIALOG_API_KEY', api_key)

    def reply(self, text):
        params = {'APIKEY': self.__api_key, 'utt': text}
        response = requests.post(self.BASE_URL, params).json()
        utt = response['utt']

        return utt
