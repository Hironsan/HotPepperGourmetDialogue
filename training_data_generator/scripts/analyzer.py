import MeCab


def analyze_morph(sent):
    surfaces = []
    features = []
    t = MeCab.Tagger()
    t.parse('')
    m = t.parseToNode(sent)
    while m:
        if m.feature.startswith('BOS/EOS'):
            m = m.next
            continue
        surfaces.append(m.surface)
        features.append(m.feature)
        m = m.next
    return surfaces, features


if __name__ == '__main__':
    sent = "太郎はこの本を二郎を見た女性に渡した。"