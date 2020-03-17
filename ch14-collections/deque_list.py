from collections import deque
import time

d = deque(range(10000000))
#print(d)


l = list(range(10000000))
#print(l)

t1 = time.time()
#d.append(-1)
print(d[59999])
# d.insert(1110, -1)
print('deque:', time.time() - t1)

t2 = time.time()
#l.append(-1)
print(l[59999])
# l.insert(1110, -1)
print('list:', time.time() - t2)
