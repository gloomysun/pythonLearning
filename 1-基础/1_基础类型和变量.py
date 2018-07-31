print('i\'m ok')

# 使用r''表示内部默认不转义
print(r'i\'m ok')
#使用'''...'''表示多行内容
print('''
hello
python
i'am ok
''')

#boolean
print(True)
print(not True)
print(3>2)

a = 'ABC'
b = a
a = 'XYZ'
print(b)


print(10/3)
print(10//3)

print("==============练习======================")
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)