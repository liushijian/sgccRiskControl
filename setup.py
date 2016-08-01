#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="sgccRiskControl",
    version="0.1.2",
    packages=find_packages(),
    zip_safe=False,
    description="sgcc risk control data process",
    long_description="sgccRiskControl is package specific for risk control in state grid cooperation of China",
    author="Wang Qi,Li Zhiyun",
    author_email="wangalexqi@126.com",
    install_requires=['pandas','openpyxl'],
    license="MIT",
    keywords=["sgcc", "risk","control"],
    url="https://pypi.python.org/pypi",
)