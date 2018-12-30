# 模块 module


def my_sum(*args):

    result = 0
    for item in args:
        result += item

    return result


def my_max(*args):
    print("最大值")


def my_min(*args):
    print("最小值")


class People:

    def __index__(self, name, age):
        self.name = name
        self.age = age


MAX_NUM = 100

print(__name__)


if __name__ == '__main__':

    print('1+2+3+4 =', my_sum(1, 2, 3, 4))
