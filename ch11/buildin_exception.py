# 内置的异常

"""
                              Exceptions
                                  |
             --------------------------------------------
             |                                          |
          内置异常                                  用户自定义的异常
"""


# AttributeError

# >>> import os
# >>> os.test
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'os' has no attribute 'test'
# >>>

# ImportError

# >>> import t
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: No module named 't'
# >>>

# IndexError

# >>> a = [1]
# >>> a[1]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
# >>>

# KeyError

# >>> a = {1:1}
# >>> a[2]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 2
# >>>

# NameError

# >>> b
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'b' is not defined
# >>>

# ZeroDivisionError

# >>> 1/0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
# >>>

# KeyboardInterrupt

# >>> while True:
# ...     pass
# ...
# ^CTraceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# KeyboardInterrupt
# >>>
