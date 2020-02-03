![vkbee](https://raw.githubusercontent.com/asyncvk/vkbee/master/bg.png)
# vkbee
Simple Async VKLibrary faster than vk_api
```python
import aiohttp
import asyncio
import longpoll
import api
import time



import aiohttp
import asyncio
import vkbee
import time
import datetime

async def main(loop):
    token = "tokenhere"
    vk = vkbee.VkApi(token, loop=loop)
    delta = datetime.timedelta(hours=8, minutes=0)  # разница от UTC. Можете вписать любое значение вместо 3
    t = (datetime.datetime.now(datetime.timezone.utc) + delta)  # Присваиваем дату и время переменной «t»
    nowtime = t.strftime("%H:%M")  # текущее время
    nowdate = t.strftime("%d.%m.%Y")  # текущая дата
    none={}
    on = await vkbee.VkApi.call(vk,"friends.getOnline",none)
    counted = len(on)  # считаем кол-во элементов в списке

    data = {
        'text':'VKBee: '+nowtime + " ? " + nowdate + " ? " + "Друзей онлайн: " + str(counted)
    }
    while True:
        a=await vkbee.VkApi.call(vk,'status.set',data)
        print(a)
        time.sleep(1)
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))

```
