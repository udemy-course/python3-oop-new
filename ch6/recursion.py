# n! = 1*2*3........(n-1)*

# n* (n-1) * (n-2)...........2*1!

# def test(n):
#     result = 1
#     for item in range(1, n+1):
#         result = result * item
#     return result


def test(n):
    if n == 1:
        return n
    return n * test(n-1)


print(test(3))
