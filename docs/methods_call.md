# Вызов методов
 ## API Auth

```python
async def main(loop):
    vk = vk_s.get_api() 
    await vk.messages.send(chat_id=1, message='VKBEE', random_id=0)
```
### Разбор аргументов
| Параметр | Описание |
| -------- | ---------|
| vk | Авторизированный пользователь (сессия)
| vk_s  | Авторизированный пользователь (упрощенная  сессия)
| chat_id | Числовой идентификатор чата для доставки сообщения
| message | Сообщение
| random_id | Рандомный идентификатор (0 - генерация на стороне ВКонтакте

 ## LongPoll Auth
```python
async def main(loop):
    await API.call(vk_session, 'messages.send', {'user_id': user_id, 'message': message_text, 'random_id': 0})
```    
| Параметр | Описание |
| -------- | ---------|
| vk_session | Авторизированный пользователь (сессия)
| json  | Запрос в json



## Парсинг ответа

Буду использовать вариацию с LongPoll Auth

```python
async def main(loop):
    a=await API.call(vk_session, 'messages.send', {'user_id': user_id, 'message': message_text, 'random_id': 0})
    print(a['response'])
```
 В примере мы спарсили ответ response от вызова метода.    
