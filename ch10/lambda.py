# lambda匿名函数


def test(x, y):
    return x + 2 * y


def demo(x, y, f):
    return f(x, y)


print(demo(1, 2, lambda x, y: x + 2 * y))


def add_n(n):
    return lambda x: n + x


f = add_n(40)

print(f(1))
print(f(-10))
