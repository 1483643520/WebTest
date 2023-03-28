# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : urls.py
@Project  : WebTest
@Time     : 2023/3/28 15:08
@Author   : Zhao Hexin
@Software : PyCharm
@License  : (C)Copyright 2023-2028, Taogroup-NLPR-CASIA
@Last Modify Time      @Version     @Desciption
--------------------   --------     -----------
2023/3/28 15:08          1.0            None

app内url注册
"""
from sanic import Blueprint

from . import views

bp = Blueprint("demo", url_prefix="/demo")

# load blueprint request middleware
# from utils import middlewares
# bp.on_request(middlewares.check_user)
