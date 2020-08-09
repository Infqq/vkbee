# Longpoll
## Bot Longpoll
```python
async for event in longpoll.events():
    user_id = event['object']['message']['from_id']
    message_text = event['object']['message']['text']
```

## User Longpoll
```python
from vkbee.user_events import get_event
...
async for event in longpoll.events():
```