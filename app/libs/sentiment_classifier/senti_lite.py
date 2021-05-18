from textblob import TextBlob


def classify(text):
    blob = TextBlob(text)  # .correct()
    sentiment = blob.sentiment
    sentence_count = len(blob.sentences)
    print sentiment
    confidence = calculate_confidence(sentiment, sentence_count)
    res = {'polarity': round(sentiment.polarity, 1), "confidence": confidence}

    return res


def calculate_confidence(sentiment, sentence_count):
    polarity = sentiment.polarity
    subjectivity = sentiment.subjectivity

    if polarity != 0.0:
        if polarity > -0.1 and polarity < 0.1:
            if sentence_count <= 5:
                return 'low'
        if subjectivity > 0.5:
            if polarity > -0.2 and polarity < 0.2:
                return 'low'
            else:
                return 'med'
        else:
            return 'high'
    else:
        return 'high'
