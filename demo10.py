

# 函数 : 具有特定的功能的代码块，比如说登陆功能，相加


"""
def 函数名字(参数列表):
    代码块
"""


# 函数的定义 : 加法
def add(x,y):
    z = x + y
    return z

# 函数的调用
add(3,4)
print(add(3,4))
print(add(3,4.8))
print(add('a','b'))

def div(x,y):
    return x / y

print(div(2,5))


# 函数 : 位置参数
def add(x,y):
    return x + y

print(add(3,4))
print(add('hellp','world'))
print(add(3,4))
print()


# 关键字参数
def student_lesson(grade,subject):
    z = "{}年级上{}课".format(grade,subject)
    return z

print(student_lesson(grade=2,subject='语文'))
print(student_lesson(subject='语文',grade=2))
print(student_lesson('2','语文'))
print(student_lesson(2,subject='语文'))
# 用处 : 实现一个函数，参数特别多
# connect(host='localhost',username='root',password='root',datebase,port,commit)

# 默认参数 : 其中某个参数会有默认值，带有默认值的参数放在最后面。
def study_kanguage(name,language='python'):
    info = ("{}要学习{}语言".format(name,language))
    return info

print(study_kanguage('张三','java'))
print(study_kanguage('李四','python'))
print(study_kanguage('王五'))


# 2.可变化参数，字典形式的参数
def show_info(**kwarges):
    print(kwarges)

dt_data = {'x':1,'y':2,'z':3}
print(show_info(a='hello',b='world',c=123))
print(show_info(a='hello',b='world'))
print(show_info(**dt_data))


def shou_info(*args,**kwargs):
    print(args,kwargs)


# 面向对象

# 1.定义一个电梯的类 : class 类名()
class Elevator():
    # 2.在类里申明车的属性(数据)和方法(函数)
    button = "开/关"
    floor = 15
    peple_nums = 13

    # 打开电梯
    def start(self):
        print("打开电梯")

    # 关闭电梯
    def stop(self):
        print("关闭电梯")

    # 运行电梯
    def run(self):
        print("电梯运行")
# 3.定义一个具体的对象，叫初始化对象，对象是一个实实在在的对象。=> 初始化对象：对象名 = 类名
e = Elevator()

# 4.使用对象调用方法或者属性 : 对象名.属性 || 对象名.方法
e.start()
e.stop()
e.run()


class Students():

    name = ""
    grade = ""

    def study(self):
        print("{}年纪的学生{}正在学习".format(self.grade,self.name))

s1 = Students()
s1.name= "张三"
s1.grade = '5'
print(s1.study())

s2 = Students()
s2.name = '李四'
s2.grade = '4'
print(s2.study())