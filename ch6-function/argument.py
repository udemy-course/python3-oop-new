
# def add(a, b):
#     return a + b


# def add(*args):
#
#     result = 0
#     for item in args:
#         result += item
#     return result
#
#
# print(add(1, 2, 10, 20, 30))
#

# def test(a, b, c):
#     print(a + b + c)
#
#
# def add(x, **kwargs):
#
#     if x == 2:
#         test(**kwargs)
#
#
# add(x=2, a=1, b=2, c=2)
#

def test(a, b=False):
    if b:
        return a
    else:
        return a * a


print(test(a=2, b=True))


def test1(**kwargs):
    pass