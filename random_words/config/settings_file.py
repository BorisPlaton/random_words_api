import json

from . import settings as st


class Settings:
    """Класс для получения значений из `config.settings`."""

    def setup_config_from_settings(self):
        """Устанавливает значения констант из `configuration.settings`."""
        for constant in self._config_list:
            setattr(self, constant, getattr(st, constant))

    def load_config_file(self, path_to_config):
        """Читает данные из конфигурационного json-файла."""
        with open(path_to_config) as config_file:
            self.config = json.load(config_file)

    def __init__(self):
        """
        Загружает значения и устанавливает их как атрибуты класса из
        `settings.py` файла.
        """
        self.config = {}
        self._config_list = [
            constant for constant in dir(st) if not constant.startswith('__')
        ]  # Не берёт во внимание переменные файла `settings.py`, к примеру  `__file__`, `__name__` и т.д.
        self.setup_config_from_settings()

    def __getitem__(self, item):
        """Возвращает значение из json-файла конфига."""
        return self.config[item]


settings = Settings()
