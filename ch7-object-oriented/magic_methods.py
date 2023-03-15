class FancyTuple:

    properties = {
        'first': 0,
        'second': 1,
        'third': 2,
        'fourth': 3,
        'fifth': 4,
    }

    def __init__(self, *items) -> None:
        self.items = items

    def __len__(self) -> int:
        return len(self.items)

    def __getattr__(self, name):
        try:
            return self.items[self.properties[name]]
        except KeyError:
            raise AttributeError(f'No such attribute: {name}')



if __name__ == '__main__':
    t = FancyTuple(1, 2, 3, 4, 5)
    print(t.first)
    print(t.second)
    print(t.third)
    print(t.fourth)
    print(t.fifth)
    print(len(t))
