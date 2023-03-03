"""
主要参考文档

PEP 484 Type Hints: https://peps.python.org/pep-0484/

mypy Built-in types: https://mypy.readthedocs.io/en/stable/builtin_types.html

"""

# 简单类型

pi: float = 3.142
name: str = "Guido"
centered: bool = False


def circumference(radius: float=10) -> float:
    return 2 * pi * radius


# 复杂类型  list, tuple, dict
from typing import Dict, List, Tuple
num_list: List[int] = [1, 2, 3]
num_tuple: Tuple[int] = (1, 2, 3)
num_dict: Dict[int, int] = {
    1: 1,
    2: 2
}

# Any 和 Sequence
from typing import Any

list1: List[Any] = [1, 'a', [1, 2]]

from typing import List, Sequence

def square(elems: Sequence[float]) -> List[float]:
    return [x**2 for x in elems]



# The Optional Type
from typing import Optional
def test(a: str, b: Optional[str]=None)-> None:
    pass


test(a='1')
test(a='1', b='2')
