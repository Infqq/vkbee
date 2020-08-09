# Вызов методов
## Синтаксис вызова
```python
await API.call(vk_session, 'users.get', {'user_id': 1})
```

### Разбор аргументов
| Параметр | Описание |
| -------- | ---------|
| vk_session | Сессия авторизации ([Авторизация](https://github.com/vkbee/vkbee/blob/master/docs/quick_start.md#авторизация))
| method_name  | Название метода
| data | Параметры запроса (в json)

 Список методов и их параметров имеется в официальной документации ВКонтакте: https://vk.com/dev/methods

## Парсинг ответа
```python
response = await API.call(vk_session, 'users.get', {'user_id': 1})
first_name = response['response']['first_name']
```