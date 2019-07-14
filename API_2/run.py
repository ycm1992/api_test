# --*-- coding=utf-8 --*--
# @File    : run.py
# @Time    : 2019-05-03 17:38
# @Author  : chuanman.yu
# @Email   : 1165358716@qq.com
# @Software: PyCharm


import unittest
import time
import sys
sys.path.append("./")
import HTMLTestRunnerNew
from API_2.common.project_path import report_path
from API_2.test_cases.test_register import TestCases

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestCases))

now = time.strftime("%Y_%m_%d_%H_%M_%S")
report = report_path+"\\"+now+".html"
with open(report, "wb")as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                title='测试报告',
                                description='注册接口测试报告',
                                verbosity=2,
                                tester='chuanman.yu')
    runner.run(suite)
