from unidecode import unidecode

from sentiment_classifier import senti_heavy, senti_lite


def classify(text, heavy=False):
    text = unidecode(text).encode('UTF-8', 'ignore')

    if heavy:
        res = senti_heavy.classify(text)
    else:
        res = senti_lite.classify(text)

    return res


def normalize_scores(pos_score, neg_score):
    tot_score = pos_score + neg_score

    if tot_score != 0:
        pos_score = round(pos_score / tot_score, 1)
        neg_score = round(1 - pos_score, 1)
    else:
        pos_score, neg_score = 0, 0

    return pos_score, neg_score
