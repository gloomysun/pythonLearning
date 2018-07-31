class Animal():
    def run(self):
        print('animal run')


Animal().run()


class Dog(Animal):
    def run(self):
        print('dog run')


class Cat(Animal):
    pass


Dog().run()


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())


class Timer():
    def run(self):
        print('time run')

run_twice(Timer())