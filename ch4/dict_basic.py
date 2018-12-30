# 字典创建

a = {
    1: 'a',
    2: 'b',
    '3': 'c'
}


# 不可改变的数据类型


l1 = [1, 2, 3]
#
#
# b = {
#     l1: 1
# }

t1 = (1, 2, 3)

c = {
    t1: l1
}

print(c)


d = dict()
print(d)

e = dict(a=1, b=2, c='a')
print(e)


# 字典的访问

print(e['c'])

e['d'] = 123

print(e)

e['c'] = 3

print(e)

f = {1:1}

g = {
    f: [1,2,3]
}

f[2] = 2
f[3] = 3
