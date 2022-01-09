"""
Author: xtrs
自定义Button
"""
from decimal import Decimal

from PyQt5.QtWidgets import QLineEdit
import PyQt5.QtGui as qui
import PyQt5.QtCore as qtc

import const


class UpDownEdit(QLineEdit):
    """
    提供 up down
    """
    signal1 = qtc.pyqtSignal()

    def __init__(self, parent=None):
        super(UpDownEdit, self).__init__(parent)
        self.setToolTip('按住W、S或者↑、↓以增减数值')
        # 装上验证器
        re_validator = qui.QRegExpValidator(qtc.QRegExp(const.SHAPES_SIZE))
        self.setValidator(re_validator)
        self.textChanged.connect(self.onTextChanged)
        self.editingFinished.connect(self.finished_edit)

    def init_ui(self):
        self.isUpDown = True
        self.num = Decimal(self.text())

    def keyPressEvent(self, a0: qui.QKeyEvent) -> None:
        key = a0.key()
        if key == qtc.Qt.Key_W:
            self.adjustNum(Decimal('0.1'))
            self.signal1.emit()
            # 不让editingFinished发射信号
            self.isUpDown = True
        elif key == qtc.Qt.Key_S:
            self.adjustNum(Decimal('-0.1'))
            self.signal1.emit()
            self.isUpDown = True
        super().keyPressEvent(a0)

    def keyReleaseEvent(self, a0: qui.QKeyEvent) -> None:
        key = a0.key()
        if key == qtc.Qt.Key_Up:
            self.adjustNum(Decimal('0.1'))
            self.signal1.emit()
            self.isUpDown = True
        elif key == qtc.Qt.Key_Down:
            self.adjustNum(Decimal('-0.1'))
            self.signal1.emit()
            self.isUpDown = True
        super().keyReleaseEvent(a0)

    def adjustNum(self, delta: Decimal):
        """
        只有 up down 会进来
        :param delta:
        :return:
        """
        temp = self.text()
        if not temp:
            temp = '0'
        # 记录调整之前的num
        self.num = Decimal(temp)
        num = self.num + delta
        if num >= 0:
            self.setText(str(num))

    def up_down_connect(self, func):
        self.signal1.connect(func)

    def onTextChanged(self):
        self.isUpDown = False

    def finished_edit(self):
        # 完成编辑时纠正不合规输入 TODO(优化算法)
        temp: str = self.text()
        if temp == '' or temp == '.':
            temp = '0'
            self.setText(temp)
        elif temp.endswith('.'):
            temp = temp.replace('.', '.0')
            self.setText(temp)
        elif temp.startswith('.'):
            temp = temp.replace('.', '0.')
            self.setText(temp)
        if self.isUpDown:
            print(f'{self.objectName()} 上一次编辑 是up down')

        else:
            print(f'{self.objectName()} 不是up down')
            self.signal1.emit()
            self.isUpDown = True

    def focusInEvent(self, a0: qui.QFocusEvent) -> None:
        self.num = Decimal(self.text())
        super(UpDownEdit, self).focusInEvent(a0)
