"""
Author: xtrs
Data: 2021/12/7
Function:UI文件
"""

# noinspection PyUnresolvedReferences
from PyQt5.uic import loadUiType
from setting import Setting as s

# 加载UI
ui, _ = loadUiType('../UI/lightning_tailor.ui')
ui_set, _ = loadUiType('../UI/setting.ui')
# 加载用户配置
s.loadConfig_local('../UI_Manager/config.json')
s.get_config()
