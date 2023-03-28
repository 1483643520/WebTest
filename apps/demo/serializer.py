# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : serializer.py
@Project  : WebTest
@Time     : 2023/3/28 15:14
@Author   : Zhao Hexin
@Software : PyCharm
@License  : (C)Copyright 2023-2028, Taogroup-NLPR-CASIA
@Last Modify Time      @Version     @Desciption
--------------------   --------     -----------
2023/3/28 15:14          1.0            None

序列化
"""
from utils.serializer import ReadOnlyModelSer


class DemoUserSer(ReadOnlyModelSer):
    class Meta:
        fields = ["id", "name", ]
