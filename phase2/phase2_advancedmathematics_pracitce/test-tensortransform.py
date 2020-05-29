# -*- coding: utf-8 -*-
'''
@Time    : 2020/5/24 22:33
@Author  : s.xiao
@FileName: test-img.py
@Software: PyCharm
1使用torch完成对tensor的相关操作
'''

import torch

a = torch.rand(1, 3, 5, 4)
print(a, "\n", a.shape)
# 换轴操作，注意参数为元祖
b = a.permute((1, 0, 3, 2))
print(b.shape)
