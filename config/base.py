# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File     : base.py
@Project  : WebTest
@Time     : 2023/3/28 14:20
@Author   : Zhao Hexin
@Software : PyCharm
@License  : (C)Copyright 2023-2028, Taogroup-NLPR-CASIA
@Last Modify Time      @Version     @Desciption
--------------------   --------     -----------
2023/3/28 14:20          1.0            None

sanic 默认配置
"""
"""
内置配置(Builtin values)
变量名称	默认值	说明
REQUEST_MAX_SIZE	100000000	Request 的最大字节数
REQUEST_BUFFER_QUEUE_SIZE	100	请求流缓冲区队列大小
REQUEST_TIMEOUT	60	请求超时时间
RESPONSE_TIMEOUT	60	响应超时时间
KEEP_ALIVE	True	是否启用长连接
KEEP_ALIVE_TIMEOUT	5	长连接超时时间
WEBSOCKET_MAX_SIZE	2^20	websocket 传入消息最大字节数
WEBSOCKET_MAX_QUEUE	32	websocket 传入消息最小字节数
WEBSOCKET_READ_LIMIT	2^16	websocket 传入字节的缓冲区上限
WEBSOCKET_WRITE_LIMIT	2^16	websocket 传出字节的缓冲区上限
WEBSOCKET_PING_INTERVAL	20	websocket ping 帧 发送间隔
WEBSOCKET_PING_TIMEOUT	20	websocket pong 帧 响应超时时间
GRACEFUL_SHUTDOWN_TIMEOUT	15.0	强制关闭非空闲连接超时时间
ACCESS_LOG	True	访问日志开关
FORWARDED_SECRET	None	用于安全地识别特定的代理服务器（见下文）
PROXIES_COUNT	None	应用程序钱代理服务器的数量（见下文）
FORWARDED_FOR_HEADER	X-Forwarded-For	客户端IP和代理IP：X-Forwarded-For
REAL_IP_HEADER	None	客户端真实IP： X-Real-IP

如果您处于 ASGI 模式， 那么 WEBSOCKET_ 的值将会被忽略
"""

SECRET_KEY = '!()bygw+chvo+2sf0&$z(-ep=1jsk@4e%8g@bz3l$cv+2)u%&a'

# app注册
APPLICATIONS = [
    "apps.demo",
]

REDIS_PASSWD = ""
