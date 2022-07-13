import os

from flask import Flask
from flask_restful import Api

from random_words.config.settings_file import settings
from random_words.utils.words import words_file


def create_app(json_config) -> Flask:
    """Создаёт экземпляр приложения и возвращает его."""
    settings.load_config_file(json_config)
    words_file.set_words_files(settings['WORDS']['FILES'])

    app = Flask(__name__)
    app.debug = os.getenv('DEBUG') == '1'

    from random_words.views import GetWords
    api = Api(catch_all_404s=True)
    api.add_resource(GetWords, '/')

    api.init_app(app)

    return app
