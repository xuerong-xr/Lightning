"""
Author: xtrs
时间：2021/12/27
内嵌窗口_工具
"""
import abc
from embedded_wid import EmbWid


class ToolWid(EmbWid):
    """
    内嵌窗口_工具
    """
    def getChildren(self):
        """
        获取子控件
        :return:
        """

    def update_setting(self):
        """
        从配置文件读取 用户设置数据
        :return:
        """

    def bindSlots(self):
        """
        给子控件绑定槽函数
        :return:
        """
