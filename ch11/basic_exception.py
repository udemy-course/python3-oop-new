
a = [10, 4, 3, 7, 11, 6, 1, 9, 22, '10']

try:
    b = [item for item in a if 100 % item == 0]
    print(b)
except ZeroDivisionError:
    print('0不能作为除数')
except TypeError:
    print('数据类型错误')

except Exception:
    print('其它类型异常')

print('完成')
