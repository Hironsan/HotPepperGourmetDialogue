# -*- coding: utf-8 -*-
import os
import yaml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, 'ontology/genre.yaml')

with open(file_path, 'r') as f:
    data = yaml.load(f)