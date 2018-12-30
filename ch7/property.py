class People:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        # 格式的规范
        return self.__name.upper()

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, name):
        # 做一些合法性的检查
        self.__name = name

    def set_age(self, age):
        self.__age = age


someone = People(name='Jack', age=20)
print(someone.name)
print(someone.age)
someone.name = 'Test'
print(someone.name)
