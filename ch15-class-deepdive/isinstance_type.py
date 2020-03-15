class A:
    pass


class B(A):
    pass

class C:
    pass

a = A()

b = B()

print(isinstance(b, (A, B, C)))

# isinstance(b, A) or isinstance(b, B) or isinstance(b, C)

