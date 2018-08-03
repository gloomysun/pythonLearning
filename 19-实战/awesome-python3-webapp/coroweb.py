#!/usr/bin/env python
# encoding: utf-8
'''
@file: coroweb.py
@time: 2018/8/3 15:13
@desc:
'''
import logging;

logging.basicConfig(level=logging.INFO)
import functools, asyncio, inspect


def get(path):
    '''
    Define decorator @get('/path)
    '''

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)

        wrapper.__methos__ = 'GET'
        wrapper.__route__ = path
        return wrapper

    return decorator


def post(path):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)

        wrapper.__method__
        'POST'
        wrapper.__route__ = path
        return wrapper

    return decorator


def has_var_kw_arg(fn):
    '有'
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            return True

def has_request_arg(fn):
    sig = inspect.signature(fn)
    params = sig.parameters
    found = False
    for name, param in params.items():
        if name == 'request':
            found = True
            continue  # 退出本次循环
        if found and (
                param.kind != inspect.Parameter.VAR_POSITIONAL and param.kind != inspect.Parameter.KEYWORD_ONLY and param.kind != inspect.Parameter.VAR_KEYWORD):
            raise ValueError(
                'request parameter must be the last named parameter in function: %s%s' % (fn.__name__, str(sig)))


class RequestHandler():
    '''
    RequestHandler是一个类，由于定义了__call__()方法，因此可以将其实例视为函数。
    RequestHandler目的就是从URL函数中分析其需要接收的参数，从request中获取必要的参数，调用URL函数，然后把结果转换为web.Response对象，这样，就完全符合aiohttp框架的要求：
    '''

    def __init__(self, app, fn):
        self._app = app
        self._func = fn

    async def __call__(self, request):
        kw = None

        r = await self._func(**kw)
        return r


def add_route(app, fn):
    '''注册一个URL处理函数：'''
    method = getattr(fn, '__method__', None)
    path = getattr(fn, '__route__', None)
    if path is None or method is None:
        raise ValueError('@get or @post not defined in %s.' % str(fn))
    if not asyncio.iscoroutinefunction(fn) and not inspect.isgeneratorfunction(fn):
        fn = asyncio.coroutine(fn)
    logging.info(
        'add route %s %s => %s(%s)' % (method, path, fn.__name__, ', '.join(inspect.signature(fn).parameters.keys())))
    app.router.add_route(method, path, RequestHandler(app, fn))


def add_routes(app, module_name):
    n = module_name.rfind('.')
    if n == '-1':
        mod = __import__(module_name, globals(), locals())
    else:
        name = module_name[n + 1:]
        mod = getattr(__import__(module_name[:n], globals(), locals(), [name]), name)
        ''' __import__() 函数用于动态加载类和函数 。如果一个模块经常变化就可以使用 __import__() 来动态载入。'''
    for attr in dir(mod):
        if attr.startswith('_'):
            continue
        fn = getattr(mod, attr)
        if callable(fn):
            method = getattr(fn, '__method__', None)
            path = getattr(fn, '__route__', None)
        if method and path:
            add_route(app, fn)


@get('/')
def test():
    pass
