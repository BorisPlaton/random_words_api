from flask import request
from flask_restful import Resource

from utils.words import words_file


class GetWords(Resource):
    """View-class для получения списка слов."""

    def get(self):
        words_amount = request.args.get('amount', 2)
        words_list = words_file.get_words_from_file(words_amount)
        return {
            'words': words_list,
        }
