# -*- coding: utf-8 -*-
'''
@Time    : 2020/5/24 22:33
@Author  : s.xiao
@FileName: test-img.py
@Software: PyCharm
1使用numpy完成对图像的数据展示,将图像转为向量
'''

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("pic.jpg")  # 使用Image.open方法打开pic.jpg
# img.show()  也使用默认图像浏览器打开图像
plt.imshow(img)
plt.show()

img_data = np.array(img)
print(img_data)
print(img_data.shape)  # 打印该图像数据的形象
