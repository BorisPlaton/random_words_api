from utils.shortcuts import create_app


if __name__ == '__main__':
    from dotenv import load_dotenv

    load_dotenv()
    app = create_app('config.json')
    app.run()
