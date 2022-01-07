"""
Author: xtrs
自定义数学计算模块
"""
import random
import string


def rand4words():
    """

    :return:
    """
    str_list = [random.choice(string.digits + string.ascii_letters+string.digits) for i in range(4)]
    random_str = ''.join(str_list)
    return random_str
