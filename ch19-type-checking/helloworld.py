from dataclasses import dataclass


class Person1:
    def __init__(self, name, age, height, email):
        self.name = name
        self.age = age
        self.height = height
        self.email = email


@dataclass
class Person2:
    name: str
    age: int
    height: float
    email: str
