# Быстрый старт
## Подключение VKBee
```python
import asyncio
import vkbee
```

## Авторизация
 - ## Для работы с API
 ```python
from vkbee import API
async def main(loop):
    vk = API(token='token', loop=loop)
  ```
### Разбор аргументов
| Параметр | Описание |
| -------- | ---------|
| token | Ключ доступа
| loop  | Цикл событий

 - ## Для работы с Longpoll
 ```python
from vkbee.longpoll import BotLongpoll, Session
async def main(loop):
    vk = Session(token='token', loop=loop)
    longpoll = BotLongpoll(vk_session, groupid, wait)
  ```
### Разбор аргументов
| Параметр | Описание |
| -------- | ---------|
| token | Ключ доступа
| loop  | Цикл событий
| vk_session | Сессия
| groupid  | Числовой идентификатор сообщества
| wait | Время жизни запроса обновлений новых событий (в секундах, рекомендуется 10)
