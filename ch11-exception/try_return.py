def test_exc_return():

    try:
        print('in try....')
        raise KeyError()
        return 1

    except KeyError:
        print('key error')
        return 2

    else:
        return 3
    
    finally:
        print('finally')

if __name__ == "__main__":

    a = test_exc_return()
    print(a)