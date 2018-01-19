from flask import Flask, request, abort, jsonify

import ProfanityFilter
import SentimentClassifier

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/process', methods=['POST'])
def process_post():
    if not request.json or 'post' not in request.json:
        abort(400)

    text = request.json['post']
    url = None if 'ignore_words' not in request.json else request.json['ignore_words']

    words = ProfanityFilter.applyFilter(text, url)
    sentiment = SentimentClassifier.classify(text)

    response = {'words': words, 'sentiment': sentiment}

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# TODO: Improve classifier performance
