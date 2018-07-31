L = list(range(10))


def f(x):
    return x * x


r = map(f, L)
print(list(r))


def add(x, y):
    return x + y


from functools import reduce

r = reduce(add, L)
print(r)


def fn(x, y):
    return x * 10 + y


r = reduce(fn, 'ab')
print(r)

print('======================练习=============')


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    r = list(map(lambda x: DIGITS[x] if x != '.' else ".", s))
    r1 = reduce(lambda x, y: x * 10 + y, r[:s.index('.')])
    r2 = reduce(lambda x, y: x * 10 + y, r[s.index('.') + 1:])
    return r1 + r2/(pow(10,len(str(r2))))


print(str2float('123.456'))
