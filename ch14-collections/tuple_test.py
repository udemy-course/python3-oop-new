# tuple

print('1.iterable')
my_tuple = ('python', 3, 7, 3)
for i in my_tuple:
    print(i)

print('2.indexing and slicing')
print(my_tuple[0])
print(my_tuple[0:2])

print('3.sequence unpacking')
name, _, y, z  = my_tuple
print(name, y, z)  #name=python, y=7, z=3

name, *_  = my_tuple
print(name)

name, *version  = my_tuple
print(name, version)


print('4.immutable')
# my_tuple[1] = 2  thread safe

my_dict = {my_tuple: 1}
print(my_dict)
my_tuple = (1, 2, 3)
print(my_dict)
# my_dict = {[1, 2]: 1}

# i = 1
# a = {i: 1}
# i = 2
# print(a)

a = []
 
b = ()
