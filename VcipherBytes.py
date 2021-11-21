import string

b = input("input b:")
b = bytearray(b,'utf-8')
k = input("input:k")
k = bytearray(k,'utf-8')
c = bytes(i^j for i,j in zip(b,k))
print(c)