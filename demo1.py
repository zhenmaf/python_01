



# print方法
print("hello world")
print(1+1)
print(2 == 2)

# type方法
print(type("hellp world"))
print(type(11))


# 整数  int
num1 = 10
print(num1)
print(id(num1))

# 二进制  0b+数值
num2 = 0b1010
print(num2,type(num2))

# 八进制  0o+数值
num3 = 0o12
print(num3,type(num3))

# 十六进制   0x
num4 = 0xa
print(num4,type(num4))

# 通过几个内置函数可以将10进制数转换成其他进制的字符串表示
# bin（）十进制转换二进制
# oct（）十进制转换八进制
# hex（）十进制转换十六进制

print(bin(10),type(bin(10)))
print(oct(10),type(oct(10)))
print(hex(10),type(hex(10)))

# 布尔值    bool
# 真:True   假:False
# True:1      False:0
b01 = True
b02 = False
print(b01,type(b01))
print(b02,type(b02))

# 浮点数  float
pi = 3.1415
print(pi,type(pi))

f1 = 3.1E1
print(f1,type(f1))

f2 = 3.1e-1
print(f2,type(f2))

# 复数  complex
c1 = 1 + 2j
print(c1,type(c1))

# 字符串   str
str1 = "这是一个字符串"
print(str1,type(str1))


# 元组   tuple
t1 = (1,2,3)
print(t1,type(t1))

# 列表  list
l1 = [1,2,3]
print(l1,type(l1))

# 集合  set
s1 = {1,2,3}
print(s1,type(s1))

# 字典  dict
d1 = {"name":"qinrui","age":18}
print(d1,type(d1))


# 空类型  NoneType
n1 = None
print(n1,type(n1))

