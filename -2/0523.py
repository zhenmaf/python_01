

# 字符串格式化:  %s
my_str = "my name is %s" % ('张三')
print(my_str)

# 格式化整数:  %d
my_str1 = "张三今年 %d 岁" % (22)
print(my_str1)

# 格式化浮点数:  %f
my_str2 = "一斤苹果%f元" % (5.296)
print(my_str2)

# m.n:m是显示的最小总宽度，n是小数点后的保留位数
my_str3 = "一斤苹果%7.2f元" % (5.111)
print(my_str3)

# -:显示左对齐
my_str4 = "一斤苹果%-7.2f元" % (5.111)
print(my_str4)

# +:正数前面显示+
my_str5 = "一斤苹果%+-7.2f元" % (5.111)
print(my_str5)

#  :正数前面显示空格
my_str6 = "一斤苹果% 7.2f元" % (5.111)
print(my_str6)

# 0:不希望有空格，前面用0代替
my_str7 = "一斤苹果%07.2f元" % (5.111)
print(my_str7)

# 使用format去格式化 : "{}".format("字符串")
my_str8 = "张三今年{}岁" .format(22)
print(my_str8)

# format格式化两个参数 : "{}  {}".format(参数1，参数2)
my_str9 = "今天星期{},张三买了{}斤苹果".format('一','5')
print(my_str9)

print("今天星期{},张三买了{}斤苹果".format('一','5'))

# format的位置参数 : "{0}{1}{2}{3}"format.(第一个数，第二个数，第三个数，第四个数)
my_str10 = "今天星期{1},张三买了{0}斤苹果".format('一','5')
print(my_str10)

# format的关键字参数 : "{x}{y}"format.(x='hello',y='world')
my_str11 = "今天星期{x},张三买了{y}斤苹果".format(x='一',y='5')
print(my_str11)

# 位置参数和关键字参数结合使用 : "{0}{x}"format.('hello',x='world')
my_str12 = "今天星期{0},张三买了{x}斤苹果".format('一',x='5')
print(my_str12)

# 字符串方法演示

# 1.连接字符串 : join(seq)
astr = "+"
bstr = astr.join("world")
print(bstr)

# 2.分割字符串 : split(str="")，其中str代表分割符
cstr = "hello world python"
dstr = cstr.split("l")
print(dstr)

# 3.查找字符串 : find(substr),如果找到了返回的是最小索引，没有找到返回-1
estr = "helloworld"
print(estr.find("w"))
print(estr.find("x"))
print(estr.index("w"))

# 4.查找以xxx结尾的字符串 : endswith('xxx')
fstr = "测试报告.doc"
if fstr.endswith('.doc'):
    print("它是一个word文档")

# 5.替换字符串 : replace(old_value.new_calue)
gstr = "hello world"
hstr = gstr.replace('world','hello')
print(hstr)

# 6.查找字符串 : 使用方法和find一样，index找不到会报错
print(estr.index("w"))

# 7.查找以xxx开头的字符串 : startwith(old_value.new_calue)
# istr = "ll_hello"
# if istr.startswith('ll')
#     print('指定目录')


# 12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# jstr = "ds9sad a98f-89g9s8ag9 89-w8 9-8-87g -w8 gw-rgw=g88w"
# a = b = c = d = 0
# for x in jstr:
#     if x.isdigit():
#         a += 1
#     elif x.isalpha():
#         b += 1
#     elif x.isspace():
#         c += 1
#     else:
#         d += 1
# print(a)
# print(b)
# print(c)
# print(d)

# 序列的通用操作

# 1.索引: seq[index],index 代表的下标，默认从0开始；索引支持 列表，元组，字符串
lst = ['red','hello',2,3.4]
print(lst[1])   # 列表里的第二个值
print(lst[-3])

my_str13 = "redhello2"
print(my_str13[1])
print(my_str13[-1])

# 2.序列的切片: seq[start:end:step],start代表位置默认是从0开始，
# end是代表结束位置，如果不填写，代表列表的长度，step代表的是步长，默认是1
lst1 = ['red','green','blue','black','gold','orange']
print(lst1[1:5:1])     # 获取第2-5个元素
print(lst1[1:6:2])     # 获取的偶数值
print(lst1[:2])    # 取1-2个元素，步数为1

print(lst1[2:])    # 省略了end和step,和下方结果一致
print(lst1[2:6:1])
print(lst1[2::])

print(lst1[::2])    #省略了start和end
print(lst1[0:6:2])

print(lst1[1::2])    #省略了end
print(lst1[1:6:2])

print(lst1[:3:])    #省略了start和step
print(lst1[0:3:1])

print(lst1[::])   #全省略


# 列表中有10个元素，取出其中的奇数个数的元素
print(lst1[::2])


# 3.序列的相加和相乘:+,*
alst = [1,2]
blst = [3,4]
clst = alst + blst
print(clst)
astr = 'hello'
bstr = 'python'
print(astr + bstr)
dlst = alst * 2
print(dlst)

elst = [None] * 3
print(elst)

print("=====================")
print("=" * 30)

print("hello" + "world")

klst = list()
print(klst)
cstr = "abc"
mlst = list(cstr)
print(cstr)

nlst = [1,2,3]
dstr = str(nlst)
print(dstr)
print(dstr,type(dstr))
estr = str(23)
print(estr,type(estr))

# 循环序列中的索引和值
lst7 = ['red','green','blue','black','gold','orange']
# for x in lst7:
#     print(x,end=' ')

# 循环序列中的索引和值
for a,b in enumerate(lst7):
    print(a,'====',b)


# 生成一个1-10的列表
lst = []
for x in range(1,11):
    lst.append(x)
print(lst)

lst2 = [x for x in range(1,11)]
print(lst2)

print([x for x in range(1,11)])

# 生成一个1-10的列表,要求只打印奇数
lst3 = [x for x in range(1,11) if x % 2 != 0]
print(lst3)

# 生成一个1-10的列表,生成的奇数的值加上10
lst4 = [x + 10 for x in range(1,11) if x % 2]
print(lst4)

for x in range(1,11):
    if x % 2 != 0:
        x += 10
        print(x,end=' ')