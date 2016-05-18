# encoding:utf-8
__author__ = 'hanzhao'

import urllib



def run(msg):
    if msg in ['打开英雄榜','.英雄榜']:
        return 'http://www.battlenet.com.cn/wow/zh/'
    if msg.startswith('英雄榜') and ' ' in msg:
        command = msg.split(' ')
        if len(command)==2 :
            if command[1]=='':
                return '请输入服务器以及角色名称\t 例如 英雄榜 塞拉摩 宿舍再见'
            else:
                return 'http://www.battlenet.com.cn/wow/zh/search?q=' + urllib.quote(command[1])
        elif len(command)==3 :
            if command[2]=='':
                return '请输入服务器以及角色名称\t 例如 英雄榜 塞拉摩 宿舍再见'
            else:
                return 'http://www.battlenet.com.cn/wow/zh/character/'+urllib.quote(command[1])+'/'+urllib.quote(command[2])+'/simple'
        else:
            return '正确格式为 英雄榜＋空格＋服务器名＋空格+角色名\n 例如<英雄榜 塞拉摩 宿舍再见>'
    elif msg in ['打开多玩魔兽']:
        return 'http://wow.duowan.com/'
    elif msg in ['打开NGA','打开nga','.nga']:
        return 'http://bbs.ngacn.cc/'
    elif msg in ['baidu','打开百度','.baidu']:
        return 'http://www.baidu.com/'
    else :
        return None