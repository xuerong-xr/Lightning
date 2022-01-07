"""
Author: xtrs
主窗口
立项时间：2021年12月2日
开发时间：2021年12月6日-
"""
from PyQt5 import QtCore as qtc
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main import UI
from setting import Setting as s
from set_dia import SettingWin


class LightningWin(QMainWindow, UI.ui):
    """
    主窗口类
    """
    signal_forChildren = qtc.pyqtSignal()

    def __init__(self):
        QMainWindow.__init__(self)
        # self.getConfig()
        self.setupUi(self)
        self.ui_init()
        self.handle_btn()

    def ui_init(self):
        """
        载入界面时，导入用户数据处理界面初始化
        :return:
        """
        print('lightning ui_init')
        self.signal_forChildren.emit()

    def handle_ui_change(self):
        """
        处理页面变化
        :return:
        """

    def handle_btn(self):
        """
        绑定btn事件
        :return:
        """
        self.action_top_show.triggered.connect(lambda: self.action_setInd(0))
        self.action_AS.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.action_smh.triggered.connect(lambda: self.action_setInd(1))

    def action_setInd(self, index):
        """
        action_top_show
        """
        self.stackedWidget.setCurrentIndex(index)

    def slot_statusBar(self):
        self.statusbar.showMessage('Ready', 3000)
        pass

    def closeEvent(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        print('close')
        # s.dumpConfig_local('config.json')


if __name__ == '__main__':
    qtc.QCoreApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling)
    app = QApplication([])
    translator = qtc.QTranslator()
    translator.load('../qm/qt_zh_CN.qm')
    app.installTranslator(translator)
    lt_win = LightningWin()
    set_win = SettingWin()
    lt_win.show()
    lt_win.Btn_aS_exec.clicked.connect(set_win.show)
    app.exec_()
