from pathlib import Path
from typing import TypedDict

from configuration.config import Settings


class WordsConfig(TypedDict):
    DEFAULT_QUANTITY: int
    DEFAULT_LANGUAGE: str


class FilesConfig(TypedDict):
    ru: str
    eng: str


class JsonConfig(TypedDict):
    WORDS: WordsConfig
    FILES: FilesConfig


class CustomSettings(Settings):
    BASE_DIR: Path
    json: JsonConfig
