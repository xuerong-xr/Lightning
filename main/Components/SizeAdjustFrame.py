"""
Author: xtrs
调整尺寸大小 Frame
"""
from decimal import Decimal
from PyQt5.QtWidgets import QFrame
# noinspection PyUnresolvedReferences
from PyQt5.uic import loadUiType

# 加载UI
ui_SizeAdjustFrame, _ = loadUiType('../UI/SizeAdjustFrame.ui')


class SizeAdjustFrame(QFrame, ui_SizeAdjustFrame):
    """
    尺寸调整 Frame
    """

    def __init__(self, parent=None):
        super(SizeAdjustFrame, self).__init__(parent)
        self.setupUi(self)
        self.init_UI()

    def init_UI(self):
        print('SizeAdjustFrame收到信号')
        # edit
        self.edit_list = [self.w_edit, self.h_edit]
        [x.init_ui() for x in self.edit_list]
        self.bindslots()

    def bindslots(self):
        # 绑定 槽函数 edit up down 信号
        self.w_edit.up_down_connect(lambda: self.adjustAnother(0))
        self.h_edit.up_down_connect(lambda: self.adjustAnother(1))
        # 给btn绑定
        self.w_up_btn.clicked.connect(lambda: self.w_edit.adjustNum(Decimal('1')))
        self.w_down_btn.clicked.connect(lambda: self.w_edit.adjustNum(Decimal('-1')))
        self.h_up_btn.clicked.connect(lambda: self.h_edit.adjustNum(Decimal('1')))
        self.h_down_btn.clicked.connect(lambda: self.h_edit.adjustNum(Decimal('-1')))

    def adjustAnother(self, index):
        # TODO(处理精度问题，优化算法)
        if self.lockRatio_btn.isChecked():
            a_index = 1 ^ index
            wh = self.edit_list[index].num
            if wh:
                self.edit_list[a_index].setText(str(round(self.shapes_size[0] * self.shapes_size[1] / wh, 1)))
            # 如果是0 则同比例增长
            else:
                self.edit_list[a_index].setText(str(self.shapes_size[index]))

    @property
    def shapes_size(self):
        """
        返回当前 宽高
        :return:
        """
        temp_w = self.w_edit.text()
        temp_h = self.h_edit.text()
        width = Decimal(temp_w)
        height = Decimal(temp_h)
        return width, height
