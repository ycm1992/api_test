# -*- coding:utf-8 -*-
# @Time:2019/5/12 21:06
# @Author:chuanman.yu
# @Email:1165358716@qq.com
# @File:get_data.py
# Software:PyCharm


class GetData:

    """可以用来动态得获取，删除，更改数据"""
    cookie = None
    loanid = None

# 类属性


# print(GetData.cookie)
# print(GetData().cookie)

# 类得反射可以动态得查看，增加，删除，更改类得属性或者实例得属性
# 利用反射获取值：第一个参数是类名，第二个参数是属性得参数名
# print(getattr(GetData, "cookie"))
# 判断是否有该属性，返回布尔值
# print(hasattr(GetData, "cookie"))
# 添加属性:类名，属性参数名，属性值
# setattr(GetData, "cookie", "12345")
# print(getattr(GetData, "cookie"))
# 删除属性
# delattr(GetData, "cookie")
# print(getattr(GetData, "cookie"))