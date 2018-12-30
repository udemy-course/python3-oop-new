# 类的定义


class MyClass:
    pass


# __init__() method 方法 function(函数)
# attribute 属性
# method 方法


class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayhi(self):
        print("Hi, my name is {}, and I'm {}".format(
            self.name, self.age
        ))


# class instance 类的实例

someone = People(name='Jack', age=20)
print(someone.name)
print(someone.age)
someone.sayhi()
