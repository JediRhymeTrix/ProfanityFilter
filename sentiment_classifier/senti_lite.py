from textblob import TextBlob


def classify(text):
    blob = TextBlob(text).correct()
    res = {'polarity': round(blob.sentiment.polarity, 1)}

    return res
