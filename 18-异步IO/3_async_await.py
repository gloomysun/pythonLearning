'''
用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，然后在coroutine内部用yield from调用另一个coroutine
实现异步操作

请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
把@asyncio.coroutine替换为async；
把yield from替换为await。
'''
import asyncio

@asyncio.coroutine
def test():
    n = 1
    for i in range(50000000):
        n = n + i
    return n


async def hello():
    print('Hello, world!')
    r = await test()
    print('Hello, again %s' % r)
#
# t= test()
# for x in t:
#     print(x)
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
