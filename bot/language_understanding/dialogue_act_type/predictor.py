# -*- coding: utf-8 -*-
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier

from bot.language_understanding.utils.utils import *


class DialogueActTypePredictor(object):

    def __init__(self, file_name='model.pkl'):
        try:
            file_path = os.path.join(os.path.dirname(__file__), file_name)
            self.estimator = joblib.load(file_path)
        except FileNotFoundError:
            self.estimator = RandomForestClassifier()

    def train(self, train_x, train_y, file_name='model.pkl'):
        self.estimator.fit(train_x, train_y)
        joblib.dump(self.estimator, file_name)

    def predict(self, X):
        return self.estimator.predict(X)[0]

    def evaluate(self, test_x, test_y):
        print(self.estimator.score(test_x, test_y))


def sent2features_(sent):
    from training_data_generator.scripts.analyzer import analyze_morph
    dic_path = os.path.join(os.path.dirname(__file__), 'dic.txt')
    surfaces, _ = analyze_morph(sent)
    dictionary = corpora.Dictionary.load_from_text(dic_path)
    features = to_features(dictionary, surfaces)

    return features

if __name__ == '__main__':
    import os
    import pickle
    import random

    f = lambda path: os.path.dirname(path)

    root_dir = f(f(f(f(__file__))))
    training_data_dir = os.path.join(root_dir, 'training_data')
    sents = []
    labels = []

    for file_name in os.listdir(training_data_dir):
        if not file_name.endswith('.pkl'):
            continue
        category = file_name.split('.')[0]
        file_path = os.path.join(training_data_dir, file_name)
        with open(file_path, 'rb') as rf:
            tmp_data = pickle.load(rf)
            sents.extend(tmp_data)
            labels.extend([category] * len(tmp_data))

    # shuffle
    for i in range(len(sents)):
        j = random.randint(i, len(sents) - 1)
        sents[i], sents[j] = sents[j], sents[i]
        labels[i], labels[j] = labels[j], labels[i]

    train_num = int(len(sents) * 0.9)
    train_sents = sents[:train_num]
    test_sents = sents[train_num:]

    words = get_words(sents)

    dic_name = 'dic.txt'
    try:
        dictionary = corpora.Dictionary.load_from_text(dic_name)
    except FileNotFoundError:
        dictionary = create_dictionary(words)
        dictionary.save_as_text(dic_name)

    train_x = [to_features(dictionary, words) for words in get_words(train_sents)]
    train_y = labels[:train_num]

    test_x = [to_features(dictionary, words) for words in get_words(test_sents)]
    test_y = labels[train_num:]

    predictor = DialogueActTypePredictor()
    predictor.train(train_x, train_y)
    predictor.evaluate(test_x, test_y)


