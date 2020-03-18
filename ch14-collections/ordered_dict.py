from collections import OrderedDict

# d = dict()

# d['a'] = 1
# d['c'] = 3
# d['b'] = 2
# d['d'] = 4

# print(d)

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3

print(d)

d.move_to_end('a')

print(d)