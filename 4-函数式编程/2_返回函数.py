def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


print(lazy_sum(1, 2, 3)())

print('======================练习======================')


def createCounter():
    n = 0
    def counter():
        nonlocal n
        n += 1
        return n

    return counter

#
# print(createCounter()())
# print(createCounter()())
# print(createCounter()())

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')