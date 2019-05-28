class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'name={self.name}, age={self.age}'

s1 = Student(name='test', age=10)
l1 = [1, 2, 3]
d1 = {
    1:1,
    2:2
}

class B(Student):
    pass

"""
$ python3.7 -i class_object.py 
>>> 
>>> 
>>> l1
[1, 2, 3]
>>> d1
{1: 1, 2: 2}
>>> type(l1)
<class 'list'>
>>> type(d1)
<class 'dict'>
>>> s1
name=test, age=10
>>> type(s1)
<class '__main__.Student'>
>>> type(list)
<class 'type'>
>>> 
>>> 
>>> type(dict)
<class 'type'>
>>> 
>>> 
>>> 
>>> type(Student)
<class 'type'>
>>> 
>>> isinstance(Student, type)
True
>>> 
>>> 
>>> 
>>> 
>>> isinstance(list, type)
True
>>> 
>>> 
>>> type(type)
<class 'type'>
>>> 
>>> 
>>> Student
<class '__main__.Student'>
>>> list
<class 'list'>
>>> dict
<class 'dict'>
>>> Student.__bases__
(<class 'object'>,)
>>> 
>>> list.__bases__
(<class 'object'>,)
>>> 
>>> dict.__bases__
(<class 'object'>,)
>>> type(object)
<class 'type'>
>>> 
>>> 
>>> 
>>> 
>>> 
"""