a = 100
b = 200

# a,b = b,a
# print(a,b)

a ^= b
b ^= a
a ^= b

print(a,b)