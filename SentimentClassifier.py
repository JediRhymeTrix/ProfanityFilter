from nltk import sent_tokenize
from unidecode import unidecode

from sentiment_classifier import senti_classifier


def classify(text):
    sentences = sent_tokenize(unidecode(text))
    pos_score, neg_score = senti_classifier.polarity_scores(sentences)
    pos_score, neg_score = normalize_scores(pos_score, neg_score)
    res = {'pos': pos_score, 'neg': neg_score}

    return res


def normalize_scores(pos_score, neg_score):
    tot_score = pos_score + neg_score

    if tot_score != 0:
        pos_score = round(pos_score / tot_score, 1)
        neg_score = round(1 - pos_score, 1)
    else:
        pos_score, neg_score = 0, 0

    return pos_score, neg_score
