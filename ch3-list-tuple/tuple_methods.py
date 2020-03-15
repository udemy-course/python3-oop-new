# 获取元组的一些基本信息

tuple1 = (9, 1, -4, 3, 7, 11, 3)

print('tuple1的长度 =', len(tuple1))


print('tuple1里的最大值=', max(tuple1))


print('tuple1里的最小值 =', min(tuple1))


print('tuple1里3这个元素一共出现了{}次'.format(tuple1.count(3)))


# 元组的改变？？？？

# tuple2 = ('a', 'c', 'd')
#
# tuple2[1] = 2


# 元组翻转 ??
# tuple3 = (1, 2, 3)
# tuple3.reverse()


# 元组排序 ??
#
# tuple4 = (9, 1, -4, 3, 7, 11, 3)
# tuple4.sort(reverse=True)

print(tuple1.index(9))