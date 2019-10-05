#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/10/4 21:36
@Author:  LQ
@Email: LQ65534@163.com
@File: get_veriy_img.py
@Software: PyCharm

本代码负责生成随机图片
参考地址 https://blog.csdn.net/ding_312/article/details/82258442
"""
import io
from PIL import ImageDraw
from PIL import ImageFont
from django.http import HttpResponse
from PIL import Image
import random
import os

base_dir = os.path.dirname(os.path.abspath(__file__))


# Create your views here.


# 获取随机颜色
def get_random_color():
    R = random.randrange(255)
    G = random.randrange(255)
    B = random.randrange(255)
    return (R, G, B)


def get_verify_img(request):
    # 定义画布背景颜色
    bg_color = get_random_color()
    # 画布大小
    img_size = (100, 38)
    # 定义画布
    # image = Image.new("RGB", img_size, bg_color)  # 动态改变背景
    image = Image.new("RGB", img_size, (232,240,254)) # 把背景定死
    # 定义画笔
    draw = ImageDraw.Draw(image, "RGB")
    # 创建字体（字体的路径，服务器路径）
    font_path = os.path.join(base_dir, "static", "data_process", "font", "AdobeArabic-BoldItalic.otf")
    # 实例化字体，设置大小是30
    font = ImageFont.truetype(font_path, 30)
    # 准备画布上的字符集
    source = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789"
    # 保存每次随机出来的字符
    code_str = ""
    for i in range(4):
        # 获取数字随机颜色
        text_color = get_random_color()
        # 获取随机数字 len
        tmp_num = random.randrange(len(source))
        # 获取随机字符 画布上的字符集
        random_str = source[tmp_num]
        # 将每次随机的字符保存（遍历） 随机四次
        code_str += random_str
        # 将字符画到画布上
        draw.text((10 + 20 * i, 5), random_str, text_color, font)
    # 记录给哪个请求发了什么验证码
    request.session['captcha'] = code_str

    # 使用画笔将文字画到画布上
    # draw.text((10, 20), "X", text_color, font)
    # draw.text((40, 20), "Q", text_color, font)
    # draw.text((60, 20), "W", text_color, font)

    # 获得一个缓存区
    buf = io.BytesIO()
    # 将图片保存到缓存区
    image.save(buf, 'png')
    # 将缓存区的内容返回给前端 .getvalue 是把缓存区的所有数据读取
    return HttpResponse(buf.getvalue(), 'image/png')
