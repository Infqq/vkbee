# Users.get method test

import vkbee
import asyncio
import time

async def main(loop):
    vk = vkbee.VkApi(
        "6487ed076487ed076487ed07bc64e85d05664876487ed073ac28c0f3ba125e9cac51fb3",
        loop=loop,
        )

    start = time.time()

    await vkbee.VkApi.call(vk, "users.get", {"user_id": 1})

    stop = time.time()

    speed = stop - start

    print(speed)

    exit()

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
