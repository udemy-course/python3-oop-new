import sys
import hashlib

file_name = sys.argv[1]
with open(file_name, "rb") as f:
    bytes = f.read()  # read entire file as bytes
    readable_hash = hashlib.sha256(bytes).hexdigest().upper()
    print(readable_hash)