#!-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
import unittest,time
# 引入HTMLTestRunner包
import HTMLTestRunner

# 导入公共的类
from package import common
from package import function
from package import member
from data import testdata


class TestHome(unittest.TestCase):
    u'''首页'''
    def setUp(self):
        # 启动浏览器
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1280,800)
        # 设置隐式时间等待
        self.driver.implicitly_wait(5)


    def test01_home(self):

        u'''首页概览'''
        function.login_shanghu(self.driver, testdata.login_url, testdata.username, testdata.password)
        time.sleep(2)

        # 断言判断登录后导航栏首页概览
        homepage = common.findXpath(self.driver, '/html/body/div[1]/div[1]/ul/li[1]/a').text
        self.assertEqual(homepage, "首页概览")

    def test02_menu(self):

        u'''左侧菜单检查'''
        function.login_shanghu(self.driver, testdata.login_url, testdata.username, testdata.password)
        time.sleep(2)

        # 菜单检查
        function.open_menu(self.driver,u"会员功能",u"会员管理")
        function.open_menu(self.driver,u"会员功能",u"会员集点")
        function.open_menu(self.driver,u"会员功能",u"会员红包")
        function.open_menu(self.driver,u"会员功能",u"会员储值")
        function.open_menu(self.driver,u"交易管理","")
        function.open_menu(self.driver,u"账单管理","")
        function.open_menu(self.driver,u"公众号授权","")
        function.open_menu(self.driver,u"账户信息","")
        function.open_menu(self.driver,u"首页概览","")

        function.logout(self.driver)


    def tearDown(self):
        driver=self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()