import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*kw, **kwargs):
        print('call %s()' % func.__name__)
        return func(*kw, **kwargs)

    return wrapper


@log
def now():
    print('2000-1-1')


# 相当于log(now)

now()
print('======================')


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*kw, **kwargs):
            print('call %s():%s' % (func.__name__, text))
            return func(*kw, **kwargs)

        return wrapper

    return decorator


@log('execute')
def now():
    print('2000-1-1')


now()
print(now.__name__)

# 相当于now = log('execute')(now)

print('======================练习===============')
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time


def metric(fn):
    def wrapper(*kw, **kwargs):
        start = time.time()
        a = fn(*kw, **kwargs)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, end - start))
        return a
    return wrapper
@metric
def my_func():
    time.sleep(0.1)

my_func()

print('==================练习2===================')

def log(text=''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*kw, **kwargs):
            print('call %s():%s' % (func.__name__, text))
            return func(*kw, **kwargs)

        return wrapper

    return decorator


@log()
def now():
    print('2000-1-1')

now()