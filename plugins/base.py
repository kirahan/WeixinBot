# encoding:utf-8
__author__ = 'hanzhao'




import sys


def run(msg):
    print '[info] 基本问答模块载入中。。'
    if msg in ['.author','查看作者']:        #查看作者
        print '[base]自动回答'
        return 'kira晗\n QQ:478222961\n'
    elif msg in ['.h','.help']:
        print '[base]自动回答'    #帮助文档
        return '.author\t 查看作者'
    elif msg in ['查看插件','.plugin']:
        return 'command list plugin'
    elif msg.startswith('开启插件'):
        return 'command open plugin'+':'+msg.split(' ')[1]
    elif msg.startswith('关闭插件'):
        return 'command close plugin'+':'+msg.split(' ')[1]
    elif msg.startswith('载入配置'):
        return 'command load plugin config' + ':' + msg.split(' ')[1]
    else :
        print '[base]未找到匹配值'
        return None