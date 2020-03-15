class Student:

    count = 0

    def __init__(self, name):
        Student.count += 1
        self.name = name


s1 = Student('A')
s2 = Student('B')
s3 = Student('C')

print(Student.count)

# print(Student.count)
#
# s1 = Student(name='A')
# print(s1.name)
# print(s1.count)
#
# s1.name = 'B'
# s1.count = 1
# print(s1.name)
# print(s1.count)
# print(Student.count)
#
# Student.count = 2
#
#
# print(Student.count)
# print(s1.count)
#
# #########################
#
#
# s2 = Student('X')
#
# print(s2.count)
