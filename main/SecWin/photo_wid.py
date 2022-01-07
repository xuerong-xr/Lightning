"""
Author: xtrs
时间：2021/12/27
内嵌窗口_照片
"""
from embedded_wid import EmbWid


class PhotoWid(EmbWid):
    """
    内嵌窗口_照片
    """

    def ui_init_slot(self):
        """
        接收主界面载入完成之后发射的信号 【槽】
        :return:
        """
        print('我是父类方法')

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
