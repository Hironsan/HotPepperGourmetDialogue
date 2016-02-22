# -*- coding: utf-8 -*-

import os
import pickle


# 文生成
# 形態素解析
# IOB2タグ付け
# 保存
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
WORDS_DIR = os.path.join(BASE_DIR, 'words')
SAVE_DIR = os.path.join(os.path.dirname(BASE_DIR), 'training_data')

print(os.listdir(TEMPLATE_DIR))
print(os.listdir(WORDS_DIR))
for file_name in os.listdir(WORDS_DIR):
    print(os.path.abspath(file_name))
