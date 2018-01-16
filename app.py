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

    print text

    words = ProfanityFilter.applyFilter(text)
    sentiment = SentimentClassifier.classify(text)

    print words, sentiment

    response = {'words': words, 'sentiment': sentiment}

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
