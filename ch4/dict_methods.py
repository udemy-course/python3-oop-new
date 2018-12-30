d = {
    'Name': 'Jack',
    'Age': 9,
    'Grade': 5,
}

print(d.get("name"))


print(d.keys())

print(d.values())

print(d.items())

c = d.pop('Name')

print(c)

print(d)

d.clear()

print(d)


# 字典的更新

c = {
    1: 1,
    2: 2
}

c[3] = 3
c[4] = 4

print(c)


d = {
    1: 5,
    6: 6
}

# c.update(d)
#
# print(c)

e = {**c, **d}

print(e)



