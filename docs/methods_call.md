# Вызов методов
 ## При авторизации для работы с API

```python
async def main(loop):
    vk = vk_s.get_api() 
    await vk_s.messages.send(chat_id=1, message='VKBEE', random_id=0)
```

 ## При авторизации для работы с LongPoll
```python
async def main(loop):
    await API.call(vk_session, 'messages.send', {'user_id': user_id, 'message': message_text, 'random_id': 0})
```    



## Парсинг ответа

TODO
