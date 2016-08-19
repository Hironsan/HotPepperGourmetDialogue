# -*- coding: utf-8 -*-
import os

from dialogue_system.knowledge.reader import data

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    save_file = os.path.join(BASE_DIR, 'words/genre.txt')
    genre = []
    for dic in data.values():
        synonyms = list(dic.keys())[0].split(',')
        genre.extend(synonyms)

    with open(save_file, 'w') as f:
        f.write('\n'.join(set(genre)))