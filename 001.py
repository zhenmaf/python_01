
# 隐式转换
# int类型和bool类型进行算数运算时，会自动将bool转换int再进行运算
# int类型和float类型进行算数运算时，会自动将int转换成float，进行运算，结果为float
num1 = 100
num2 = 3.14
num3 = num1 + num2
print(num3,type(num3))


# 显示转换     “100”    ->    100
# int()      int("100") ->  100
float()
complex()
bool()
tuple()
str()
list()
dict()
set()


s1 = "1011"
num1 = int(s1)
print(num1,type(num1))

# s2 = "1011a"
# num2 = int(s2)

s3 = "3.14"
num3 = float(s3)
print(s3,type(s3))


# 转换成bool类型为false的值
# 0, 0.0, "", (), {}, [], set(), None
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(set()))
print(bool(None))

print("==============")
# 交换两个变量的值
a = 100
b = 200

a,b = b,a
print(a,b)

# 算数运算符
print(18 / 3)
print(17 / 3)   # 结果是float

print(17 // 3)    # 结果是int，相当于商
print(17 % 3)       # 取余数

print(2 ** 3)

# input()函数
# 从终端获取用户输入，返回结果是一个str类型
# inputValue = input("请输入一个四位数")
# print(inputValue,type(inputValue))

# 赋值运算符
num1 = 100
num1 += 10  # -> num1 = num1 + 10     110

# 多重赋值：给多个变量赋同一个值
a = b = c = 300
print(a,b,c)

# 多元赋值：给多个变量赋不同的值
e,f,g = 1,2,3
print(e,f,g)
# 多元赋值的时候，值的个数必须和变量个数相同
# x,y = 1
# x,y = 1,2,3

# 比较运算符
# 通过比较运算符连接的表达式结果是一个bool类型
# <,>,==,!=,<=,>=

# 逻辑运算符
# 逻辑运算符表达式结果是一个bool类型
# and , or , not

# 成员运算符
# 表达式结果是一个bool类型
# in , not in
# x in object :如果x是object中的一个元素，那么表达式的结果为True，否则表达式的结果为False
print("a" in "abcd")   #True
print("ab" in "abcd")   #True
print("ac" in "abcd")   # False
print("ab" not in "abcd")  #False
print("ac" not in "abcd")  #True

print(1 in (1,2,3))   #True
print(4 in (1,2,3))   #False

# 身份运算符
# 表达式结果是一个bool类型
# is ：当两个对象再内存中是同一块内存，返回True，否则返回False
# is not ： 和is相反
num1 = 20
num2 = 20
print(num1 == num2)  # 判断值是否相同
print(num1 is num2)  # 判断是否一块内容
print(id(num1),id(num2))

print(num1 is not num2)  # False

num3 = 20
num4 = 20.0
print(num3 == num4)
print(num3 is num4)
print(id(num3),id(num4))

# 位运算符
# 数据再内存中都是以二进制存储
# 按位与运算: &
# 按位或运算: |
# 按位异或: ^
# 按位取反: ~
# 左移: <<
# 右移: >>
num1 = 60  # 0011 1100
num2 = 13  # 0000 1101

print(num1 & num2)  # 0000 1100  ->  12
print(num1 | num2)  # 0011 1101  ->  61
print(num1 ^ num2)  # 0011 0001  ->  49
print(~num1)  #  ~x = -x-1   ->   -61
# 左移两位，相当于原来的数乘以4
print(num1 << 2)  # 1111 0000
# 右移两位，相当于原来的数除以4
print(num1 >> 2)  # 0000 1111
print(num1 << 3)