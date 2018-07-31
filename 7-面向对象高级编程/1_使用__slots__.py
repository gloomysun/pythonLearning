class Student():
    pass


def set_age(self, age):
    self.age = age


s = Student()
from types import MethodType

# s.set_age = set_age
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)


def set_score(self, score):
    self.score = score


Student.set_score = set_score
s.set_score(100)
print(s.score)

#__slots__ 限制实例添加的属性
class Student():
    __slots__ = ('name','age')

s = Student
s.name='li'
s.score=100
print(s.name)
print(s.score)
s2 = Student()
print(s2.name)
s2.score=100