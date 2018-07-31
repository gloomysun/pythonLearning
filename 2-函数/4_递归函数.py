def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(1))


# 栈溢出print(fact(1000))
# 尾递归优化
# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。
def fact_iter(n, product=1):
    if n == 1:
        return product
    else:
        return fact_iter(n - 1, n * product)
print('====================练习=====================')

# 汉诺塔的移动可以用递归函数非常简单地实现。

# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        print(a, '-->', c)
        move(n - 1, b, a, c)

move(3, 'A', 'B', 'C')