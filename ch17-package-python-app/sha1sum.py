import sys
import hashlib

data = sys.argv[1]
m = hashlib.sha1()
m.update(bytes(data, 'utf-8'))
print(m.hexdigest())
