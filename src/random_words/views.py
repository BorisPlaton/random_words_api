import logging

from flask import request

from configuration import settings
from random_words.utils.base_views import BaseView
from random_words.utils.words import words_file


class GetWords(BaseView):
    """View-class для получения списка слов."""

    log_file = settings.BASE_DIR.parent / 'logs' / 'words_logs.log'
    logger_level = logging.INFO

    def get(self):
        """Возвращает клиенту список слов на выбранном языком."""
        try:
            words_list = (words_file[self.get_words_language_query_parameter()]
                          .get_words_from_file(self.get_words_amount_query_parameter()))
        except ValueError as e:
            self.logger.info('%s - %s' % (request.remote_addr, str(e)))
            return {'error': str(e)}, 400
        return {
            'words': words_list,
        }

    @staticmethod
    def get_words_amount_query_parameter() -> int:
        """
        Получает количество слов из url-параметра `quantity`.

        Значение параметра `quantity` должно быть числом и больше нуля.
        Если это не число, то вернет значение из настроек
        `settings['WORDS']['DEFAULT_QUANTITY']`. Если число меньше 0, то
        вернет ответ пользователю со статусом 400 и сообщением, что
        количество слов не может быть отрицательным числом.
        """
        words_amount = request.args.get(
            'quantity',
            int(settings.json['WORDS']['DEFAULT_QUANTITY']),
            type=int,
        )
        if words_amount < 0:
            raise ValueError("Words quantity can't be a negative number `%s`" % words_amount)
        return words_amount

    @staticmethod
    def get_words_language_query_parameter() -> str:
        """
        Получает язык слов из url-параметра `lang`.

        Значение параметра `lang` должно находиться в ключах
        `settings['FILES']` json-файла конфига, иначе
        будет вызвана ошибка, что такой язык недоступен. Если
        параметр не будет указан, то будет использоваться значение,
        которое указано в `settings['WORDS']['DEFAULT_LANGUAGE']`.
        """
        words_language = request.args.get(
            'lang',
            settings.json['WORDS']['DEFAULT_LANGUAGE'],
        )
        if words_language not in settings.json['FILES']:
            raise ValueError(
                "Incorrect language - `%s`. Only %s are available." %
                (words_language, f"`{'`, `'.join(settings.json['FILES'].keys())}`")
            )
        return words_language
