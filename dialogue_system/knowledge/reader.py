# -*- coding: utf-8 -*-
import os
import yaml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read_locations():
    file_path = os.path.join(BASE_DIR, 'locations.txt')
    with open(file_path, 'r') as f:
        locations = [loc.strip() for loc in f]

    return locations


def read_genres():
    file_path = os.path.join(BASE_DIR, 'genre.yaml')
    with open(file_path, 'r') as f:
        genres = yaml.load(f)

    return genres