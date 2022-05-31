
# 1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
a = 3
b = 4
c = 5
d = 6
print(a+b-c*d)

# 2. 打印1~100内被3整除的所有数的和
x = 0
sum = 0
while x <= 100:
    sum += x
    x += 3
print(sum)

# 3. 使用range()输出1~10内的所有奇数
for x in range(1,11,2):
    print(x)

# 4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
sum1 = 0
sum2 = 0
x = 1
for x in range(1,101,1):
    if x % 2 == 0:
        sum1 += x
    else:
        sum2 += x
print(sum1 - sum2)

# 5. 求1+2+3+...+100的和
sum = 0
for x in range(1,101,1):
    sum += x
print(sum)

# 6. 判断一个数n能同时被3和5整除
# x = int(input("输入一个数:"))
# if x % 3 == 0 and x % 5 == 0:
#     print("被3和5整除")
# else:
#     print("不能被3和5整除")

# 7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
# x = int(input())
# if x in range (1,101,1):
#     print(x)

# 8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
# x = int(input())
# y = int(input())
# z = int(input())
# list = [x,y,z]
# list.sort()
# for l in list:
#     print("排序后结果:",l)

#  9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。备注：需要使用input()方法
# score = int(input("输入成绩"))
# if score >= 90:
#     print("A")
# elif score >=60 and score <= 89:
#     print("B")
# else:
#     print("C")

# 10. 将一个列表的数据复制到另一个列表中
alst = [1,2]
blst = [3,4]
alst.extend(blst)
print("追加后的结果:",alst)

# 11. 输出 9*9 乘法口诀表

# 12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
# s = input("输入字符串:")
# a = b = c = d = 0
# for x in s:
#     if x.isalpha():
#         a += 1
#     elif x.isspace():
#         b += 1
#     elif x.isdigit():
#         c += 1
#     else:
#         d += 1
# print("字母",a)
# print("数字",b)
# print("空格",c)
# print("其他",d)

# 13. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

# 14. 题目：打印出如下图案（菱形）
num = 5    # 总数
x = num - 1  # 循环数

for n in range(1,num):
    space = " " * (x-n)
    start = "*" * (2 * (n - 1) + 1)
    print(space + start + space)

for n in range(1,4):
    space = " " * n
    start = "*" * (7 - 2 * n)
    print(space + start)
    
a = "*"
alst = [1,3,5,7,5,3,1]
for x in alst:
    print((a * x).center(7))