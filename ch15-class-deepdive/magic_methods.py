class Account:

    def __init__(self, name, amount=0):
        self.name = name
        self.amount = amount
        self._transaction = []
    
    @property
    def balance(self):
        return self.amount + sum(self._transaction)

    def __len__(self):
        return len(self._transaction)

    def __repr__(self):
        return f'Account({self.name}, {self.amount})'

    def __str__(self):
        return f'name={self.name}, amount={self.amount}'

    def add_transaction(self, amount):
        self._transaction.append(amount)

    def __eq__(self, other):
        return self.balance == other.balance
    
    def __lt__(self, other):
        return self.balance < other.balance


a1 = Account('Jack', 10)
a1.add_transaction(100)
a1.add_transaction(-20)

a2 = Account('Mark', 10)
a2.add_transaction(200)
a2.add_transaction(-50)
a2.add_transaction(10)

print(a1==a2)
print(a1<a2)


