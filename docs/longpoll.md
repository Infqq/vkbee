# Longpoll
## Bot Longpoll
```python
async for event in longpoll.events():
    user_id = event['object']['message']['from_id']
    message_text = event['object']['message']['text']
```

## User Longpoll
```python
import vkbee.user_events
...
async for event in longpoll.events():
    event_type = get_event_type(event)
```