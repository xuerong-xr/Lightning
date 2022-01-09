"""
Author: xtrs
开发是生成默认配置文件
"""
import json
from PyQt5.QtWidgets import QWidget


def generateDCfg(instance: QWidget):
    """

    :param instance:
    """
    cfg = {'name': instance.objectName(), 'setting': []}
    for i, child in enumerate(instance.findChildren(QWidget)):
        type_ = str(type(child)).split('.')[-1].replace("'>", '')
        if hasattr(child, 'isChecked'):
            value = child.isChecked()
        elif hasattr(child, 'text'):
            value = child.text()
        else:
            value = ''
        cfg['setting'].append({'id': i, 'name': child.objectName(), 'type_': type_, 'value': value})
    path = 'as_df_config.json'
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(cfg, f, indent=4)


if __name__ == '__main__':
    # x = AdjustShapesForm()
    # generateDCfg(x)
    pass
