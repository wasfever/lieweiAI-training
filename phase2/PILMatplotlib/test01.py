# -*- coding: utf-8 -*-
'''
@Time    : 2020/6/17 21:00
@Author  : s.xiao
@FileName: test01.py
@Software: PyCharm
PIL基本操作
'''

from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

img = Image.open(r"image/person.jpg")  # 此处为相对路径,'r'表示取消转义
img.show()  # 以系统默认图片查看器显示
# plt.imshow(img)
# plt.show()

w, h = img.size
print(w, h)
#缩放图片，在原图上采样
img3 = img.resize((w//2, h//2))
# img.show()
#等比缩放，建立复制重新采样
img2 = img.thumbnail((w//3, h//3),resample=Image.ANTIALIAS)  #抗锯齿
# img.show()
#抠图
img1 = img.crop((100,100,450,450))
img1.show()
#旋转
img.rotate(15) # 从0°开始向180°旋转15°
#滤波器 imagefilter
imgf = Image.open(r"image/minons.jpeg")
# img = img.filter(ImageFilter.CONTOUR)
# img.show()
# img = img.filter(ImageFilter.BLUR)
# img.show()
# img = img.filter(ImageFilter.BoxBlur(radius=20))
# img.show()
# img = img.filter(ImageFilter.DETAIL)
# img.show()
# img = img.filter(ImageFilter.EMBOSS)
# img.show()
# img = img.filter(ImageFilter.EDGE_ENHANCE)
# img.show()

#加入logo，贴图
# logo = Image.open("image/horse.jpg")
# logo = logo.resize((60,60),resample=Image.ANTIALIAS)
# img.paste(logo,(100,100))
# img.show()