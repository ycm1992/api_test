# --*-- coding=utf-8 --*--
# @File    : http_request.py
# @Time    : 2019-05-04 11:39
# @Author  : chuanman.yu
# @Email   : 1165358716@qq.com
# @Software: PyCharm


import requests


class HttpRequest:

    def http_request(self, method, url, param, cookies):

        global resp
        if method.upper() == "GET":
            try:
                resp = requests.get(url, params=param, cookies=cookies)
            except Exception as e:
                print("get请求出错了：".format(e))
        elif method.upper() == "POST":
            try:
                resp = requests.post(url, data=param, cookies=cookies)
            except Exception as e:
                print("post请求出错了：".format(e))
        else:
            print("不支持该种请求方式")
            resp = None

        return resp


if __name__ == '__main__':
    method = "get"
    url = "http://47.107.168.87:8080/futureloan/mvc/api/member/register"
    param = {"mobilephone": "15921919560", "pwd": "123456"}
    result = HttpRequest().http_request(method, url, param)
    print(result.headers)
