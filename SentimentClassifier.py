from nltk import sent_tokenize
from senti_classifier import senti_classifier


def classify(text):
    sentences = sent_tokenize(text)
    pos_score, neg_score = senti_classifier.polarity_scores(sentences)
    return {'pos': pos_score, 'neg': neg_score}

    # return {'pos': 0.6, 'neg': 0.4}
