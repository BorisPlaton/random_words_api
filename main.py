from flask import Flask, request

from utils.words import WordsHandler


app = Flask(__name__)
words_file = WordsHandler('words_list.txt')


@app.route('words/')
def get_words():
    words_amount = request.args.get('amount', 150)
    words = words_file.get_words_from_file(words_amount)
