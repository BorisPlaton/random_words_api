from flask import jsonify
from flask_restful import Resource

from config.settings import BASE_DIR
from utils.mixins import LoggerMixin


class BaseView(Resource, LoggerMixin):
    """Базовый View-класс."""

    log_file = BASE_DIR / 'logs' / 'base_logs.log'

    def dispatch_request(self, *args, **kwargs):
        try:
            response = super().dispatch_request(*args, **kwargs)
        except Exception as e:
            self.logger.exception(str(e))
            response = jsonify(
                error=str(e),
                status_code=400,
            )

        return response
