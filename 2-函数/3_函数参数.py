# 位置参数
def power(x, n):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s


print(power(2, 3))


# 默认参数
# 默认参数必须指向不可变对象
def power(x, n=2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s


print(power(2))


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())
print(add_end())


# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum


print(calc(1, 2, 3))
t = (1, 2, 3)
print(calc(*t))


# 关键字参数
def person(name, age, **kw):
    print('name:%s,age:%s,kw:%s' % (name, age, kw))


person('xi', 10, city='tianjin')


# 命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')

# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

print('====================练习=====================')


# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(*args):
    if not len(args):
        raise TypeError
    else:
        s = 1
        for x in args:
            s = s * x
        return s

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')