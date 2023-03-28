# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : models.py
@Project  : WebTest
@Time     : 2023/3/28 15:11
@Author   : Zhao Hexin
@Software : PyCharm
@License  : (C)Copyright 2023-2028, Taogroup-NLPR-CASIA
@Last Modify Time      @Version     @Desciption
--------------------   --------     -----------
2023/3/28 15:11          1.0            None

数据库模型
"""
from datetime import timedelta

from tortoise import Model, fields

# class DemoUser(Model):
#     name = fields.CharField(50)
#
#     is_del = fields.BooleanField(default=False, description="tombstoned")
#     create_time = fields.DatetimeField(auto_now_add=True)
#     update_time = fields.DatetimeField(auto_now=True)
#
#     def __str__(self):
#         return f"I am {self.name}"
