#-*- coding:UTF-8 -*-

import os
from configparser import ConfigParser

# 使用相对目录确定文件位置
conf_dir = os.path.dirname(__file__)
conf_file = os.path.join(conf_dir, 'config.ini')

# print(conf_dir)


# 继承ConfigParser，写一个将结果转为dict的方法
class MyParser(ConfigParser):
    def as_dict(self):
        d = dict(self._sections)
        for k in d:
            d[k] = dict(d[k])
        return d


# 读取所有配置，以字典方式输出结果
def get_all_conf():
    _config = MyParser()
    result = {}
    if os.path.isfile(conf_file):
        try:
            _config.read(conf_file, encoding='UTF-8')
            result = _config.as_dict()
        except OSError:
            raise ValueError('Read config file faoled: %s' % OSError)
    return result


# 将各配置读出来，放在变量中，后续其他文件直接引用这些变量
config = get_all_conf()
sys_cfg = config['sys']
smtp_cfg = config['smtp']
email_cfg = config['email']
log_cfg = config['log']

print(sys_cfg)
print(smtp_cfg)
print(smtp_cfg['host'])
print(email_cfg)
print(log_cfg)
