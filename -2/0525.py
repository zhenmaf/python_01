


class Students():

    # name = "张三"
    # grade = "二年级"

    def __int__(self,name,grade):
        self.name = name
        self.grade = grade

    def study(self):
        # self.name = '张三'
        # self.grade = '二年级'
        print("这里的self是:",self)
        # print("{}年级的学生{}正在学习".format(self.grade,self.name))

    def eat(self):
        print(self.name,'是',self.grade,'正在吃饭')

s1 = Students('张三','二年级')
# print(s1.study())
print(s1.eat())





# 1.使用类名调用
# print(Students.name)
# print(Students.grade)
#
# # 2.通过示例化对象调用
# print("="*20)
#
# s1 = Students()
# print(s1.name)
# print(s1.grade)

# s1 = Students()
# print(s1)
# s1.name = '张三'
# s1.grade = '5'
# print(s1.study())

