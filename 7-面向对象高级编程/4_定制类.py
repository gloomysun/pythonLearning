class Student():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object[name:%s]' % self.name

    __repr__ = __str__


s = Student('ly')
print(s)

print('===========================练习===================')


class Chain():
    def __init__(self, path=''):
        self.path = path

    def __getattr__(self, item):
        if item == 'users':
            return lambda x: Chain('%s/%s/:%s' % (self.path, item, x))
        return Chain('%s/%s' % (self.path, item))

    def __str__(self):
        return self.path

    __repr__ = __str__


c = Chain()
print(c.user.list)
print(c.users('xiaoli').index)

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self,item):
        return Student()

s = Student('xx')
print(s('ddd'))