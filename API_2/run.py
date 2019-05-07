# --*-- coding=utf-8 --*--
# @File    : run.py
# @Time    : 2019-05-03 17:38
# @Author  : chuanman.yu
# @Email   : 1165358716@qq.com
# @Software: PyCharm


from API_1.common.http_request import HttpRequest
from API_1.common.do_excel import DoExcel
from API_1.common.project_path import case_path

test_data = DoExcel(case_path, "register").read_data()

for case in test_data:
    method = case["Method"]
    url = case["Url"]
    param = eval(case["Params"])
    print("开始测试")
    resp = HttpRequest().http_request(url=url, method=method, param=param)
    print("实际结果是{}".format(resp.json()))

    if resp.json() == eval(case["ExpectedResult"]):
        Test_Result = "PASS"
    else:
        Test_Result = "FAILED"
    print("该条测试用例结果是{}".format(Test_Result))

    t = DoExcel(case_path, "register")
    # 不能写入json格式，因为excel只能写入字符串和数字，所以用resp.text
    t.write_back(case["CaseId"]+1, 8, resp.text)
    t.write_back(case["CaseId"]+1, 9, Test_Result)
