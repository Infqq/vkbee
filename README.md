![vkbee](https://github.com/asyncvk/vkbee/blob/master/vkbee/bgtio.png?raw=true)
# vkbee
Simple Async VKLibrary faster than vk_api
```python
import aiohttp
import asyncio
import vkbee
import time
import datetime

async def main(loop):
    token = "tokenhere"
    vk = vkbee.VkApi(token, loop=loop)
    delta = datetime.timedelta(hours=8, minutes=0)  # ðàçíèöà îò UTC. Ìîæåòå âïèñàòü ëþáîå çíà÷åíèå âìåñòî 3
    t = (datetime.datetime.now(datetime.timezone.utc) + delta)  # Ïðèñâàèâàåì äàòó è âðåìÿ ïåðåìåííîé «t»
    nowtime = t.strftime("%H:%M")  # òåêóùåå âðåìÿ
    nowdate = t.strftime("%d.%m.%Y")  # òåêóùàÿ äàòà
    none={}
    on = await vkbee.VkApi.call(vk,"friends.getOnline",none)
    counted = len(on)  # ñ÷èòàåì êîë-âî ýëåìåíòîâ â ñïèñêå

    data = {
        'text':'VKBee: '+nowtime + " ? " + nowdate + " ? " + "Äðóçåé îíëàéí: " + str(counted)
    }
    while True:
        a=await vkbee.VkApi.call(vk,'status.set',data)
        print(a)
        time.sleep(1)
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))

```
