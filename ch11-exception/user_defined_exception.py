

class MyException(Exception):

    pass



# try:
#     raise MyException("这是用户定义的异常")
# except MyException as e:
#     print(e)


def my_interaction():
    raise MyException('这是用户定义的异常')


try:
    my_interaction()
except MyException as error:
    print(error)
else:
    print('Executing the else clause.')


try:
    my_interaction()
except MyException as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('清理工作')
