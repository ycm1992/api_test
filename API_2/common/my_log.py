# -*- coding:utf-8 -*-
# @Time:2019/5/7 23:10
# @Author:chuanman.yu
# @Email:1165358716@qq.com
# @File:my_log.py
# Software:PyCharm


import logging
from API_2.common.read_config import ReadConfig
from API_2.common.project_path import conf_path, log_path


class Mylog:

    def __init__(self):
        self.logger_name = ReadConfig(conf_path).get_str_data('LOG', 'logger_name')
        self.logger_level = ReadConfig(conf_path).get_str_data('LOG', 'logger_level')
        self.file_level = ReadConfig(conf_path).get_str_data('LOG', 'file_level')
        self.stream_level = ReadConfig(conf_path).get_str_data('LOG', 'stream_level')
        self.formatter = ReadConfig(conf_path).get_str_data('LOG', 'formatter')

    def my_log(self, level, msg):
        my_logger = logging.getLogger(self.logger_name)
        my_logger.setLevel(self.logger_level)
        # 定义日志标准输出格式
        formatter = logging.Formatter(self.formatter)

        # console handler:输出控制台
        ch = logging.StreamHandler()
        # 设置级别
        ch.setLevel(self.stream_level)
        # 设置输出格式
        ch.setFormatter(formatter)

        # file handler:输出到文件
        fh = logging.FileHandler(log_path, encoding='utf-8')
        fh.setLevel(self.file_level)
        fh.setFormatter(formatter)

        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        elif level == 'CRITICAL':
            my_logger.critical(msg)

        # 一定要移除，不然会导致日志重复
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log('DEBUG', msg)

    def info(self, msg):
        self.my_log('INFO', msg)

    def warning(self, msg):
        self.my_log('WARNING', msg)

    def error(self, msg):
        self.my_log('ERROR', msg)

    def critical(self, msg):
        self.my_log('WARNING', msg)