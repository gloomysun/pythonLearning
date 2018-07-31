class Student():
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0-100')
        else:
            self._score = value


s = Student()

print('请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution')


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        print(self.width)
        print(self._width)
        return self.width*self.height

# 测试:
s = Screen()
s.width = 1024
print(s._width)
