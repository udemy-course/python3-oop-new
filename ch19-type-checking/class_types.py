class People:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def can_drive(p: People) -> bool:

    if p.age >= 18:
        return True
    else:
        return False
    
p = People(name='Jan', age=20)

print(can_drive(p=p))