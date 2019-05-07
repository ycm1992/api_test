# -*- coding:utf-8 -*-
# @Time:2019/5/7 18:05
# @Author:chuanman.yu
# @Email:1165358716@qq.com
# @File:test11.py
# Software:PyCharm

import requests
param = {'mobilephone': '15921919560', 'pwd': '123456'}
resp = requests.get("http://test.lemonban.com/futureloan/mvc/api/member/register", params=param)
print(resp.text)