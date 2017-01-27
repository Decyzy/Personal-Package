#!/usr/bin/env python
# encoding: utf-8

"""
@version: Python3.5
@author: Yang
@software: PyCharm
@file: save_data.py
@time: 2017年1月26日0026 16:09

code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏┓
           ┏┛┻━━━┛┻┓
          ┃   ☃   ┃
         ┃ ┳┛ ┗┳ ┃
        ┃   ┻   ┃
       ┗━┓   ┏━┛
        ┃   ┗━━━┓
       ┃神兽保佑 ┣┓
      ┃永无BUG！┏┛
     ┗┓┓┏━┳┓┓┏┛
     ┃┫┫  ┃┫┫
    ┗┻┛  ┗┻┛

"""
import pickle
import os
from colorama import init, Fore, Style, Back
import datetime
import sys
version = '0.2.3'
'''
格式：\033[显示方式;前景色;背景色m

说明：
前景色            背景色           颜色
---------------------------------------
30                40              黑色
31                41              红色
32                42              绿色
33                43              黃色
34                44              蓝色
35                45              紫红色
36                46              青蓝色
37                47              白色
显示方式           意义
-------------------------
0                终端默认设置
1                高亮显示
4                使用下划线
5                闪烁
7                反白显示
8                不可见

例子：
\033[1;31;40m    <!--1-高亮显示 31-前景色红色  40-背景色黑色-->
\033[0m          <!--采用终端默认设置，即取消颜色设置-->
'''
# 颜色大全
STYLE = {
    'fore': {   # 前景色
        'black': 30,  # 黑色
        'red': 31,  # 红色
        'green': 32,  # 绿色
        'yellow': 33,  # 黄色
        'blue': 34,  # 蓝色
        'purple': 35,  # 紫红色
        'cyan': 36,  # 青蓝色
        'white': 37,   # 白色
    },
    'back': {   # 背景
        'black': 40,  # 黑色
        'red': 41,  # 红色
        'green': 42,  # 绿色
        'yellow': 43,  # 黄色
        'blue': 44,  # 蓝色
        'purple': 45,  # 紫红色
        'cyan': 46,  # 青蓝色
        'white': 47,  # 白色
    },
    'mode': {   # 显示模式
        'mormal': 0,  # 终端默认设置
        'bold': 1,  # 高亮显示
        'underline': 4,  # 使用下划线
        'blink': 5,  # 闪烁
        'invert': 7,  # 反白显示
        'hide': 8,  # 不可见
    },
    'default': {'end': 0}
}


# 模块信息输出
def info():
    _info = '模块: deckee\n' + '版本: ' + version + '\n作者: YangZhiyu\nemail:Decyzy@tongji.edu.cn' + '''
模块包括:
==============================================
def save_data(var, filename, mode='normal'):
    保存用,var为需保存对象, filename为文件路径
    mode='ignore':不询问直接覆盖, mode='normal':询问后覆盖

def read_data(filename):
    读取函数,filename为文件路径
==============================================
日志打印模块:
LogPrint类:
    级别levels小:
        critical > error > warning > info > debug > notset(弃用)
    输出模式modes:
        simple: 时间+级别+信息
        normal: 时间+级别+函数名+信息
        detailed: 日期时间+级别+函数名+行号+信息
已初始化的实例log：
    log = LogPrint('debug', 'normal')
    打印级别为debug及以上，输出模式为'normal'
==============================================
'''
    return _info


# log级别判断装饰器
def call_level(func):
    def _call_level(args, message):
        if args.levels_control > args.levels[func.__name__.upper()]:
            return False
        else:
            func(args, message)
            return True
    return _call_level


# 函数调用日志记录装饰器
def log_debug_func_use(func):
    def _log_debug_func_use(*args, **kwargs):
        log.debug('执行函数' + str(func.__name__))
        return func(*args, **kwargs)
    return _log_debug_func_use


# 废弃，不支持win cmd输出，支持linux
def color_print(forecolor='black', backcolor='black', mode='bold'):
    return '\033[' + str(STYLE['mode'][mode]) + ';' + str(STYLE['fore'][forecolor]) + ';' \
          + str(STYLE['back'][backcolor]) + 'm'


# 日志打印基类，如:xxx = LogPrint('info', 'simple')
class LogPrint:
    levels = {
        'CRITICAL': 50,
        'ERROR': 40,
        'WARNING': 30,
        'INFO': 20,
        'DEBUG': 10,
        'NOTSET': 0
    }
    modes = {
        'simple': 0,
        'normal': 10,
        'detailed': 20
    }
    levels_control = levels['DEBUG']
    mode_control = modes['simple']
    symbolR = Fore.BLACK + ']' + Style.RESET_ALL
    symbolL = Fore.BLACK + '[' + Style.RESET_ALL

    def __init__(self, level='DEBUG', mode='normal'):
        self.levels_control = self.levels[level.upper()]
        self.mode_control = self.modes[mode]

    def print_time(self):
        if self.mode_control is self.modes['detailed']:
            return '[' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ']' + self.symbolL
        if self.mode_control is self.modes['normal']:
            return '[' + str(datetime.datetime.now().strftime("%H:%M:%S")) + ']' + self.symbolL
        if self.mode_control is self.modes['simple']:
            return '[' + str(datetime.datetime.now().strftime("%H:%M:%S")) + ']' + self.symbolL

    def line_get(self):
        try:
            raise Exception
        except:
            f = sys.exc_info()[2].tb_frame.f_back.f_back.f_back
            if self.mode_control is self.modes['detailed']:
                return self.symbolL + Fore.YELLOW + Style.BRIGHT + '%s,line:%s' % (f.f_code.co_name, f.f_lineno) + \
                       Style.RESET_ALL + self.symbolR
            if self.mode_control is self.modes['normal']:
                return self.symbolL + Fore.YELLOW + Style.BRIGHT + '%s' % f.f_code.co_name + Style.RESET_ALL + \
                       self.symbolR
            if self.mode_control is self.modes['simple']:
                return ''

    @call_level
    def debug(self, message):
        message = Fore.BLACK + Style.BRIGHT + message + Style.RESET_ALL
        time_now = Fore.BLACK + self.print_time() + Style.RESET_ALL
        level = Fore.BLACK + Style.BRIGHT + 'debug' + Style.RESET_ALL
        print(time_now + level + self.symbolR + self.line_get() + message)

    @call_level
    def info(self, message):
        message = Fore.CYAN + Style.BRIGHT + message + Style.RESET_ALL
        time_now = Fore.BLACK + self.print_time() + Style.RESET_ALL
        level = Fore.CYAN + Style.BRIGHT + 'info' + Style.RESET_ALL
        print(time_now + level + self.symbolR + self.line_get() + message)

    @call_level
    def warning(self, message):
        message = Fore.RED + Style.BRIGHT + message + Style.RESET_ALL
        time_now = Fore.BLACK + self.print_time() + Style.RESET_ALL
        level = Fore.RED + Style.BRIGHT + 'warning' + Style.RESET_ALL
        print(time_now + level + self.symbolR + self.line_get() + message)

    @call_level
    def error(self, message):
        message = Fore.BLACK + Style.BRIGHT + Back.RED + message + Style.RESET_ALL
        time_now = Fore.BLACK + self.print_time() + Style.RESET_ALL
        level = Fore.BLACK + Style.BRIGHT + Back.RED + 'error' + Style.RESET_ALL
        print(time_now + level + self.symbolR + self.line_get() + message)

    @call_level
    def critical(self, message):
        message = Fore.BLACK + Style.BRIGHT + Back.MAGENTA + message + Style.RESET_ALL
        time_now = Fore.BLACK + self.print_time() + Style.RESET_ALL
        level = Fore.BLACK + Style.BRIGHT + Back.MAGENTA + 'critical' + Style.RESET_ALL
        print(time_now + level + self.symbolR + self.line_get() + message)


# 日志实例
log = LogPrint('debug', 'normal')


# 保存函数
# mode='ignore':不询问直接覆盖, mode='normal':询问后覆盖
@log_debug_func_use
def save_data(var, filename, mode='normal'):
    filename = filename_correct(filename)
    if os.path.isfile(filename) is True:
        if mode is 'ignore':
            if save_data_simple(var, filename) is True:
                log.warning('已覆盖同名文件!')
            return True
        elif mode is 'normal':
            log.warning('该路径下已有同名文件!')
            log.info('是否覆盖？')
            # ch = input()
            ch = input_call()
            if ch is True:
                log.warning('正在覆盖旧文件。。。')
                return save_data_simple(var, filename)
            else:
                log.warning('文件\"' + filename + '\"未保存。')
                return False
        else:
            raise NameError
    else:
        return save_data_simple(var, filename)


# 简单保存函数(直接覆写)
@log_debug_func_use
def save_data_simple(var, filename):
    with open(filename, 'wb') as f:
        pickle.dump(var, f)
        log.info('文件\"' + filename + '\"成功保存!')
        return True


# 读取函数
@log_debug_func_use
def read_data(filename):
    try:
        with open(filename, 'rb') as f:
            dict1 = pickle.load(f)
            return dict1
    except FileNotFoundError:
        log.warning('文件不存在！位于打开\"' + str(filename) + '\"文件时')
        if filename[-4:] != '.pkl' and os.path.isfile(filename_correct(filename, 'ignore')) is True:
            filename = filename_correct(filename, 'ignore')
            log.info('尝试打开\"' + filename + '\"')
            if read_data(filename):
                log.info('\"' + filename + '\"' + '成功打开')
        return False


# mode='ignore':修正且不打印日志, mode='normal':修正打印日志
@log_debug_func_use
def filename_correct(filename, mode='normal'):
    if filename[-4:] == '.pkl':
        return filename
    else:
        if mode != 'ignore':
            log.info('文件\"' + filename + '\"已自动添加\".pkl\"后缀名')
        return filename + '.pkl'


# 询问函数，大小写不敏感，带检查输入合法性，y=Ture, n=False
@log_debug_func_use
def input_call():
    log.info('输入y/n或者Y/N')
    ch = input().upper()
    while ch != 'Y' or ch != 'N':
        if ch == 'Y':
            return True
        elif ch == 'N':
            return False
        log.warning('输入不合法！重新输入y/n或者Y/N')
        # print('输入不合法！')
        ch = input().upper()

if __name__ == '__main__':
    # def log_test():
    #     log.debug('debug')
    #     log.info('info')
    #     log.warning('waining')
    #     log.error('error')
    #     log.critical('critical')
    #     pass
    # print('日志打印测试')
    # print('simple')
    # log = LogPrint('debug', 'simple')
    # log_test()
    # print('normal')
    # log = LogPrint('debug', 'normal')
    # log_test()
    # print('detailed')
    # log = LogPrint('debug', 'detailed')
    # log_test()
    #
    # print('存读测试')
    # log = LogPrint('debug', 'simple')
    # a = 1
    # b = 2
    # read_data('测试')
    # save_data(b, 'sas')
    print(info())
