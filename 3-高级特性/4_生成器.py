L = (x * x for x in range(1, 100))
print(L)


def fib(max):
    n, a, b = 0, 1, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


g = fib(10)
while True:
    try:
        next(g)
    except StopIteration as e:
        print(e.value)
        break
print('====================练习=====================')


# 杨辉三角定义如下：
#
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list：
def triangles():
    L = [1]
    yield L
    while True:
        L = L + [0]
        L = [L[n - 1] + L[n] for n in range(len(L))]
        yield L


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break

