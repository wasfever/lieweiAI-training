# -*- coding: utf-8 -*-
'''
@Time    : 2020/6/20 19:50
@Author  : s.xiao
@FileName: test02verificationcode.py
@Software: PyCharm
验证码生成
'''
import random
from PIL import Image, ImageDraw, ImageFont


class GenerateCode():
    # 设定验证码内容
    def getcode(self):
        # ASIC码从65-90为A-Z
        char = chr(random.randint(65, 90))
        return char

    # 设定前景色,按照RGB取色，返回三元组
    def fr_color(self):
        return (random.randint(0, 168),
                random.randint(0, 168),
                random.randint(0, 168))

    # 背景色与前景色设置相同，只要颜色有差距即可
    def bg_color(self):
        return (random.randint(160, 255),
                random.randint(160, 255),
                random.randint(160, 255))

    # 验证码生成
    def gen_pic(self):
        # 定义画板长、宽w，h
        w, h = 240, 60
        img = Image.new(mode="RGB", size=(w, h), color=(255, 255, 255))
        # 定义画笔
        draw = ImageDraw.Draw(img)
        # 定义字体
        font = ImageFont.truetype(font="Inkfree.ttf", size=35)
        # 画背景
        for y in range(h):
            for x in range(w):
                draw.point((x, y), fill=self.bg_color())
        for i in range(4):
            draw.text((60 * i + 20, 10), text=self.getcode(), fill=self.fr_color(), font=font)
        # 使用PIL画矩形
            draw.rectangle((20,10,45,45),outline="red")
        img.show()
        # img.save()


g = GenerateCode()
g.gen_pic()
