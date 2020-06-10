# -*- coding: utf-8 -*-
'''
@Time    : 2020/5/22 23:47
@Author  : s.xiao
@FileName: test04.py
@Software: PyCharm
1.使用梯度下降法完成对一堆点的直线y=wx+b拟合
2.在原有demo基础上加入了动态画图
'''

import random
import matplotlib.pyplot as plt

# 构建数据集
_x = [i / 100 for i in range(100)]
_y = [2 * e + 3 + random.random() for e in _x]
# 随机生成w和b，最终w逼近3，b逼近4
w = random.random()
b = random.random()
plt.ion()  # 开启画图

for i in range(40):
    for x, y in zip(_x, _y):  # 通过zip函数同时从_x _y的list中取值
        z = w * x + b  # 将数据x输入到构建好的线性模型中得到输出，前向过程，推理过程
        o = z - y  # 损失
        loss = o ** 2  # 损失的正值处理，根据前向输出和标签得到损失

        # 通过梯度下降法对w和b求偏导寻找最小值
        dw = -2 * o * x  # 链式求导,注意取负让方向向下
        db = -2 * o
        l = 0.1  # 定义步长值
        w = w + l * dw  # 使用梯度下降法更新w值
        b = b + l * db
        print("w=", w, "; b=", b, "loss=", loss)

        # 动态画图过程，如果过于频繁可以放到轮次循环中
        plt.cla()  # 清空画板
        plt.title(loss)  # 加入标题，展示精度变化
        plt.plot(_x, _y, ".")  # 画出数据集_x _y
        v = [w * e + b for e in _x]
        plt.plot(_x, v)
        plt.pause(0.01)  # 睡眠0.01秒

plt.ioff()  # 关闭画图
plt.show()
