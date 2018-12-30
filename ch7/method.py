class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayhi(self):
        print("Hi, my name is {}, and I'm {}".format(
            self.name, self.age
        ))

    @classmethod
    def test1(cls):
        print('这是一个类方法')
        cls.test2()

    @staticmethod
    def test2():
        print('这是一个静态方法')


p1 = People(name='Jack', age=20)
p1.sayhi()

p1.test1()

