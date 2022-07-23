#导包
import unittest
import time
import requests
from tools.HTMLTestRunner import HTMLTestRunner
from unittest_params import TPShopLogin
#封装测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TPShopLogin))
#制定报告路径
report = "./report/report-{}.html".format(time.strftime('%Y%m%d-%H%M%S'))
#打开文件流
with open(report,'wb') as f:
    #创建HTMLTESTRUNNER
    runner = HTMLTestRunner(f,title='tpshop接口测试报告')
    #执行测试套件
    runner.run(suite)