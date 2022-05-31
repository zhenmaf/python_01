




# 方法：从文件中读取数据，返回的是列表形式的数据
def from_file_get_data(file_name):

    try:
        f = open(file_name,'r')
        line = f.readline()
        user_data = eval(line)
        return user_data
    except Exception as e:
        print(e)
    finally:
        if not f :
            f.close()

# 方法：向文件中写入内容，用户添加的信息是在原来基础上添加的

def save_date(file_name,file_content):
    f = None
    try:
        f = open(file_name,'w')
        f.write(str(file_content))
    except Exception as e:
        print(e)
    finally:
    if not f:
        f.close()





# 定义用户默认数据 : [a1,a2]
# user_list = [{'role':'admin','account':'admin','password':'123456','dept':'tester'},{'role':'user','account':'dev','password':'123456','dept':'dev'}]

"""
值if 表达式1 else 表达式2
"""
user_list = []
user_list = user_list if user_list else from_file_get_data(r'D:\py\python_01\work\a.log')

# 定义默认返回结果
result = {"code":0,"message":""}
login_status = 0

# 定义登录功能
def login(username,password):
    # 用户名或密码为空的情况
    if username is None or username == "":
        result.update({"code":1,"message":"用户名不能为空"})
        return  result
    if password is None or password == "":
        result.update({"code": 1, "message": "密码不能为空"})
        return result
    # 登录成功的情况
    for user_info in user_list:
        if username == user_info.get('account') and password == user_info.get('password'):
            result.update({"message": "登录成功!", "user_list": user_list})
            login_status = 1
            return result
    # 用户名和密码不匹配的情况
    result.update({"code":1,"message":"用户或密码输入错误"})
    return result

# 创建一个类，包括新增用户，修改用户，删除用户，查询用户
class User():

    # 构造方法
    def __init__(self):
        global login_status
        self.result = result
        self.user_lst = copy.deepcopy(user_list)

    # 添加用户的方法
    def add_user(self, username, password='123456', **kwargs):
        user_dict = {}
        user_dict['account'] = username
        user_dict['password'] = password
        user_dict.update(**kwargs)
        # 将组装的数据添加到用户列表中
        user_list.append(user_dict)
        save_data('user_data.txt', user_list)
        self.result = {"code": 20, "message": "用户添加成功",
                       "add_time": datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')}
        return self.result


# 用户查询功能
def get_user(username):

    # 判断用户名是否登录，若登录成功可以进行查询，若登录失败，返回权限不足
    if not result.get('code'):
        result.update({"code":11,"message":"用户没登录，无法查询出结果"})
        return result
    # 输入正确用户名进行查询，返回结果（支持模糊查询）
    result.update({"user_list":[]})
    lst = []            # 存放的是查询到的结果的数据
    for x in user_list:
        account = x.get('account')
        if username in account:      # 支持模糊查询
            x.pop('password')
        lst.append(x)


    # 判断新列表里的数据，如果列表不为空，查询成功，返回对应的结果
    if lst:
        result.update({"message":"查询用户成功","user_list":lst})
        return result


    # 若输入的用户名不正确 ，返回无查询结果提示
    self.result = {"code": 12, "message": "未查到用户，请重新输入"}
    return self.result

if __name__ == '__main__':

    # 1.进行循环，以及用户各种操作
    flag = True

    while flag:

        # 提供用户各种选择，比如输入1代表登录操作，输入2代表查询操作，输入q代表退出操作
        vls = input("操作请输入对应编号:"
              "\n 1:) 进行登录 :"
              "\n 2:) 进行查询用户，请输入用户名:"
              ""
              "\n q:) 退出操作:"
              "\n 其他字符:) 未知操作，请重新输入: ")

        # 当输入未知符号后，进行重新输入
        if not vls in ('1','2','q','quit'):
            print("="*30)
            continue
        # 进行登录操作
        if vls == '1':
            username = input("请输入用户名:")
            password = input("请输入密码:")
            login_resylt = login(username,password)
            print(login_resylt)
            print("="*30)
            continue


        # 进行查询用户的情况
        if vls == '2':
            name = input("请输入查询用户名：")
            get_result = get_user(name)
            print(get_result)
            print("="*30)
            continue

        # 是否退出
        if vls in ('q','quit'):
            flag = False
            print("退出成功！")








