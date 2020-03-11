
def add(x, y):
    ''' return the sum of x and y'''
    return x + y


"""
$ python3.7 -i all_is_object.py 
>>> 
>>> 
>>> add
<function add at 0x109fdf1e0>
>>> 
>>> 
>>> add(1,2)
3
>>> 
>>> 
>>> add.__name__
'add'
>>> add.__doc__
' return the sum of x and y'
>>> 
>>> 
>>> dir(add)
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__d
oc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_s
ubclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__
reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> 
>>> 
>>> add.__call__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add() missing 2 required positional arguments: 'x' and 'y'
>>> 
>>> add.__call__(1,2)
3
>>> 
>>> 
>>> 
>>> a = add
>>> 
>>> 
>>> a
<function add at 0x109fdf1e0>
>>> add
<function add at 0x109fdf1e0>
>>> a(1,2)
3
>>> a.__name__
'add'
>>> 
>>> 
>>> a.__doc__
' return the sum of x and y'
>>> 
>>> 
>>> l = []
>>> l.append(add)
>>> l
[<function add at 0x109fdf1e0>]
>>> 
>>> 
>>> l[0]
<function add at 0x109fdf1e0>
>>> l[0](1,2)
3
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> add
<function add at 0x109fdf1e0>
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def test(func):
...    return func(1,2)
... 
>>> 
>>> test(a)
3
>>> test(add)
3
>>> 
>>> 
>>> def test(func, x, y)
  File "<stdin>", line 1
    def test(func, x, y)
                       ^
SyntaxError: invalid syntax
>>> def test(func, x, y):
...     return func(x, y)
... 
>>> 
>>> 
>>> test
<function test at 0x10a1136a8>
>>> test(add, 1, 3)
4
>>> 
>>> 
>>> 
"""