# -*- coding: utf-8 -*-
import os


API_TOKEN = os.environ.get('SLACK_API_KEY', '')
 
default_reply = "スイマセン。其ノ言葉ワカリマセン"

PLUGINS = [
    'plugins',
]