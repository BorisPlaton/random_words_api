# API случайных слов

Возвращает список случайных слов в виде `json`. 
Слова могут быть на русском или английском языке в зависимости от параметра `lang`. Допустимые значения:
- `ru` - русский
- `eng` - английский

Количество слов слов можно изменить с помощью параметра `quantity`. Не должен быть меньше 0.

## Запуск
Проект имеет `Dockerfile` и `docker-compose` файлы. Чтобы запустить на `5050` порту введите следующую команду:
```
$ docker-compose up
```
## Примеры запроса/ответа
```console
$ curl http://127.0.0.1:5050/?quantity=5
{
    "words": [
        "сразу",
        "мир",
        "совсем",
        "остаться",
        "об"
    ]
}
```
```console
$ curl 'http://127.0.0.1:5050/?quantity=2&lang=eng'
{"words": ["bright", "agreement"]}
```
```console
$ curl http://127.0.0.1:5050/?lang=pol
{"error": "Incorrect language - `pol`. Only `ru`, `eng` are available."}
```
```console
$ curl http://127.0.0.1:5050/?quantity=-2
{"error": "Words quantity can't be a negative number `-2`"}
```