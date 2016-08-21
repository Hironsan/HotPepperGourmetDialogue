import re
from gensim import corpora, matutils


tt_ksuji = str.maketrans('一二三四五六七八九〇壱弐参', '1234567890123')

re_suji = re.compile(r'[十拾百千万億兆\d]+')
re_kunit = re.compile(r'[十拾百千]|\d+')
re_manshin = re.compile(r'[万億兆]|[^万億兆]+')

TRANSUNIT = {'十': 10,
             '拾': 10,
             '百': 100,
             '千': 1000}
TRANSMANS = {'万': 10000,
             '億': 100000000,
             '兆': 1000000000000}


def kansuji2arabic(string, sep=False):
    """漢数字をアラビア数字に変換"""

    def _transvalue(sj, re_obj=re_kunit, transdic=TRANSUNIT):
        unit = 1
        result = 0
        for piece in reversed(re_obj.findall(sj)):
            if piece in transdic:
                if unit > 1:
                    result += unit
                unit = transdic[piece]
            else:
                val = int(piece) if piece.isdecimal() else _transvalue(piece)
                result += val * unit
                unit = 1

        if unit > 1:
            result += unit

        return result

    transuji = string.translate(tt_ksuji)
    for suji in sorted(set(re_suji.findall(transuji)), key=lambda s: len(s),
                           reverse=True):
        if not suji.isdecimal():
            arabic = _transvalue(suji, re_manshin, TRANSMANS)
            arabic = '{:,}'.format(arabic) if sep else str(arabic)
            transuji = transuji.replace(suji, arabic)

    return transuji


def is_hiragana(ch):
    return 0x3040 <= ord(ch) <= 0x309F


def is_katakana(ch):
    return 0x30A0 <= ord(ch) <= 0x30FF


def get_character_type(ch):
    if ch.isspace():
        return 'ZSPACE'
    elif ch.isdigit():
        return 'ZDIGIT'
    elif ch.islower():
        return 'ZLLET'
    elif ch.isupper():
        return 'ZULET'
    elif is_hiragana(ch):
        return 'HIRAG'
    elif is_katakana(ch):
        return 'KATAK'
    else:
        return 'OTHER'


def get_character_types(string):
    character_types = map(get_character_type, string)
    character_types_str = '-'.join(sorted(set(character_types)))

    return character_types_str


def extract_pos_with_subtype(morph):
    idx = morph.index('*')

    return '-'.join(morph[1:idx])


def word2features(sent, i):
    word = sent[i][0]
    chtype = get_character_types(sent[i][0])
    postag = extract_pos_with_subtype(sent[i])
    features = [
        'bias',
        'word=' + word,
        'type=' + chtype,
        'postag=' + postag,
    ]
    if i >= 2:
        word2 = sent[i-2][0]
        chtype2 = get_character_types(sent[i-2][0])
        postag2 = extract_pos_with_subtype(sent[i-2])
        iobtag2 = sent[i-2][-1]
        features.extend([
            '-2:word=' + word2,
            '-2:type=' + chtype2,
            '-2:postag=' + postag2,
            '-2:iobtag=' + iobtag2,
        ])
    else:
        features.append('BOS')

    if i >= 1:
        word1 = sent[i-1][0]
        chtype1 = get_character_types(sent[i-1][0])
        postag1 = extract_pos_with_subtype(sent[i-1])
        iobtag1 = sent[i-1][-1]
        features.extend([
            '-1:word=' + word1,
            '-1:type=' + chtype1,
            '-1:postag=' + postag1,
            '-1:iobtag=' + iobtag1,
        ])
    else:
        features.append('BOS')

    if i < len(sent)-1:
        word1 = sent[i+1][0]
        chtype1 = get_character_types(sent[i+1][0])
        postag1 = extract_pos_with_subtype(sent[i+1])
        features.extend([
            '+1:word=' + word1,
            '+1:type=' + chtype1,
            '+1:postag=' + postag1,
        ])
    else:
        features.append('EOS')

    if i < len(sent)-2:
        word2 = sent[i+2][0]
        chtype2 = get_character_types(sent[i+2][0])
        postag2 = extract_pos_with_subtype(sent[i+2])
        features.extend([
            '+2:word=' + word2,
            '+2:type=' + chtype2,
            '+2:postag=' + postag2,
        ])
    else:
        features.append('EOS')

    return features


def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]


def sent2labels(sent):
    return [morph[-1] for morph in sent]


def sent2tokens(sent):
    return [morph[0] for morph in sent]


def word2features_(word):
    pass


def sent2features_(sent):
    return [word2features_(word) for word in sent]


def get_words(sents):
    res = []
    for sent in sents:
        words = []
        for word in sent:
            if word[1] == '名詞':
                surface = word[0]
                words.append(surface)
        res.append(words)

    return res


def create_dictionary(words):
    dic = corpora.Dictionary(words)

    return dic

def create_bow(dictionary, words):
    vec = dictionary.doc2bow(words)

    return vec

def to_features(dictionary, words):
    tmp = dictionary.doc2bow(words)
    dense = list(matutils.corpus2dense([tmp], num_terms=len(dictionary)).T[0])

    return dense