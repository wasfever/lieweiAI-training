# -*- coding: utf-8 -*-
'''
@Time    : 2020/5/20 23:12
@Author  : s.xiao
@FileName: test01.py
@Software: PyCharm
'''

import numpy as np
import matplotlib.pyplot as plt


# 实现幂函数画图
def power_function():
    x = np.arange(-100, 100)
    # y = x**2
    # y = x**3
    y = x ** (-1)  # 注意x取值不能为0
    plt.plot(x, y)  # plot表示折线图
    plt.show()


# 实现常函数
def constant_function():
    x = np.arange(-10, 10)
    y = np.tile([3], x.shape)  # 广播，次数为x的长度
    plt.plot(x, y)
    plt.show()


# 指数函数
def exponential_function():
    x = np.arange(-5, 5, 0.1)
    y = 2 ** x
    y1 = 0.5 ** x
    plt.plot(x, y)
    plt.plot(x, y1)
    plt.show()


# 对数函数(重点掌握)
def logarithm_function():
    x = np.arange(0.1, 10, 0.1)
    y = np.log(x)  # 默认底数为e
    y2 = np.zeros_like(x)  # 画出y=0的直线
    # 通过换底公式换成以0.5为底数的对数
    y3 = np.log(x) / np.log(np.array(0.5))  # 通过np.array转换为数组

    plt.plot(x, y)
    plt.plot(x, y2)
    plt.plot(x, y3)
    plt.show()


# sigmoid函数 and tanh函数
def sigmoid_function():
    x = np.arange(-10, 10, 0.1)
    y = 1 / (1 + np.exp(-x))
    y1 = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
    y0 = np.zeros_like(x)
    plt.plot(x, y)
    plt.plot(x, y1)
    plt.plot(x, y0)
    plt.show()


# ReLU函数实现
def relu_function():
    x = np.arange(-10, 10, 0.1)
    y = np.where(x < 0, 0, x)
    y1 = np.where(x<0, -0.1, x)
    plt.plot(x, y)
    plt.plot(x,y1)
    plt.show()

if __name__ == '__main__':
    # power_function()
    # constant_function()
    # exponential_function()
    # logarithm_function()
    # sigmoid_function()
    relu_function()