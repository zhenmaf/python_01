


# 类的继承
class People():

    age = 0

    def eat(self,people_type):
        print(people_type,'正在吃饭')

class Students(People):

    def eat(self,grade):
        super().eat(grade)
        print(grade,"学生正在吃饭")


class Teacher(People):

    def eat(self,subject,time):
        print("{}的老师在{}时间吃饭".format(subject,time))


s = Students()
s.eat('二年级')
Students.age = '20'
print(Students.age)

t = Teacher()
t.eat('语文','12:00')
Teacher.age = '40'
print(Teacher.age)
