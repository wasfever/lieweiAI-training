# -*- coding: utf-8 -*-
'''
@Time    : 2020/5/21 23:08
@Author  : s.xiao
@FileName: test02.py
@Software: PyCharm
'''
import torch
import numpy as np
x = torch.tensor([3.0], requires_grad=True)
y = x ** 3
y.backward()  #对y进行求导
print(x.grad) #打印出X的梯度

