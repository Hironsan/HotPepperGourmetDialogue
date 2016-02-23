# -*- coding: utf-8 -*-
from training_data_generator.scripts.analyzer import analyze_morph


def tagging(l, r, ne, ylabel):
    for i in range(l, r):
        prefix = 'B' if i == l else 'I'
        ylabel[i] = prefix + '-' + ne


def matching(sentence, ne_list):

    def get_word_pos_list(sentence, ne_list):
        word_pos_list = []
        searched_pos = 0
        for nw, ne in ne_list:
            nw = ''.join(nw.split(' '))
            idx = sentence.index(nw, searched_pos)
            searched_pos = idx + len(nw)
            word_pos_list.append((idx, searched_pos))

        return word_pos_list

    def get_morph_pos_list(wakati, word_pos_list):
        morph_pos_list = []
        for start_pos, end_pos in word_pos_list:
            ch_cnt = 0
            morph_pos = []
            for i, morph in enumerate(wakati):
                if ch_cnt < start_pos:
                    ch_cnt += len(morph)
                elif ch_cnt < end_pos:
                    morph_pos.append(i)
                    ch_cnt += len(morph)
                else:
                    break
            morph_pos_list.append(morph_pos)

        return morph_pos_list

    def tagging(morph_pos_list, ne_list, ylabel):
        for i in range(len(ne_list)):
            nw, ne = ne_list[i]
            morph_pos = morph_pos_list[i]
            for j, k in enumerate(morph_pos):
                prefix = 'B' if j == 0 else 'I'
                ylabel[k] = prefix + '-' + ne

    wakati, features = analyze_morph(sentence)
    sentence = ''.join(sentence.split(' '))
    word_pos_list = get_word_pos_list(sentence, ne_list)
    morph_pos_list = get_morph_pos_list(wakati, word_pos_list)

    ylabel = ['O'] * len(wakati)

    tagging(morph_pos_list, ne_list, ylabel)

    labeled_sent = []
    for i in range(len(wakati)):
        tmp = []
        tmp.append(wakati[i])
        tmp.extend(features[i].split(','))
        tmp.append(ylabel[i])
        labeled_sent.append(tmp)

    # Error
    for word_pos, morph_pos in zip(word_pos_list, morph_pos_list):
        start_pos, end_pos = word_pos
        word1, word2 = sentence[start_pos: end_pos], ''.join([wakati[i] for i in morph_pos])
        if word1 != word2:
            print(word1, word2)

    return labeled_sent


if __name__ == '__main__':
    sent = '中華がいい'
    ne_list = [['中華', 'GENRE']]
    labeled_sent = matching(sent, ne_list)
    for morph in labeled_sent:
        print(','.join(morph))