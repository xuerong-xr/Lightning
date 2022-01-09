"""
Author: xtrs
二级窗口
"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor


class SecWin:
    """
    二级窗口接口
    """
    config_j = {}

    def ui_init_slot(self):
        """
        接收界面载入信号 【槽】
        :return:
        """
        print('我是secWin实例方法 ui_init_slot')
        # 1.获取子控件
        self.getChildren()
        # 2.更新各控件用户配置信息
        self.update_setting()
        # 3.给各控件绑定槽函数
        self.bindSlots()

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

    @staticmethod
    def render_shadow_child(wid: QWidget, offset=(0, 0), radius=20, color=(128, 128, 255)):
        """
        设置阴影
        :param wid: 控件
        :param offset: 偏移量
        :param radius: 阴影半径
        :param color: 颜色
        """
        wid.shadow = QGraphicsDropShadowEffect(wid)  # 设置阴影
        wid.shadow.setOffset(offset[0], offset[1])  # 偏移
        wid.shadow.setBlurRadius(radius)  # 阴影半径
        wid.shadow.setColor(QColor(color[0], color[1], color[2]))  # 阴影颜色
        wid.findChild(QFrame).setGraphicsEffect(wid.shadow)  # 将设置套用到widget窗口中

    @staticmethod
    def render_shadow_self(wid: QWidget, offset=(0, 0), radius=20, color=(128, 128, 255)):
        """
        设置阴影
        :param wid: 控件
        :param offset: 偏移量
        :param radius: 阴影半径
        :param color: 颜色
        """
        parent = wid.parent()
        parent.shadow = QGraphicsDropShadowEffect(wid)  # 设置阴影
        parent.shadow.setOffset(offset[0], offset[1])  # 偏移
        parent.shadow.setBlurRadius(radius)  # 阴影半径
        parent.shadow.setColor(QColor(color[0], color[1], color[2]))  # 阴影颜色
        wid.setGraphicsEffect(parent.shadow)  # 将设置套用到widget窗口中


if __name__ == '__main__':
    exec("""
print('你好')""")
