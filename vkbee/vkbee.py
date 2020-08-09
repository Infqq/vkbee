# -*- coding: utf-8 -*-
# author: asyncvk

import six
import aiohttp
import requests
import time
import asyncio
import logging

from .exceptions import *

"""
:authors: sergeyfilippov1, YamkaFox
:license: Mozilla Public License, version 2.0, see LICENSE file
:copyright: (c) 2020 asyncvk
"""


class API:
    def __init__(self, token, loop, api_version="5.122"):
        self.error_handlers = {
            TOO_MANY_RPS_CODE: self.async_too_many_rps_handler,
            "NON-ASYNC_RPS": self.rps_handler,
        }

        self.token = token
        self.api_version = api_version

        self.base_url = "https://api.vk.com/method/"
        self.s = aiohttp.ClientSession()

        self.last_request_time = 0
        self.start_time = time.time()
        self.request_count = 0
        self.logger = logging.getLogger("vkbee")

    def rps_handler(self, error):
        self.logger.warning("Too many requests in second!! Sleeping 0.5 secs")

        time.sleep(0.5)
        return error.nonasync_try_method()

    async def async_too_many_rps_handler(self, error):
        """ Обработчик ошибки "Слишком много запросов в секунду".
            Ждет полсекунды и пробует отправить запрос заново
        :param error: исключение
        """

        self.logger.warning("Too many requests in second!! Sleeping 0.5 secs")

        time.sleep(0.5)
        return await error.try_method()

    async def call(self, method_name, data):
        data["access_token"] = self.token
        data["v"] = self.api_version

        url = self.base_url + method_name
        self.request_count += 1

        self.last_request_time = time.time()
        r = await self.s.post(url, data=data)

        r = await r.json()

        if "error" in r:
            error = api_error(self, method_name, data, r["error"])
            if error.code in self.error_handlers:
                response = await self.error_handlers[error.code](error)
                if response is not None:
                    return response
            raise error
        else:
             return r       
            

        return r

    def sync_call(self, method_name, data):
        data["access_token"] = self.token
        data["v"] = self.api_version

        url = self.base_url + method_name
        r = requests.post(url, data=data).json()

        if "error" in r:
            error = api_error(self, method_name, data, r["error"])
            if error.code == 6:
                response = self.error_handlers["NON-ASYNC_RPS"](error)

                if response is not None:
                    return response

            raise error

        return r["response"]