"""
Author: xtrs
设置
"""
import json
import const
import jsonpath as jp


class Setting:
    """
    设置
    """
    # 用户配置json json数组
    __config_j: json = {}

    @classmethod
    def restore_default(cls, *arg):
        """
        恢复默认设置
        :param arg:要恢复默认设置的窗口
        """
        if not arg:
            cls.__config_j = const.SET_DEFAULT
        else:
            for arg_ in arg:
                cls.__config_j['setting'][arg_] = const.SET_DEFAULT['setting'][arg_]

    @classmethod
    def get_config(cls, expr='.'):
        """
        获取配置内容  【查】
        :param expr: 节点选取表达式
        :return: 数组
        """
        result = jp.jsonpath(cls.__config_j, expr)
        return result

    @classmethod
    def set_config(cls, win, name, value):
        """
        设置   【增/改】 目前实际上只有对第五级的改要求 暂时如此
        想不到好办法，jsonpath_ng 的过滤器有问题，jsonpath_rw_ext 不能用update,头大真是
        :param win: 窗口
        :param name: 控件名字
        :param value: 状态值
        """
        # 可能出错
        # TODO(只能修改第五级，找到按节点修改的方式)
        temp_c = cls.__config_j['setting'][win]
        for i, te in enumerate(temp_c):
            if te['name'] == name:
                cls.__config_j['setting'][win][i]['value'] = value

    @classmethod
    def loadConfig_local(cls, path: str):
        """
        读取用户配置文件，获取初始化数据
        :return:
        """
        if not path.endswith('.json'):
            return
        try:
            with open(path, 'r', encoding='utf-8') as f:
                # 是什么类型返回什么类型
                cls.__config_j = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            # 如果找不到配置文件 或者 配置文件为空 造成解码错误
            print(e)
            cls.restore_default()
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(cls.__config_j, f, indent=4)

    @classmethod
    def dumpConfig_local(cls, path: str):
        """
        将用户设置信息 导入配置文件 （防止误删，上传到服务器）
        :param path:
        :return:
        """
        if not path.endswith('.json'):
            return
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(cls.__config_j, f, indent=4)


class AdjShaSet:
    """
    调整图片大小界面的相关设置
    """
    platform = const.PLATFORM_WPS_WENZI


if __name__ == '__main__':
    Setting.restore_default()
    Setting.get_config()
