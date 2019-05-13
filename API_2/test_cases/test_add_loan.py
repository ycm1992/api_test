# --*-- coding=utf-8 --*--
# @File    : test_add_loan.py
# @Time    : 2019-05-13 21:26
# @Author  : chuanman.yu
# @Email   : 1165358716@qq.com
# @Software: PyCharm


import unittest
from ddt import ddt,data
from API_2.common.project_path import case_path
from API_2.common.http_request import HttpRequest
from API_2.common.do_excel import DoExcel
from API_2.common.my_log import Mylog
from API_2.common.get_data import GetData
from API_2.common.do_mysql import DoMysql

mylog = Mylog()
test_data = DoExcel(case_path, "add_loan").read_data("ADD_LOAN_CASE")

@ddt
class TestCases(unittest.TestCase):

    def setUp(self):
        self.t = DoExcel(case_path, "add_loan")

    def tearDown(self):
        pass

    @data(*test_data)
    def test_cases(self, case):
        global TestResult
        # global cookies
        method = case["Method"]
        url = case["Url"]
        if case["Params"].find("loanid") != -1:
            # 获取到的loanid值是int类型，replace时需要先转换为str
            param = eval(case["Params"].replace("loanid", str(getattr(GetData, "loanid"))))
        else:
            param = eval(case["Params"])
        mylog.info("------正在测试{}模块里面第{}条测试用例------".format(case["Module"], case["CaseId"]))
        mylog.info("测试数据是{}".format(case))
        resp = HttpRequest().http_request(method, url, param, cookies=getattr(GetData, "cookie"))
        if case["sql"] != None:
            loan_id = DoMysql().do_mysql(eval(case["sql"])["sql"])
            # 操作数据库获取的结果是元祖，所以取loan_id[0]
            setattr(GetData, "loanid", loan_id[0])
        if resp.cookies:
            # cookies = resp.cookies
            setattr(GetData, "cookie", resp.cookies)
        try:
            self.assertEqual(eval(case["ExpectedResult"]), resp.json())
            TestResult = "PASS"
        except AssertionError as e:
            TestResult = "FAILED"
            mylog.error("断言出错", e)
            raise e
        finally:
            self.t.write_back(case["CaseId"]+1, 9, resp.text)
            self.t.write_back(case["CaseId"]+1, 10, TestResult)

        mylog.info("实际结果是{}".format(resp.json()))


if __name__ == '__main__':
    unittest.main()
