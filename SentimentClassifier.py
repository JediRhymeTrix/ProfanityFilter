from nltk import sent_tokenize
from senti_classifier import senti_classifier


def classify(text):
    sentences = sent_tokenize(text)
    pos_score, neg_score = senti_classifier.polarity_scores(sentences)

    tot_score = pos_score + neg_score
    pos_score = round(pos_score / tot_score, 1) if pos_score != 0 else 0
    neg_score = round(1 - pos_score, 1)

    return {'pos': pos_score, 'neg': neg_score}

