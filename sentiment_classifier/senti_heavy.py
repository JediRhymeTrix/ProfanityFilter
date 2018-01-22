from nltk.tokenize import sent_tokenize

import senti_classifier


def classify(text):
    sentences = sent_tokenize(text)
    pos_score, neg_score = senti_classifier.polarity_scores(sentences)
    polarity = normalize_scores(pos_score, neg_score)
    res = {'polarity': polarity}

    return res


def normalize_scores(pos_score, neg_score):
    tot_score = pos_score + neg_score

    if tot_score != 0:
        pos_score = pos_score / tot_score
        neg_score = 1 - pos_score
    else:
        pos_score = neg_score = 0

    polarity = round(pos_score - neg_score, 1)

    return polarity
