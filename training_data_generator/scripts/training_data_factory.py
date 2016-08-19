# -*- coding: utf-8 -*-

import os
import pickle
from training_data_generator.scripts.analyzer import analyze_morph
from training_data_generator.scripts.matching import matching


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
WORDS_DIR = os.path.join(BASE_DIR, 'words')
SAVE_DIR = os.path.join(os.path.dirname(BASE_DIR), 'training_data')



file_list = ['genre.txt', 'locations.txt', 'maximum_amount.txt']
template_strs = ['GENRE', 'LOCATION', 'MAXIMUM_AMOUNT']

for file_name, template_str in zip(file_list, template_strs):
    template_path = os.path.join(TEMPLATE_DIR, file_name)
    words_path = os.path.join(WORDS_DIR, file_name)

    with open(template_path) as tf, open(words_path) as wf:
        templates = [line.strip() for line in tf]
        words = [line.strip() for line in wf]

    # 文生成
    training_data = []
    for template in templates:
        for word in words:
            sent = template.replace(template_str, word)

            # 形態素解析とIOB2タグ付け
            labeled_sent = matching(sent, [[word, template_str]])

            training_data.append(labeled_sent)

    # 保存
    save_path = os.path.join(SAVE_DIR, template_str.lower() + '.pkl')
    with open(save_path, 'wb') as f:
        pickle.dump(training_data, f)

sents_path = os.path.join(WORDS_DIR, 'other.txt')
with open(sents_path) as wf:
    sents = [line.strip() for line in wf]

training_data = []
for sent in sents:
    labeled_sent = matching(sent, [['', '']])
    training_data.append(labeled_sent)
save_path = os.path.join(SAVE_DIR, 'other.pkl')
with open(save_path, 'wb') as f:
    pickle.dump(training_data, f)