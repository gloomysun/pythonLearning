class Student(object):
    def __init__(self, name):
        self.name = name


s = Student('Bob')
s.score = 90


class Student(object):
    name = 'jim'


s = Student()
print(s.name)
s.name = 'zzs'
print(s.name)
del s.name
print(s.name)
print('====================练习==================')


# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student(object):
    count = 0
    def __init__(self):
        Student.count = Student.count + 1

s1 =Student()
print(s1.count)
s2 =Student()
print(s2.count)