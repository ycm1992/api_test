# --*-- coding=utf-8 --*--
# @File    : learn_mysql.py
# @Time    : 2019-05-13 23:44
# @Author  : chuanman.yu
# @Email   : 1165358716@qq.com
# @Software: PyCharm


import pymysql

db_config = {"host": "test.lemonban.com",
                     "user": "test",
                     "password": "test",
                     "port": 3306,
                     "database": "future",
                     "charset": "utf8"
                     }

query = "select*from member where MobilePhone=15921919560"
cnn = pymysql.connect(**db_config)
cursor = cnn.cursor()
cursor.execute(query)
result = cursor.fetchone()
print(result)
