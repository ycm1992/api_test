# --*-- coding=utf-8 --*--
# @File    : project_path.py
# @Time    : 2019-05-04 21:18
# @Author  : chuanman.yu
# @Email   : 1165358716@qq.com
# @Software: PyCharm


import os


project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
case_path = os.path.join(project_path, "test_cases", "api_test.xlsx")
print(case_path)
