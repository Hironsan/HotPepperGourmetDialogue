# -*- coding: utf-8 -*-
import os
from itertools import chain

import yaml
import pycrfsuite
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelBinarizer


class MLBasedAttributeExtractor(object):

    def __init__(self, model_file='model.crfsuite'):
        self.__tagger = pycrfsuite.Tagger()
        try:
            file_path = os.path.join(os.path.dirname(__file__), 'model', model_file)
            self.__tagger.open(file_path)
        except FileNotFoundError:
            print('Learn')

    def train(self, train_x, train_y, save_file='model.crfsuite'):
        trainer = pycrfsuite.Trainer(verbose=False)
        for xseq, yseq in zip(train_x, train_y):
            trainer.append(xseq, yseq)
        trainer.set_params({
            'c1': 1.0,   # coefficient for L1 penalty
            'c2': 1e-3,  # coefficient for L2 penalty
            'max_iterations': 50,  # stop earlier
            'feature.possible_transitions': True
        })
        trainer.train(save_file)
        self.__tagger.open(save_file)

    def extract(self, xseq, sent):
        """
        千葉でラーメンを食べる
        -> [['LOC', '千葉'], ['GENRE', 'ラーメン']]
        """
        pred_y = self.__tagger.tag(xseq)
        res = []
        i = 0
        while i < len(pred_y):
            if pred_y[i].startswith('B'):
                word_stack = [sent[i][0]]
                label_stack = [pred_y[i]]
                i += 1
                while i < len(pred_y) and pred_y[i].startswith('I'):
                    word_stack = [sent[i][0]]
                    label_stack = [pred_y[i]]
                    i += 1
                label_stack = set([l.split('-')[1] for l in label_stack])
                res.append([''.join(label_stack), ''.join(word_stack)])
            else:
                i += 1

        return res

    def tagger(self, xseq):
        return self.__tagger.tag(xseq)

    def evaluate(self, y_true, y_pred):
        lb = LabelBinarizer()
        y_true_combined = lb.fit_transform(list(chain.from_iterable(y_true)))
        y_pred_combined = lb.transform(list(chain.from_iterable(y_pred)))

        tagset = set(lb.classes_) - {'O'}
        tagset = sorted(tagset, key=lambda tag: tag.split('-', 1)[::-1])
        class_indices = {cls: idx for idx, cls in enumerate(lb.classes_)}

        return classification_report(
            y_true_combined,
            y_pred_combined,
            labels=[class_indices[cls] for cls in tagset],
            target_names=tagset,
        )


if __name__ == '__main__':
    import os
    import pickle
    import random
    from dialogue_system.language_understanding.utils.utils import sent2features, sent2labels
    f = lambda path: os.path.dirname(path)

    root_dir = f(f(f(f(__file__))))
    training_data_dir = os.path.join(root_dir, 'training_data')
    training_data = []

    for file_name in os.listdir(training_data_dir):
        if not file_name.endswith('.pkl'):
            continue
        file_path = os.path.join(training_data_dir, file_name)
        with open(file_path, 'rb') as rf:
            tmp_data = pickle.load(rf)
            training_data.extend(tmp_data)

    random.shuffle(training_data)
    train_num = int(len(training_data) * 0.9)
    train_sents = training_data[:train_num]
    test_sents = training_data[train_num:]

    train_x = [sent2features(s) for s in train_sents]
    train_y = [sent2labels(s) for s in train_sents]

    test_x = [sent2features(s) for s in test_sents]
    test_y = [sent2labels(s) for s in test_sents]

    extractor = MLBasedAttributeExtractor()
    extractor.train(train_x, train_y)

    pred_y = [extractor.tagger(xseq) for xseq in test_x]
    print(extractor.evaluate(test_y, pred_y))
