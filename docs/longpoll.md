# Longpoll
## Bot Longpoll
```python
async for event in longpoll.events():
    user_id = event['object']['message']['from_id']
    message_text = event['object']['message']['text']
```

## User Longpoll
```python
from vkbee import API
...
async for event in longpoll.events():
    event_type = API.getEventType(event[0])
    if event_type == 'ADD_NEW_MESSAGE':
        user_id = event[3]
        message_text = event[6]
```

Типы событий и их структура описаны в официальной документации ВКонтакте: https://vk.com/dev/using_longpoll_2