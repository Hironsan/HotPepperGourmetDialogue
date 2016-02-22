# -*- coding: utf-8 -*-

import yaml

FILEIN_DICT = "sample_dict.yaml"
FILEIN_DICT = "ontology/genre.yaml"

f = open(FILEIN_DICT, 'r')
data = yaml.load(f)  # 読み込む
f.close()
print(data)