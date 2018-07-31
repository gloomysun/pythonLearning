a = 1
b = 2
if a > 0:
    print('a>0')
elif b > 0:
    print('b>0')
print('==============练习===================')

# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 用if-elif判断并打印结果：
height = 1.76
weight = 70
BMI = weight / (height * height)
if BMI < 18.5:
    print('过轻')
elif BMI < 25:
    print('正常')
elif BMI < 28:
    print('过重')
elif BMI < 32:
    print('肥胖')
else:
    print('严重肥胖')
