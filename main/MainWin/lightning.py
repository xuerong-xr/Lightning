"""
Author: xtrs
主窗口
立项时间：2021年12月2日
开发时间：2021年12月6日-
"""
from enum import Enum
from PyQt5 import QtCore as qtc
from PyQt5.QtWidgets import *
from main.MainWin.as_form import AdjustShapesForm
from main.MainWin.is_form import InsertShapesForm
from main.PopDialog.set_dia import SettingWin
import setting as se
# noinspection PyUnresolvedReferences
from PyQt5.uic import loadUiType

# 加载UI
ui, _ = loadUiType('../UI/lightning_tailor.ui')


class Page(Enum):
    """
    页面
    """
    HOME = 0
    SMH = 1
    ADJUST_SHAPES = 2
    INSERT_SHAPES = 3
    JUSTIFY = 4
    pass


class LightningWin(QMainWindow, ui):
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
        # 调整图片大小
        self.as_form = AdjustShapesForm()
        self.adjustShapes_page.layout().addWidget(self.as_form)
        # 插入图片
        self.is_form = InsertShapesForm()
        self.insertShapes_page.layout().addWidget(self.is_form)

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
        self.action_topRi.triggered.connect(lambda: self.act_turnToPage(Page.HOME.value))
        self.action_IS.triggered.connect(lambda: self.act_turnToPage(Page.INSERT_SHAPES.value))
        self.action_AS.triggered.connect(lambda: self.act_turnToPage(Page.ADJUST_SHAPES.value))
        self.action_JS.triggered.connect(lambda: self.act_turnToPage(Page.JUSTIFY.value))
        self.action_smh.triggered.connect(lambda: self.act_turnToPage(Page.SMH.value))
        self.action_set.triggered.connect(lambda: self.act_popDialog(SettingWin()))

    def act_turnToPage(self, index):
        """
        action_top_show
        """
        self.stackedWidget.setCurrentIndex(index)

    def act_popDialog(self, dialog):
        dialog.exec_()

    def statusBar_slot(self, *args):
        """
        状态栏槽函数
        :param args:
        """
        self.statusbar.showMessage(*args)
        pass

    def closeEvent(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        print('close')
        se.dumpConfig_local(self.as_form, 'as_config.json')


if __name__ == '__main__':
    qtc.QCoreApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling)
    app = QApplication([])
    # 安装翻译器
    translator = qtc.QTranslator()
    translator.load('../qm/qt_zh_CN.qm')
    app.installTranslator(translator)

    lt_win = LightningWin()
    lt_win.show()
    app.exec_()
