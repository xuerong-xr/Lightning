"""
Author: xtrs
测试用
"""
# from PyQt5.QtWidgets import *
#
#
# def __setUI(self):
#     # TODO(设置样式)
#     # 外层 layout
#     self.layout_out = QGridLayout()
#     self.layout_out.setSpacing(0)
#     # 外层 QFrame
#     self.frame_out = QFrame()
#     # 把上面两者依次添加上
#     self.layout_out.addWidget(self.frame_out)
#     self.setLayout(self.layout_out)
#
#     # 第二层 垂直布局 套 两个水平布局
#     self.layout_main = QVBoxLayout()
#     self.layout_first = QHBoxLayout()
#     self.layout_second = QHBoxLayout()
#     self.layout_third = QHBoxLayout()
#     # 依次添加上
#     self.layout_main.addLayout(self.layout_first)
#     self.layout_main.addLayout(self.layout_second)
#     self.layout_main.addLayout(self.layout_third)
#     self.frame_out.setLayout(self.layout_main)
#     # 设置外边距
#     self.layout_main.setContentsMargins(10, 4, 10, 4)
#     self.layout_main.setSpacing(2)
#
#     # 第一个布局top 加入lab
#     self.lab = QLabel('我是item的name')
#     self.layout_first.addWidget(self.lab, Qt.AlignCenter)
#
#     # 加入toolBtn
#     self.starLab = StarLab('星')
#     self.starLab.setFixedSize(26, 26)
#     self.layout_first.addWidget(self.starLab, Qt.AlignCenter)
#     self.starLab.connect_clicked_slot(lambda: print(self.starLab.isChecked))
#
#     # 第二个布局bottom 加入三个LabBtnVerFrame
#     self.verFrameLabBtn_s = [LabBtnVerFrame(), LabBtnVerFrame(), LabBtnVerFrame()]
#     [self.layout_third.addWidget(x) for x in self.verFrameLabBtn_s]
#
#     # 第三个布局加入两个lab
#     self.lab_editTime = QLabel('上次编辑时间：')
#     self.lab_useTime = QLabel('上次使用时间：')
#     self.layout_second.addWidget(self.lab_editTime)
#     self.layout_second.addWidget(self.lab_useTime)
#
#     # 添加右键菜单
#     self.contextMenu = StripLWItemRightMenu(self)
#     self.contextMenu.request_menu_bind(self.exec_menu)
#
#     # 设置整体样式
#     self.setStyleSheet('*{font-family:"华文新魏"}')
#     self.render_smaller()
