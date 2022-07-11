import os
import random

from config.settings import BASE_DIR


class WordsHandler:
    """Класс, который отвечает за работу со словами из файла."""

    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def get_words_from_file(self, amount) -> list[str]:
        """
        Возвращает список слов длинной `amount` из файла,
        путь к которому указан в атрибуте `path_to_file`.
        """
        with open(self.path_to_file, encoding='utf-8') as input_file:
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

        elements_amount = 0
        elements_list = []

        while elements_amount < amount:
            elements_list.append(random.choice(items_list))
            elements_amount += 1

        return elements_list


words_file = WordsHandler(BASE_DIR / os.getenv('FILE_LOCATION'))
