# encoding:utf-8
__author__ = 'hanzhao'




import sys


def run(msg):
    print '[info] 魔方小工具模块载入中。。'
    if msg in ['打开计时器','.计时器']:
        print '[tool]自动回答'
        return 'http://zhtimer.cn/htimer/simple'
    else :
        print '[tool]未找到匹配值'
        return None