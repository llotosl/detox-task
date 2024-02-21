# detox-task

Это реализация системы для оценки токсичности сообщений пользователей и модерации сообщений по этим данным.

## Архитектура сервиса
![test.drawio.png](static%2Ftest.drawio.png)

Наш сервис получает сообщения по какому-то брокеру, обрабатывает их c помощью ML-модели и отправляет в БД.
Консьюмеров может быть большое количество, что обеспечит масштабируемость.

К тому же наш сервис позволяет получить модератору все оценки и тексты сообщений и забанить отправителей этих сообщений
после проверки. После бана сообщение об этом уходит в сервис развлечений(Twitch, YouTube и т.д.).

Я бы подумал над выделением ML-модели в отдельный сервис(Moderation и Processing сервисы отдельно),
взвесил все за и против, но не стал этим заниматься, так как это тестовое задание.


## Что было реализовано
Я реализовал использование встроенных очередей (queue.Queue) вместо брокера и консьюмер для этой очереди с ml-моделью.

Реализовал поддержку in-memory базы данных для сохранения оценок сообщений вместо настоящей БД.

Реализовал in-memory кеширование вместо использования настоящих инструментов.

Реализовал эндпоинт для получения оценок.

## Что можно улучшить
Добавить эндпоинт для бана юзера, заменить in-memory решения на подходящие технологии, разделить запуск консьюмера и
FastAPI-приложения на разные контейнеры(сейчас они в одном процессе с помощью ThreadPoolExecutor из-за
in-memory решений), .env-настройки, добавить тесты в код, авторизация и аутентификация,
настройки логирования + TODO в коде.

Зная, что в будущем нужно заменить in-memory решения на другие, я заранее сделал интерфейсы и использовал только их в
коде консьюмера и эндпоинта

## Код
[Консьюмер](./src/detox_task/application/score_message_consumer/consumer.py)

[Эндпоинт для получения оценок](./src/detox_task/adapters/fapi/scores/router.py)

[Запуск консьюмера и FastAPI-приложения](./src/detox_task/__main__.py)


## Запуск
```shell
docker build --tag 'detox_task' .
docker run -p 8000:8000 'detox_task'
```

## Использование
При запуске приложения в очередь автоматически отправляются 5 сообщений, так что по эндпоинту
[/scores](http://127.0.0.1:8000/scores) можно получить 5 результатов. Отправить запрос можно через
[swagger](http://127.0.0.1:8000/docs)
