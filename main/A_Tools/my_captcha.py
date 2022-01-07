"""
Author: xtrs
自定义验证码模块
"""
from captcha.image import ImageCaptcha


def createCaptcha(*args: str):
    """
    创建校验码（验证码）
    :param args: 要创建的字符串元祖
    :return: 创建好的图片数组
    """
    images = []
    for arg in args:
        images.append(ImageCaptcha().generate_image(arg))
    return images
