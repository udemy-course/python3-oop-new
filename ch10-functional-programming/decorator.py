def test1(x):
    return x * 2


def test2(x):
    return x * x * x


test1(1)

test2(2)


def demo(f):

    def f_new(*args, **kwargs):
        print(f.__name__)
        return f(*args, **kwargs)

    return f_new


# f = demo(test1)
#
# print(f(2))

# f = demo(test2)
#
# print(f(2))


@demo
def test3(x):
    return x * 2 * x
#
#
# a = test3(4)
#
# print(a)


@demo
def test3(x, y):
    print('hello world')


def demo_new(s):

    def demo(f):
        def f_new(*args, **kwargs):
            print(s)
            print(f.__name__)
            return f(*args, **kwargs)

        return f_new
    return demo


@demo_new('hello world')
def test4(x, y, z):
    print('x={}, y={}, z={}'.format(x, y, z))


test4(1, 2, 3)
