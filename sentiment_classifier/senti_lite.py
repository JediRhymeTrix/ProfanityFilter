from textblob import TextBlob


def classify(text):
    blob = TextBlob(text)
    res = {'polarity': round(blob.sentiment.polarity, 1)}

    return res
