#!/usr/bin/env python
# encoding: utf-8

"""
@version: Python3.5
@author: Yang
@software: PyCharm
@file: setup.py
@time: 2017年1月26日0026 15:54

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
from distutils.core import setup
from deckee import version
setup(
    name='deckee',
    version=version,
    author='YangZhiyu',
    author_email='Decyzy@tongji.edu.cn',
    py_modules=['deckee'],
    # packages=['deckee.LogPrint'],
    description='测试模块',
)

# python setup.py sdist --format=gztar
