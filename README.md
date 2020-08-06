<head>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
</head>

![vkbee](https://github.com/UHl0aG9uZWVy/vkbee/raw/master/logo.png)

[VK chat](https://vk.me/join/AJQ1d0zSjRa17i3RkVt3m5KH)

<p align="center">
    <img alt="Made with Python" src="https://img.shields.io/badge/Made%20with-Python-%23FFD242?logo=python&logoColor=white">
    <img alt="Downloads" src="https://pepy.tech/badge/vkbee">
</p>




# vkbee

## Установка
```bash
pip3 install vkbee
```


## Пример работы
```python
import asyncio
import vkbee

from vkbee import oldlong

async def main(loop):
    token = 'token'
    vk = oldlong.VkApi(token=token, loop=loop)
    longpoll = oldlong.BotLongpoll(vk, 'groupid', 10)

    for event in longpoll.events():
        user_id = event['object']['message']['from_id']
        message_text = event['object']['message']['text']
        await vkbee.VkApi.call(vk, 'messages.send', {'user_id': user_id, 'message': message_text, 'random_id': 0})

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
```