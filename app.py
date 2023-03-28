# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : app.py
@Project  : WebTest
@Time     : 2023/3/28 13:57
@Author   : Zhao Hexin
@Software : PyCharm
@License  : (C)Copyright 2023-2028, Taogroup-NLPR-CASIA
@Last Modify Time      @Version     @Desciption
--------------------   --------     -----------
2023/3/28 13:57          1.0            None
"""

import multiprocessing
import platform
from importlib import import_module

from apps import create_app

SETTINGS_MODULE = "config.dev"
Config = import_module(SETTINGS_MODULE)

app = create_app(Config)


# `workers` is num of subprocesses
def get_workers():
    if not app.config.DEBUG and platform.system() != "Windows":
        return multiprocessing.cpu_count()
    return 1


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        debug=app.config.DEBUG,
        access_log=app.config.ACCESS_LOG,
        workers=get_workers()
    )
