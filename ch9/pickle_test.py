# import pickle
#
#

class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayhi(self):
        print("Hi, my name is {}, and I'm {}".format(
            self.name, self.age
        ))
#
#
# p1 = People(name='Jack', age=30)
# f = open('p1', 'wb')
# pickle.dump(p1, f)
# f.close()


# 序列化对象的加载

import pickle


f = open('p1', 'rb')
p2 = pickle.load(f)
f.close()

print(p2, p2.name, p2.age)
p2.sayhi()

