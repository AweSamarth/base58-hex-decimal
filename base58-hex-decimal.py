import base58

mystring = b'hello world'
mybase58 = base58.b58encode(mystring)
print("Base58 String: ")
print(mybase58)
print(base58.b58decode(mybase58))

mynumber = 23
myhexnumber = hex(mynumber)

print("Hex number: ")
print(myhexnumber)

