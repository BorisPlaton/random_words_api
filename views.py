import logging
import os

from flask import request

from config.settings import BASE_DIR
from utils.views import BaseView
from utils.words import words_file


class GetWords(BaseView):
    """View-class для получения списка слов."""

    log_file = BASE_DIR / 'logs' / 'words_logs.log'
    file_log_level = logging.INFO

    def get(self):
        """Возвращает клиенту список слов."""
        try:
            words_list = words_file.get_words_from_file(
                self.get_words_amount_parameter()
            )
        except ValueError as e:
            self.logger.info('%s - %s' % (request.remote_addr, str(e)))
            return {'error': str(e)}, 400
        return {
            'words': words_list,
        }

    def get_words_amount_parameter(self) -> int:
        """
        Получает количество слов из параметра `amount` url-адреса.

        Значение параметра `amount` должно быть числом и больше нуля.
        Если это не число, то вернет значение из переменной окружения
        `DEFAULT_WORDS_QUANTITY`. Если число меньше 0, то вернет ответ
        пользователю со статусом 400 и сообщением, что количество слов
        не может быть отрицательным числом.
        """
        words_amount = request.args.get(
            'quantity',
            int(os.getenv('DEFAULT_WORDS_QUANTITY')),
            type=int
        )
        print(self.logger)
        if words_amount < 0:
            self.logger.info('Wrong words quantity %s' % words_amount)
            raise ValueError("Words quantity can't be a negative number %s" % words_amount)
        return words_amount
