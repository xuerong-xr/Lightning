"""
Author: xtrs
主要的四大功能模块管理界面
"""
from PyQt5.QtWidgets import *
from main.Components.MyFrame import MyFrame
from user_wid import UserWid


class ModuleWid(UserWid):
    """
    主要的四大功能 模块管理控件
    """

    def __init__(self, parent=None):
        super(ModuleWid, self).__init__(parent)

    def ui_init_slot(self):
        """
        接收主界面载入完成之后发射的信号 【槽】
        :return:
        """
        super(ModuleWid, self).ui_init_slot()

    def getChildren(self):
        """
        获取子控件
        :return:
        """
        # QStackWidget
        self.staWid_module = self.findChild(QStackedWidget, 'staWid_module')

        # 自定义Frame 四大功能 按钮
        # TODO(突然不能识别提升的自定义类)
        self.fra_user_tem = self.findChild(QFrame, 'fra_user_tem')
        self.fra_user_data = self.findChild(QFrame, 'fra_user_data')
        self.fra_user_pho = self.findChild(QFrame, 'fra_user_pho')
        self.fra_user_tool = self.findChild(QFrame, 'fra_user_tool')
        self.fra_user_tem.setChecked(True)

        self.listWid_tag = self.findChildren(QListWidget)[0]
        self.listWid_strip = self.findChildren(QListWidget)[1]

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
        # MyFrame按钮
        self.fra_user_tem.connect_clicked(lambda: self.set_staWid_module_index(0))
        self.fra_user_data.connect_clicked(lambda: self.set_staWid_module_index(1))
        self.fra_user_pho.connect_clicked(lambda: self.set_staWid_module_index(2))
        self.fra_user_tool.connect_clicked(lambda: self.set_staWid_module_index(3))

    def set_staWid_module_index(self, index):
        self.staWid_module.setCurrentIndex(index)

    def import_item(self):
        pass

    def update_item(self):
        pass

    def getAllStrip(self):
        self.listWid_strip.add_itemAdd()
        print('我是getAllStrip')

    def filterStrip(self, index):
        # TODO(先做完生成模板界面，再做导入界面)
        # 考虑导入的流程 怎样节省内存
        print(index)