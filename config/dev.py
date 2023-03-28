# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : dev.py
@Project  : WebTest
@Time     : 2023/3/28 14:24
@Author   : Zhao Hexin
@Software : PyCharm
@License  : (C)Copyright 2023-2028, Taogroup-NLPR-CASIA
@Last Modify Time      @Version     @Desciption
--------------------   --------     -----------
2023/3/28 14:24          1.0            None

dev 环境配置
"""
import os

# import sentry_sdk
# from sentry_sdk.integrations.sanic import SanicIntegration

from .base import *

DEBUG = True
ACCESS_LOG = True

DB_URL = os.getenv(
    "DB_URL",
    "mysql://root:password@host:3306/db_name?charset=utf8mb4")

REDIS_URL = os.getenv("REDIS_URL", "redis://127.0.0.1:6379")

TORTOISE_ORM = {
    "connections": {"default": DB_URL},
    "apps": {
        "models": {
            "models": ["aerich.models"] + [app + ".models" for app in APPLICATIONS],  # noqa
            "default_connection": "default",
        },
    },
}

# start sentry
# 异常捕获
# sentry_sdk.init(
#     dsn="http://*****",
#     integrations=[SanicIntegration()],
#     environment="dev",
#     traces_sample_rate=1.0,
#     send_default_pii=True
# )
