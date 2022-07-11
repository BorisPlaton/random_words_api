import logging


class LoggerMixin:
    """Миксин для работы с логированием."""

    logger_name: str = __name__

    is_stream_handler = False
    stream_log_level: int = logging.WARNING
    stream_log_format: str = "%(asctime)s:%(name)s:%(message)s"

    is_file_handler = True
    file_log_level: int = logging.WARNING
    file_log_format: str = "%(asctime)s:%(name)s:%(message)s"
    log_file = None

    def __init__(self):
        self.logger = self.get_logger()

    def get_logger(self) -> logging.Logger:
        """
        Возвращает экземпляр `logging.Logger`. Добавляет логирование в
        файл, если `is_file_handler` = True. Аналогично с выводом в консоль,
        если атрибут `is_stream_handler` = True.
        """
        logger = logging.getLogger(self.logger_name)

        if self.is_file_handler:
            logger.addHandler(self.get_file_handler())

        if self.is_stream_handler:
            logger.addHandler(self.get_file_handler())

        return logger

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
            self.file_log_level,
        )

    def get_stream_handler(self) -> logging.StreamHandler:
        """Возвращает обработчик вывода в консоль `logging.StreamHandler`."""
        stream_handler = logging.StreamHandler(self.log_file)
        return self.setup_handler(
            stream_handler,
            self.stream_log_format,
            self.stream_log_level,
        )

    def setup_handler(self, handler, handler_log_format: str, log_level: int):
        """Устанавливает стандартные настройки для обработчика."""
        handler.setFormatter(
            self.get_formatter(handler_log_format)
        )
        handler.setLevel(log_level)
        return handler
