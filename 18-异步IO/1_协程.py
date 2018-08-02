'''
协程 Coroutine
python对协程的支持是通过generator实现的
'''


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[consumer] consuming %s' % n)
        r = '200 OK'


def producer(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('[producer] produce %s' % n)
        r = c.send(n)
        print('[producer] consumer returns %s' % r)
    c.close()


c = consumer()
producer(c)
