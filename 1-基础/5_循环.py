names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# for in 循环
sum = 0
for x in range(10):
    sum = sum + x
print(sum)
# while 循环
sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n - 1
print(sum)
print('==============练习===================')
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('Hello,%s' % x)

n = 0
while n < 10:
    n = n + 1
    if (n == 3):
        #break
        continue
    print(n)
