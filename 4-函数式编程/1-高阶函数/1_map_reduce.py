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
    return x*10 + y


r = reduce(fn, 'ab')
print(r)

