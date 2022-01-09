"""
Author: xtrs
设置
"""
import json
import const
import jsonpath as jp
from enum import Enum


class ConfigPath(Enum):
    """
    配置文件路径
    """
    IS_WID = '../DefaultConfigure/is_df_config.json'
    AS_WID = '../DefaultConfigure/as_df_config.json'
    JS_WID = '../DefaultConfigure/js_df_config.json'


def restore_default(instance):
    """
    恢复默认设置
    :param instance:
    """
    temp = {'AdjustShapesForm': ConfigPath.AS_WID.value}
    type_ = str(instance.__class__).split('.')[-1].replace("'>", '')
    path = temp[type_]
    print(str(instance.__class__))
    with open(path, 'r', encoding='utf-8') as f:
        default_cfg = json.load(f)
    instance.config_j = default_cfg


def get_config(instance, expr='.'):
    """
    获取配置内容  【查】
    :param instance:
    :param expr: 节点选取表达式
    :return: 数组
    """
    result = jp.jsonpath(instance.config_j, expr)
    return result


def set_config(cls, name, value):
    """
    设置   【增/改】 目前实际上只有对第五级的改要求 暂时如此
    想不到好办法，jsonpath_ng 的过滤器有问题，jsonpath_rw_ext 不能用update,头大真是
    :param cls:
    :param name: 控件名字
    :param value: 状态值
    """
    # 可能出错
    # TODO(只能修改第五级，找到按节点修改的方式)
    temp_c = cls.__config_j['setting']
    for i, te in enumerate(temp_c):
        if te['name'] == name:
            cls.__config_j['setting'][i]['value'] = value


def loadConfig_local(instance, path: str):
    """
    读取用户配置文件，获取初始化数据
    :param instance:
    :param path:
    :return:
    """
    if not path.endswith('.json'):
        return
    try:
        with open(path, 'r', encoding='utf-8') as f:
            # 是什么类型返回什么类型
            instance.config_j = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        # 如果找不到配置文件 或者 配置文件为空 造成解码错误
        print(e)
        # 使用默认配置
        restore_default(instance)
        # 将默认配置上载
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(instance.config_j, f, indent=4)


def dumpConfig_local(instance, path: str):
    """
    将用户设置信息 导入配置文件 （防止误删，上传到服务器）
    :param instance:
    :param path:
    :return:
    """
    if not path.endswith('.json'):
        return
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(instance.config_j, f, indent=4)


def ui_to_cfg(instance, wid_s: list, func_str):
    """
    将 ui 变动 更新到 config变量 中
    :param wid_s: 控件列表
    :param instance: 窗口实例
    :param func_str:
    """
    # eval()只能执行表达式 ， exec() 如果使用了global，第一个参数必须写进字典里
    cfg = instance.config_j
    for wid in wid_s:
        name = wid.objectName()
        g = {'self': instance}
        exec(f'x=self.{name}.{func_str}()', g)
        value = g['x']
        # 可能出错 TODO(只能修改第五级，找到按节点修改的方式)
        temp_c = cfg['setting']
        for i, te in enumerate(temp_c):
            if te['name'] == name:
                cfg['setting'][i]['value'] = value


def cfg_to_ui(instance, expr, func_str):
    """
    将 config变量 变动 更新到 ui 中
    :param expr: 寻址（节点）表达式
    :param instance: 窗口实例
    :param func_str:
    """
    # eval()只能执行表达式 ， exec() 如果使用了global，第一个参数必须写进字典里+++++++++++++++++++++++！坑！
    config = jp.jsonpath(instance.config_j, expr)
    # TODO()
    if isinstance(config, list):
        print('是个list')
        pass
    if len(config) == 1:
        config = config[0]
    for config_ in config:
        name = config_['name']
        value = config_['value']
        # setText(QString)要执行 value不能为空，否则相当于没有参数！！！！++++++++++++++++++++++++++！坑！
        if value != '':
            if func_str == 'setText':
                value = f'"{value}"'
            g = {'self': instance}
            exec(f'x=self.{name}.{func_str}({value})', g)


def init_config(instance):
    """
    给窗口初始化配置属性
    :param instance:
    """
    cfg = instance.config_j
    cfg['name'] = instance.objectName()
    cfg['setting'] = []
    for i, child in enumerate(instance.children()):
        cfg['setting'].append({'id': i, 'name': child.objectName(), 'type_': type(child), 'value': ''})


class AdjShaSet:
    """
    调整图片大小界面的相关设置
    """
    platform = const.PLATFORM_WPS_WENZI


if __name__ == '__main__':
    restore_default()
    get_config()
