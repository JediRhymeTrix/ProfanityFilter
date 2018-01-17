from nltk import sent_tokenize
from senti_classifier import senti_classifier


def classify(text):
    sentences = sent_tokenize(text)
    pos_score, neg_score = senti_classifier.polarity_scores(sentences)

    tot_score = pos_score + neg_score
    pos_score = round(pos_score / tot_score, 1)
    neg_score = 1 - pos_score

    return {'pos': pos_score, 'neg': neg_score}

    # return {'pos': 0.6, 'neg': 0.4}
