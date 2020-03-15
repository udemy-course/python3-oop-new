
def add(a, b):
    """
    >>> add(1, 2)
    3
    >>> add(1, 1.2)
    Traceback (most recent call last):
    ValueError: a和b必须是整数
    """
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        raise ValueError("a和b必须是整数")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
