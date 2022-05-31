
import unittest

from work.demo003 import login

import sys


from work.HTMLTestRunner import HTMLTestRunner

class TestLogin(unittest.TestCase):

    # 初始化方法
    @classmethod
    def setUpClass(cls) -> None:
        print("开始运行方法",sys._getframe().f_code.co_name)

    # 清除方法
    @classmethod
    def tearDownClass(cls) -> None:
        print("开始运行方法",sys._getframe().f_code.co_name)


    # 初始化方法
    def setUp(self) -> None:
        print("开始运行方法",sys._getframe().f_code.co_name)

    # 清除方法
    def tearDown(self) -> None:
        print("开始运行方法", sys._getframe().f_code.co_name)

    def test_login_success(self):
        print("开始运行方法：",sys._getframe().f_code.co_name)
        except_value = 0
        actual_value = login("admin",'123456').get("code")
        self.assertEqual(except_value,actual_value)

    def test_user_wrong(self):
        print("开始运行方法：", sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login("abc", '123456').get("code")
        self.assertEqual(except_value, actual_value)

    def test_login_password_is_null(self):
        print("开始运行方法：", sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login("admin", '').get("code")
        self.assertEqual(except_value, actual_value)






if __name__ == '__main__':

    # 创建一个条件a
    suite_a = unittest.TestSuite()
    suite_a.addTest(TestLogin('test_login_success'))
    suite_a.addTest(TestLogin('test_user_wrong'))
    suite_a.addTest(TestLogin('test_password_is_null'))
    print(suite_a)

    # 创建一个测试报告文件.是HTML格式的
    test_report = './test_report.html'
    with open(test_report,'wb') as f:

        runner = HTMLTestRunner(f,title='测试报告',description='测试报告描述')
        runner.run(suite_a)



