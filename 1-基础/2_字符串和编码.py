print('包含中文的str')

# bytes
print(b'ABC')

# encode
print('ABC'.encode('ascii'))
print('ABC'.encode('utf-8'))
print('中文'.encode('utf-8'))

# decode
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96'.decode('utf-8', errors='ignore'))

print(len('中文'))
print(len('中文'.encode('utf-8')))
# 格式化
print('你好，本月话费%s' % 100)
print('hello,%s' % 'zjag')
print('%20d-%04d' % (3, 1))
print("==============练习======================")
s1 = 72
s2 = 85
r = (85 - 72) / 72 * 100
print('成绩提升了%.1f %%' % r)
