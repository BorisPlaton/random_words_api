from flask import jsonify
from flask_restful import Resource

from configuration import settings
from random_words.utils.mixins import LoggerMixin


class BaseView(Resource, LoggerMixin):
    """Базовый View-класс."""

    log_file = settings.BASE_DIR / 'logs' / 'base_logs.log'

    def dispatch_request(self, *args, **kwargs):
        """
        Если происходит ошибка, то логируем её и отправляем
        приемлемый ответ пользователю.
        """
        try:
            response = super().dispatch_request(*args, **kwargs)
        except Exception as e:
            self.logger.exception(str(e))
            response = jsonify(
                error=str(e),
                status_code=400,
            )

        return response
