def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('错误类型')
    elif x < 0:
        return -x
    else:
        return x


print(type(my_abs(-100)))
print(my_abs(-100))

# 返回多个值
import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


print(type(move(1, 1, 2, 30)))
print('==============练习===================')


# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0
# 的两个解。
# 提示：计算平方根可以调用math.sqrt()函数：

def quadratic(a, b, c):
    return (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a), (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)


# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
