# A mutable object can have it value changed after it has been created

# list is mutable type

value = [1, 2, 3]
value += [4]

# immutable object must be re-created when modified
# this results in a new copy of the object which replaces the old one

# string is immutable

name = 'python'

name = 'hello' + name


# 常用数据类型中，只有 list, set, dict 是mutable的，其它都是immutable

"""
>>> x = 1
>>> id(x)
9784864
>>>
>>> x += 1
>>> id(x)
9784896
>>>
>>> y = [1,2,3]
>>> id(y)
140369901657600
>>>
>>> y.append(4)
>>> id(y)
140369901657600
>>>
"""