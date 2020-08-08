# Быстрый старт
## Подключим модуль vkbee и вспомогательные модули
```python
import asyncio
import vkbee
```

# Авторизация
 - ## Для работы с API
 ```python
from vkbee import API
async def main(loop):
    vk=API(token='token', loop=loop)
  ```
### Разбор аргументов
| Параметр | Описание |
| -------- | ---------|
| token | Ключ для доступа к вашему аккаунту
| loop  | Ваш event-loop для привязки к нему
 - ## Для работы с LongPoll
 ```python
from vkbee import API
from vkbee.longpoll import BotLongpoll, Session
async def main(loop):
    vk=Session(token='token', loop=loop)
    longpoll = BotLongpoll(vk_session, groupid, timespeak)
  ```
### Разбор аргументов
| Параметр | Описание |
| -------- | ---------|
| token | Ключ для доступа к вашему аккаунту
| loop  | Ваш event-loop для привязки к нему
| vk_session | Ваша сессия созданная строкой выше
| groupid  | Числовой идентификатор сообщества для подключения бота (строка)
| timespeak | Время жизни запроса обновлений новых событий (в сек, желательно 10)
