# --*-- coding=utf-8 --*--
# @File    : test_cases.py
# @Time    : 2019-05-05 12:06
# @Author  : chuanman.yu
# @Email   : 1165358716@qq.com
# @Software: PyCharm


import unittest
from ddt import ddt, data
from API_2.common.project_path import case_path
from API_2.common.http_request import HttpRequest
from API_2.common.do_excel import DoExcel

test_data = DoExcel(case_path, "register").read_data()


@ddt
class TestCases(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*test_data)
    def test_cases(self, case):
        method = case["Method"]
        url = case["Url"]
        param = eval(case["Params"])
        resp = HttpRequest().http_request(method, url, param)
        print("实际结果是{}".format(resp.json()))


