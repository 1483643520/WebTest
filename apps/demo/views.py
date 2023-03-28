# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : views.py
@Project  : WebTest
@Time     : 2023/3/28 15:11
@Author   : Zhao Hexin
@Software : PyCharm
@License  : (C)Copyright 2023-2028, Taogroup-NLPR-CASIA
@Last Modify Time      @Version     @Desciption
--------------------   --------     -----------
2023/3/28 15:11          1.0            None

视图执行
"""
# from sanic.views import HTTPMethodView
#
# from utils.decorators import param_check
# from utils.response import general_json_res
#
# from . import serializers
# from .models import DemoUser
#
#
# class UserView(HTTPMethodView):
#     """restful接口实例"""
#
#     async def get(self, request, pk=0):
#         if not pk:
#             users = await DemoUser.all()
#             ser = await serializers.DemoUserSer(users, many=True).data
#             return general_json_res(users=ser)
#
#         # 推荐使用 get_or_none 获取唯一的单个对象
#         user = await DemoUser.get_or_none(pk=pk)
#         if user:
#             ser = await serializers.DemoUserSer(user).data
#             return general_json_res(user=ser)
#         return general_json_res(404, "no user.")
#
#     @param_check({"name", })
#     async def post(self, request, pk=0):
#         name = request.json.get("name")
#         obj = await DemoUser.create(name=name)
#         return general_json_res(pk=obj.pk)
#
#     async def put(self, request, pk=0):
#         user = await DemoUser.get_or_none(pk=pk)
#         if user:
#             await user.update_from_dict(**request.json)
#             return general_json_res()
#         return general_json_res(404, "no user.")
#
#     async def delete(self, request, pk=0):
#         r = await DemoUser.filter(pk=pk).delete()
#         return general_json_res(r=r)
#
#
# class CacheView(HTTPMethodView):
#     """缓存使用说明，和redis的方法基本一致，具体请参考文档内的教学"""
#
#     async def get(self, request, key):
#         val = await request.app.ctx.redis.get(key)
#         if val:
#             return general_json_res(val=val)
#         return general_json_res(404, "no cache.")
#
#     async def post(self, request, key):
#         val = request.json.get("val")
#         await request.app.ctx.redis.set(key, val, 360)
#         return general_json_res()
#
#     async def delete(self, request, key):
#         await request.app.redis.delete(key)
#         return general_json_res()
