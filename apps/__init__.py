# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : __init__.py.py
@Project  : WebTest
@Time     : 2023/3/28 14:47
@Author   : Zhao Hexin
@Software : PyCharm
@License  : (C)Copyright 2023-2028, Taogroup-NLPR-CASIA
@Last Modify Time      @Version     @Desciption
--------------------   --------     -----------
2023/3/28 14:47          1.0            None

app 注册
"""
from importlib import import_module

import aioredis
from sanic import Blueprint, Sanic
from tortoise.contrib.sanic import register_tortoise


def get_blueprint_group(apps):
    bp_list = []
    for app in apps:
        bp_module = import_module(app + ".urls")
        bp_list.append(getattr(bp_module, "bp"))

    return Blueprint.group(*bp_list)


async def before_server_start(app, loop):
    await app.ctx.redis.ping()


def create_app(config):
    app = Sanic("ID_Photo_Overseas")
    # load settings
    app.update_config(config)

    # load db settings
    register_tortoise(
        app, db_url=app.config.DB_URL,
        modules={"models": [app + ".models" for app in app.config.APPLICATIONS]},  # noqa
        generate_schemas=app.config.DEBUG  # create tables before server start
    )

    # load cache
    app.ctx.redis = aioredis.from_url(
        app.config.REDIS_URL,
        password=app.config.REDIS_PASSWD,
        encoding="utf-8",
        decode_responses=True)
    app.register_listener(before_server_start, "before_server_start")

    # load static files
    app.static("/static", "./static")

    # load blueprints
    app.blueprint(get_blueprint_group(app.config.APPLICATIONS))

    # load middleware
    # app.register_middleware(check_market_from, "request")

    return app
