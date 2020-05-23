# -*- coding: utf-8 -*-
'''
@Time    : 2020/5/23 17:00
@Author  : s.xiao
@FileName: test05.py
@Software: PyCharm
使用pytorch框架实现低度下降法demo
优化器选择optim.GSD
'''

import torch
from torch import optim
import matplotlib.pyplot as plt

# 定义数据集
xs = torch.arange(0, 1, 0.01)  # 0-0.99，步长0.01共取100个数
ys = 2 * xs + 3 + torch.rand(100)  # 保持和xs形状一致，其中torch.rand（）是返回一个张量，
                                   # 包含了从区间[0, 1)的均匀分布中抽取的一组随机数


# 构建线性方程模型（类），从Moudule父类继承
class Line(torch.nn.Module):
    # 定义构造函数，通过父类实例化完成子类的构造函数
    def __init__(self):
        super(Line, self).__init__()
        # super().__init__()  一般写成这种形式更简洁
        # 模型初始化，构造模型系统参数
        self.w = torch.nn.Parameter(torch.rand(1)) # Parameter()中为tensor类型，通过torch.rand(1)构造一个随机参数值
        self.b = torch.nn.Parameter(torch.rand(1))

    # 重写父类方法forward，前向过程，返回数据输入后模型的结果
    def forward(self, x):
        return self.w * x + self.b


# 模型使用，实例化Line
line = Line()
# 定义优化器，使用SDG进行优化,lr步长0，momentum动量因子
opt = optim.SGD(line.parameters(), lr=0.1, momentum=0.1)
# opt = optim.Adam(line.parameters(), lr=0.1)
# 开启画板
plt.ion()

for epoch in range(60): # 轮次迭代
    for _x, _y in zip(xs, ys):
        # 将数据传入模型，通过forward（）前向过程计算返回结果
        z = line(_x)
        # 定义损失函数
        # loss = torch.nn.MSELoss()
        loss = (z-_y)**2
        # 梯度清空
        opt.zero_grad()
        # loss求导
        loss.backward()
        # 参数更新
        opt.step()
        print(line.w.item(), line.b.item(), loss.item())
        # 动态绘图
        plt.cla() # 清空画板
        plt.plot(xs, ys, ".")
        v = [line.w * e + line.b for e in xs]
        plt.plot(xs, v)
        plt.pause(0.01)

plt.ioff() # 关闭画板
plt.show()