import os
from pathlib import Path, WindowsPath

# https://docs.python.org/3/library/pathlib.html

# in_file = os.path.join(os.getcwd(), "demo", "test.txt")

# print(in_file)

# a = Path.cwd()

# print(a)

# print(type(a))

p = Path.cwd().parent

for file in p.rglob("*.txt"):
    print(file)


# glob, rglob