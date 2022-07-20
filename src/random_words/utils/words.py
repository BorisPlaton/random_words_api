import random

from configuration import settings


class WordFile:
    """Файл со словами."""

    def get_words_from_file(self, amount) -> list[str]:
        """
        Возвращает список слов, на языке `language`, длинной `amount`
        из файла, путь к которому указан в атрибуте `path_to_file`.
        """
        with open(self.path_to_file) as input_file:
            all_words_list = input_file.read().split()

        return self.get_random_elements(amount, all_words_list)

    @staticmethod
    def get_random_elements(amount: int, items_list: list | tuple) -> list:
        """
        Возвращает список случайных элементов длинной `amount`
        из списка `items_list`.
        """
        if not isinstance(amount, int):
            raise ValueError("Количество слов `amount` не может быть типа %s." % type(amount))
        if amount < 0:
            raise ValueError("Количество слов `amount` не может быть %s." % amount)

        if not isinstance(items_list, list | tuple):
            raise ValueError("`items_list` должен быть списком или кортежем, но не %s" % type(items_list))

        if amount >= len(items_list):
            return items_list

        return [random.choice(items_list) for _ in range(amount)]

    def __init__(self, path_to_file):
        """Устанавливает путь к файлу со словами."""
        self.path_to_file = path_to_file


class WordsHandler:
    """Класс, который отвечает за работу с файлами слов."""

    def set_words_files(self, words_files: dict):
        """
        Устанавливает файлы и их языки в атрибут экземпляра
        класса `self.words_files`.
        """
        for language, path_to_file in words_files.items():
            self.words_files[language] = WordFile(settings.BASE_DIR / path_to_file)

    def __init__(self, words_files: dict = None):
        """
        Устанавливает файлы и их языки в атрибут экземпляра
        класса `self.words_files`, если `words_files` не `None`.
        """
        self.words_files: dict[str, WordFile] = {} if not words_files else self.set_words_files(words_files)

    def __getitem__(self, item: str) -> WordFile:
        """
        Возвращает файл со словами в зависимости от языка,
        который передаётся в аргумент `item`.
        """
        return self.words_files[item]


words_file = WordsHandler()
