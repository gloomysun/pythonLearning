# 删掉偶数
def is_odd(n):
    return n % 2 == 1


r = list(filter(is_odd, list(range(10))))
print(r)
# 删掉序列的空字符串
r = list(filter(lambda x: x != " ", 'adf dfa da'))
print(r)


# 用filter求素数

def _odd_iter():
    n = 3
    while True:
        yield n
        n = n + 2


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = list(_not_divisible(n), it)


# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    return str(n) == str(n)[::-1]
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')