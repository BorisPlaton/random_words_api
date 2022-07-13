import os

from random_words.utils.shortcuts import create_app


if __name__ == '__main__':
    from dotenv import load_dotenv

    load_dotenv()
    app = create_app(os.getenv('CONFIG_FILE'))
    app.run()
