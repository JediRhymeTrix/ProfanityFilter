from flask import Flask, request, abort, jsonify
from werkzeug.contrib.fixers import ProxyFix
from libs import ProfanityFilter, SentimentClassifier


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

    url = None if 'wordlist_url' not in request.json else request.json['wordlist_url']
    ignore_words_url = None if 'ignore_words_url' not in request.json else request.json['ignore_words_url']

    response = {}

    if 'filter' in options:
        words = ProfanityFilter.applyFilter(text, url, ignore_words_url)
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


app.wsgi_app = ProxyFix(app.wsgi_app)


if __name__ == '__main__':
    import logging

    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)

    app.run(host='0.0.0.0', debug=True)
