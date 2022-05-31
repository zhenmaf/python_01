
# 1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
# a = input("请输入一个整数:")
# b = input("请输入一个整数:")
# c = input("请输入一个整数:")
# d = input("请输入一个整数:")
#
# print(int(a)+int(b)-int(c)*int(d))

# 2. 打印1~100内被3整除的所有数的和
sum = 0
for x in range(1,101):
    if x % 3 == 0:
        sum += x
        x += 1
print(sum)

sum = 0
for x in range(3,101,3):
    sum += x
    x += 1
print(sum)

sum = 0
x = 1
while x <= 100:
    if x % 3 == 0:
        sum += x
    x += 1
print(sum)

# 3. 使用range()输出1~10内的所有奇数
for x in range(1,11,2):
    print(x)

# 4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
sum1 = 0
sum2 = 0
for x in range(1,101):
    if x % 2 == 0:
        sum1 += x
    else:
        sum2 += x
print(abs(sum1 - sum2))

# 5. 求1+2+3+...+100的和
sum = 0
for x in range(1,101):
    sum += x
print(sum)

# 6. 判断一个数n能同时被3和5整除
# n = int(input("输入一个数:"))
# if n % 3 ==0 and n % 5 == 0
#     print("能被3整除")
# else:
#     print("不能被3整除")



# 7.定义一个整数变量，判断该变量值是否是1 - 100内的某个数，如果是打印出来

# x1 = input("输入一个整数:")
# if x < int(x1) < 100:
#     print("hello")
# else:
#     print("world")


# 8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()

# lst = []
# x = int(input("输入一个整数"))
# y = int(input("输入一个整数"))
# z = int(input("输入一个整数"))
# lst.append(x)
# lst.append(y)
# lst.append(z)
# print(lst)
# lst.sort()
# print(lst)

# 9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。备注：需要使用input()方法
# score = int(input("输入分数:"))
# if score >= 90:
#     print("A")
# elif score >= 60:
#     print("B")
# else:
#     print("C")

# 10. 将一个列表的数据复制到另一个列表中。
alst = [1,2,3,4]
blst = [5,6,7,8]
alst.extend(blst)
print(alst)

# 11. 输出 9*9 乘法口诀表。
for x in range(1,10):
    for y in range(1,x+1):
        print(y ," * ",x," = ",x * y,end='   ')
    print()

