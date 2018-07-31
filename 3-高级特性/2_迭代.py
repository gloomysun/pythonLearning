d = {'a': 1, 'b': 2, 'c': 3}

for a in d.items():
    print(a)
from collections import Iterable

print(isinstance('abc', Iterable))

for i, value in enumerate(d):
    print(i, value)
print('====================练习=====================')


# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if L == []:
        return (None, None)
    else:
        min = max = L[0]
        for x in L:
            if x < min:
                min = x
            if x > max:
                max = x
        return (min, max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
