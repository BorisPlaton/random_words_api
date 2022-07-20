import logging


class LoggerMixin:
    """Миксин для работы с логированием."""

    logger_name: str = __name__
    logger_level: int = logging.WARNING

    is_file_handler = True
    file_log_format: str = "[%(asctime)s in %(name)s.%(funcName)s] - %(message)s"
    log_file = None

    is_stream_handler = False
    stream_log_format: str = "[%(asctime)s in %(name)s.%(funcName)s] - %(message)s"

    def set_logger(self):
        """
        Возвращает экземпляр `logging.Logger`. Добавляет логирование в
        файл, если `is_file_handler` = True. Аналогично с выводом в консоль,
        если атрибут `is_stream_handler` = True.
        """
        logger = logging.getLogger(self.logger_name)
        logger.setLevel(self.logger_level)

        if self.is_file_handler:
            logger.addHandler(self.get_file_handler())

        if self.is_stream_handler:
            logger.addHandler(self.get_stream_handler())

    @property
    def logger(self):
        logger_instance = logging.getLogger(self.logger_name)

        if not logger_instance.hasHandlers():
            self.set_logger()

        return logger_instance

    @staticmethod
    def get_formatter(log_format: str) -> logging.Formatter:
        """Возвращает `logging.Formatter`, с форматом сообщения `log_format`."""
        formatter = logging.Formatter(log_format)
        return formatter

    def get_file_handler(self) -> logging.FileHandler:
        """Возвращает обработчик файла `logging.FileHandler`."""
        file_handler = logging.FileHandler(self.log_file)
        return self.setup_handler(
            file_handler,
            self.file_log_format,
        )

    def get_stream_handler(self) -> logging.StreamHandler:
        """Возвращает обработчик вывода в консоль `logging.StreamHandler`."""
        stream_handler = logging.StreamHandler()
        return self.setup_handler(
            stream_handler,
            self.stream_log_format,
        )

    def setup_handler(self, handler, handler_log_format: str):
        """Устанавливает стандартные настройки для обработчика."""
        handler.setFormatter(
            self.get_formatter(handler_log_format)
        )
        handler.setLevel(self.logger_level)
        return handler
