# -*- coding: utf-8 -*-
'''
@Time    : 2020/6/12 23:10
@Author  : s.xiao
@FileName: test01.py
@Software: PyCharm
全连接拟合非线性问题
'''

import torch
from torch import nn
import matplotlib.pyplot as plt
import torch.nn.functional as F  # 导入集合函数等

# 数据构造 y = x ³
# x = torch.arange(-10.0, 10.0)  #由于维度不同无法直接在神经网络中计算需要升维
x = torch.unsqueeze(torch.arange(-10.0, 10.0), dim=1)  # [20,1]  [批次,数据形状] [N, V]
y = x.pow(3)


# plt.plot(x, y, ".")  # 一般用于折线图
# plt.scatter(x, y)  # 一般用于曲线图
# plt.show()

class Net(nn.Module):
    # 构造函数
    def __init__(self):
        super(Net, self).__init__()
        # 1.注意是Parameter
        # 2.注意randn表示为标准正态分布
        # 3.注意w的形状与x必须相同
        self.w1 = nn.Parameter(torch.randn(1, 24))  # 24表示为第一层神经元的个数
        self.b1 = nn.Parameter(torch.zeros(24))  # 偏移量b个数与该层神经元个数相同,初始值为0

        self.w2 = nn.Parameter(torch.randn(24, 64))
        self.b2 = nn.Parameter(torch.zeros(64))

        self.w3 = nn.Parameter(torch.randn(64, 128))
        self.b3 = nn.Parameter(torch.zeros(128))

        self.w4 = nn.Parameter(torch.randn(128, 64))
        self.b4 = nn.Parameter(torch.zeros(64))
        # 注意关注结果的形状
        self.w5 = nn.Parameter(torch.randn(64, 1))
        self.b5 = nn.Parameter(torch.zeros(1))

    # 正向传输函数
    def forward(self, x):
        fc1 = F.relu(torch.matmul(x, self.w1) + self.b1)
        fc2 = F.relu(torch.matmul(fc1, self.w2) + self.b2)
        fc3 = F.relu(torch.matmul(fc2, self.w3) + self.b3)
        fc4 = F.relu(torch.matmul(fc3, self.w4) + self.b4)
        fc5 = torch.matmul(fc4, self.w5) + self.b5  # 最后一层的输出不加入relu激活函数
        return fc5


if __name__ == '__main__':
    net = Net()
    # 优化器选择Adam
    optim = torch.optim.Adam(net.parameters(), lr=0.1)
    # 损失函数选择MSELoss（均方损失函数）返回的 loss 结果都是维度为 (batch_size, ) 的向量
    loss_func = nn.MSELoss()
    # 开启画板
    plt.ion()

    for epoch in range(1000):
        out = net(x)
        loss = loss_func(out, y)

        optim.zero_grad()  # 清空梯度
        loss.backward()  # 反向求导
        optim.step()  # 梯度更新

        if epoch % 5 == 0:  # 每5轮画图一次
            plt.cla()  # 清空画板
            plt.scatter(x, y)  # 画出x，y的原始曲线
            plt.plot(x, out.detach().numpy(), 'r')  # 画出输出
            plt.pause(0.1)
            print(loss.item())

    plt.ioff()  # 关闭画板
    plt.show()
