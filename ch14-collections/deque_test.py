from collections import deque


d = deque([1, 2, 3])

d.append(4) 
print(d)  # [1, 2, 3, 4]
d.appendleft(0)
print(d) # [0, 1, 2, 3, 4]

d.pop()
print(d) # [0, 1, 2, 3]
d.popleft()
print(d)  # [1, 2, 3]


d.extend([4, 5])
print(d)  # [1, 2, 3, 4, 5]
d.extendleft([0, -1, -2])
print(d)  # [-2, -1. 0, 1, 2, 3, 4, 5]

d.reverse()
print(d)  # [5, 4, 3, 2, 1, 0, -1]

d.insert(0, 123)
print(d)  # [123, 5, 4, 3, 2, 1, 0, -1]
