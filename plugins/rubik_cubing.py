# encoding:utf-8
__author__ = 'hanzhao'
import os
import json
import requests
import urllib
import urllib2



CubingUrl = 'http://cubingchina.com'

NewCompetition = 'competition'
# 传入参数格式为?year=&type=&province=&event=
#  year = 2008 to 2016
#  type  = WCA or other
#  provvince =
#  event =





def run(msg):
    print '[info] 魔方小工具模块载入中。。'

    if '<br/>' in msg:     #为群聊消息时候
        [FromUser,msg] = msg.split('<br/>')
    else:                   #为个人消息时候
        pass

    if msg in ['打开粗饼','.粗饼','.cubing']:
        print '[tool]自动回答'
        return 'http://cubingchina.com/'
    elif msg.startswith('近期赛事'):
        if '' not in msg:
            return
        print '[tool]自动回答'    #帮助文档
        return 'http://zhtimer.cn/htimer/simple'
    else :
        print '[tool]未找到匹配值'
        return None