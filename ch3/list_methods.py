# 获取列表的一些基本信息

list1 = [9, 1, -4, 3, 7, 11, 3]

print('list1的长度 =', len(list1))


print('list1里的最大值=', max(list1))


print('list1里的最小值 =', min(list1))


print('list1里3这个元素一共出现了{}次'.format(list1.count(3)))


# 列表的改变

list2 = ['a', 'c', 'd']

# 给list2结尾添加一个新元素 'e'

list2.append('e')
print('list2=', list2)


# 在list2的'a'和'c'之间插入一个 'b'
list2.insert(1, 'b')
print('list2=', list2)

# 删除list2里的'b'
list2.remove('b')
print('list2=', list2)


list2[0] = '1'
print('list2=', list2)


# a = '123'
# a[0] = 'a'
# a = 'abc'


# 列表翻转
list3 = [1, 2, 3]
list3.reverse()
print('list3=', list3)


# 列表排序

list4 = [9, 1, -4, 3, 7, 11, 3]
list4.sort(reverse=True)
print('list4=', list4)


list5 = [1, 'a', 3, [1,2], 'c']
