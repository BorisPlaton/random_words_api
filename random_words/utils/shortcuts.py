import os
from pathlib import Path

from flask import Flask
from flask_restful import Api

from random_words.utils.words import words_file
from configuration import settings


def create_app(config_file, config_pyfile) -> Flask:
    """Создаёт экземпляр приложения и возвращает его."""

    settings.setup_config_from_settings(config_pyfile)

    settings.setup_config_files(
        {'json': Path(config_file).resolve()}
    )

    words_file.set_words_files(settings.json['FILES'])

    app = Flask(__name__)
    app.debug = os.getenv('DEBUG') == '1'

    from random_words.views import GetWords
    api = Api(catch_all_404s=True)
    api.add_resource(GetWords, '/')

    api.init_app(app)
    return app
