import os

from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api


api = Api()


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.debug = os.getenv('DEBUG') == '1'

    from views import GetWords
    api.add_resource(GetWords, '/')

    api.init_app(app)

    return app
