"""
主要参考文档

PEP 484 Type Hints: https://peps.python.org/pep-0484/

mypy Built-in types: https://mypy.readthedocs.io/en/stable/builtin_types.html

"""

# 简单类型

pi: float = 3.142
name: str = "Guido"
centered: bool = False


def circumference(radius: float) -> float:
    return 2 * pi * radius


# 复杂类型  list, tuple, dict



# Any 和 Sequence


# The Optional Type