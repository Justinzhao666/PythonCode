#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

import logging; logging.basicConfig(level=logging.INFO)
import asyncio
from aiohttp import web
from .Dec import get
from .models import User

# def index(request):
#     # 编码问题，只有body的话可能提示下载文件，而不是打开一个网页  需要向浏览器反馈这个是个html：content_type='text/html'
#     return web.Response(body=b'Awesome', content_type='text/html', charset='UTF-8')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    # app.router 当遇到get 并且路径为/ 的时候，使用index来返回
    app.router.add_route('Get','/',index)
    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000) #开启服务是耗时的操作交给后台处理，这个yield from就是交给后台
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

@get('/')
def index(request):
    users = yield from User.findAll()
    return {
        #'__template__'指定的模板文件是test.html，其他参数是传递给模板的数据，所以我们在模板的根目录templates下创建test.html
        '__template__': 'test.html',
        'users': users
    }

#遇到耗时操作就扔到后面去执行
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()