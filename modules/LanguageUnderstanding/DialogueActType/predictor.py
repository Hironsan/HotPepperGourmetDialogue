# -*- coding: utf-8 -*-
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


class DialogueActTypePredictor(object):

    def __init__(self, C=1, kernel='rbf', gamma=0.01):
        estimator = SVC(C=C, kernel=kernel, gamma=gamma)
        self.__classifier = OneVsRestClassifier(estimator)

    def train(self, train_x, train_y):
        self.__classifier.fit(train_x, train_y)

    def predict(self, sent):
        pass

    def evaluate(self, test_x, test_y):
        pred_y = self.__classifier.predict(test_x)
        print('One-against-rest: {:.5f}'.format(accuracy_score(test_y, pred_y)))

    def extract_feature(self):
        pass