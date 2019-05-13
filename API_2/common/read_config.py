# -*- coding:utf-8 -*-
# @Time:2019/5/7 23:27
# @Author:chuanman.yu
# @Email:1165358716@qq.com
# @File:read_config.py
# Software:PyCharm

from configparser import ConfigParser


class ReadConfig:

    def __init__(self, file_name):
        self.rc = ConfigParser()
        self.rc.read(file_name, encoding="utf-8")

    def get_int_data(self, section, option):
        return self.rc.getint(section, option)

    def get_float_data(self, section, option):
        return self.rc.getfloat(section, option)

    def get_boolean_data(self, section, option):
        return self.rc.getboolean(section, option)

    def get_str_data(self, section, option):
        return self.rc.get(section, option)

    def get_origin_data(self, section, option):
        return eval(self.rc.get(section, option))
