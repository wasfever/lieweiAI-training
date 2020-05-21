# -*- coding: utf-8 -*-
'''
@Time    : 2020/5/21 23:47
@Author  : s.xiao
@FileName: test03.py
@Software: PyCharm
使用梯度下降法完成对一堆点的直线y=wx+b拟合
'''

import random
import matplotlib.pyplot as plt

# 构建数据集
_x = [i / 100 for i in range(100)]
_y = [3 * e + 4 + random.random() for e in _x]
# 随机生成w和b，最终w逼近3，b逼近4
w = random.random()
b = random.random()

for i in range(30):
    for x, y in zip(_x, _y):  # 通过zip函数同时从_x _y的list中取值
        z = w * x + b  # 构造拟合曲线
        o = z - y  # 损失
        loss = o ** 2  # 损失的正值处理
        # 通过梯度下降法对w和b求偏导寻找最小值
        dw = -2 * o * x  # 链式求导,注意取负让方向向下
        db = -2 * o
        l = 0.1  # 定义步长值
        w = w + l * dw  # 使用梯度下降法寻找w值
        b = b + l * db
        print("w=", w, "; b=", b, "loss=", loss)

plt.plot(_x, _y, ".")  # 画出数据集_x _y
v = [w * e + b for e in _x]
plt.plot(_x, v)
plt.show()
