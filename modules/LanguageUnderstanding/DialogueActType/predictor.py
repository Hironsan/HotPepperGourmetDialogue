# -*- coding: utf-8 -*-
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib


class DialogueActTypePredictor(object):

    def __init__(self, C=1, kernel='rbf', gamma=0.01, file_name='model.pkl'):
        try:
            self.__classifier = joblib.load(file_name)
        except FileNotFoundError:
            estimator = SVC(C=C, kernel=kernel, gamma=gamma)
            self.__classifier = OneVsRestClassifier(estimator)

    def train(self, train_x, train_y, file_name='model.pkl'):
        self.__classifier.fit(train_x, train_y)
        joblib.dump(self.__classifier, file_name)

    def predict(self, sent):
        pass

    def evaluate(self, test_x, test_y):
        pred_y = self.__classifier.predict(test_x)
        print('One-against-rest: {:.5f}'.format(accuracy_score(test_y, pred_y)))


if __name__ == '__main__':
    import os
    import pickle
    import random
    from modules.LanguageUnderstanding.utils.utils import *
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
    dictionary = create_dictionary(words)

    train_x = [to_features(dictionary, words) for words in get_words(train_sents)]
    train_y = labels[:train_num]

    test_x = [to_features(dictionary, words) for words in get_words(test_sents)]
    test_y = labels[train_num:]

    from sklearn.ensemble import RandomForestClassifier
    estimator = RandomForestClassifier()
    # 学習させる
    estimator.fit(train_x, train_y)
    print(estimator.score(test_x, test_y))
    """
    predictor = DialogueActTypePredictor()
    predictor.train(train_x, train_y)
    predictor.evaluate(test_x, test_y)
    """