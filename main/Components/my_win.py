"""
Author: xtrs
自定义窗口父类
"""
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication


class MyWin(QMainWindow):
    """
    自定义窗口
    """

    def __init__(self):
        super(MyWin, self).__init__()
        self.isMoving = None
        self.start_point = None
        self.window_point = None

    def mousePressEvent(self, e):
        """

        :param e:
        """
        if e.button() == QtCore.Qt.LeftButton:
            self.isMoving = True
            self.start_point = e.globalPos()
            self.window_point = self.frameGeometry().topLeft()

    def mouseMoveEvent(self, e):
        """

        :param e:
        """
        if self.isMoving:
            rel_pos = e.globalPos() - self.start_point  # QPoint 类型可以直接相减
            self.move(self.window_point + rel_pos)  # 所以说 Qt 真是赞！

    def mouseReleaseEvent(self, e):
        """

        :param e:
        """
        self.isMoving = False


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication([])
    lt_win = MyWin()
    lt_win.show()
    app.exec_()
