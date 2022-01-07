"""
Author: xtrs
二级窗口
"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
from setting import Setting as s


class SecWin(QWidget):
    """
    二级窗口接口
    """

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

    @staticmethod
    def cfg_to_ui(expr, self, func_str):
        """
        将 config变量 变动 更新到 ui 中
        :param expr: 寻址（节点）表达式
        :param self: 窗口实例
        :param func_str: 设置状态的方法字符串
        """
        # eval()只能执行表达式 ， exec() 如果使用了global，第一个参数必须写进字典里+++++++++++++++++++++++！坑！
        config = s.get_config(expr)
        if len(config) == 1:
            config = config[0]
        for config_ in config:
            name = config_['name']
            value = config_['value']
            # setText(QString)要执行 value不能为空，否则相当于没有参数！！！！++++++++++++++++++++++++++！坑！
            if value != '':
                g = {'self': self}
                exec(f'x=self.{name}.{func_str}({value})', g)

    @staticmethod
    def ui_to_cfg(wid_s: list, self, func_str, win):
        """
        将 ui 变动 更新到 config变量 中
        :param wid_s: 控件列表
        :param self: 窗口实例
        :param func_str: 获取状态的方法字符串
        :param win: config中的窗口简称
        """
        # eval()只能执行表达式 ， exec() 如果使用了global，第一个参数必须写进字典里
        for wid in wid_s:
            name = wid.objectName()
            g = {'self': self}
            exec(f'x=self.{name}.{func_str}()', g)
            value = g['x']
            s.set_config(win, name, value)


if __name__ == '__main__':
    exec("""
print('你好')""")
