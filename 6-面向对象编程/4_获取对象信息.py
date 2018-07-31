print(type(123))
print(type('123'))
print(type(b'123'))
print(type(123.45))
print(type(None))
print(type(abs))
print(type(type))
print(type(lambda x: x))
import types


def fn():
    pass


print(types.FunctionType == type(fn))
print(types.FunctionType == type(lambda x: x))
print(types.LambdaType == type(lambda x: x))

print(isinstance(fn, types.FunctionType))


class Dog():
    pass


d = Dog()
print(isinstance(d, Dog))
print(type(d))

# 获得一个对象的所有属性和方法
print(dir(d))
print(len('abc'))
print('abc'.__len__())


class MyObject():
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


ojb = MyObject()

print(hasattr(ojb,'x'))
print(hasattr(ojb,'y'))
print(getattr(ojb, 'x'))
print(setattr(ojb,'y','1'))
print(getattr(ojb,'y'))