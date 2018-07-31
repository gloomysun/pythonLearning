L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L[:1])
print(L[-2:])

L = list(range(100))
print(L)
print(L[:10])
print(L[:10:2])

s = 'abcdefg'
print(s[-1:])
print(s[::2])


print('====================练习=====================')


# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    if s[:1] == " ":
        return trim(s[1:])
    elif s[-1:] == " ":
        return trim(s[:-1])
    else:
        return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
