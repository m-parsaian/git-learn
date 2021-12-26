import hashlib

input_str = input('Enter something: ')

print(hashlib.sha256(input_str.encode('utf-8')).hexdigest())
