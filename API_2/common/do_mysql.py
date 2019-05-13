# -*- coding:utf-8 -*-
# @Time:2019/5/12 23:13
# @Author:chuanman.yu
# @Email:1165358716@qq.com
# @File:do_mysql.py
# Software:PyCharm

import pymysql
from API_2.common.read_config import ReadConfig
from API_2.common.project_path import conf_path


class DoMysql:

    def do_mysql(self, query, flag=1):
        """
        :param query: 查询语句
        :param flag: 1：获取一条数据，2：获取所有数据
        :return: 查询结果
        """
        db_config = ReadConfig(conf_path).get_origin_data("DB", "db_config")
        cnn = pymysql.connect(**db_config)
        cursor = cnn.cursor()
        cursor.execute(query)
        if flag==1:
            result = cursor.fetchone()
        else:
            result = cursor.fetchall()
        return result


if __name__ == '__main__':
    query = "select max(Id) from loan where MemberID=1248"
    print(DoMysql().do_mysql(query))


