from flask import Flask, request, abort, jsonify

import ProfanityFilter
import SentimentClassifier

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/process', methods=['POST'])
def process_post():
    if not request.json or 'post' not in request.json or 'options' not in request.json:
        abort(400)

    text = request.json['post']
    options = request.json['options']

    url = None if 'ignore_words' not in request.json else request.json['ignore_words']

    response = {}

    if 'filter' in options:
        words = ProfanityFilter.applyFilter(text, url)
        response['profanities'] = words
    # if 'keywords' in options: # keyword finder is WIP
    #     words = KeyWordsFinder.findKeywords(text)
    #     response['keywords'] = words
    if 'sentiment' in options:
        sentiment = SentimentClassifier.classify(text)
        response['sentiment'] = sentiment
    elif 'sentiment_heavy' in options:
        sentiment = SentimentClassifier.classify(text, heavy=True)
        response['sentiment'] = sentiment

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# TODO: Improve classifier performance
