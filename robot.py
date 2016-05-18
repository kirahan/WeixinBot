# encoding:utf-8
__author__ = 'hanzhao'



import weixin
import multiprocessing
import logging
import time
import os
import json


#
def plugin_name():
    pluginname = []
    for filename in os.listdir("plugins"):
            if not filename.endswith(".py") or filename.startswith("_"):
                continue
            else :
                pluginname.append(filename[:-3])
    return pluginname

plugin_list = plugin_name()
print plugin_list

class PluginManager(object):

    def load_config(self, id):
        """
        You can load plugin config any time, then load plugin.
        :typ groupid: str or unicode
        """
        with open('config/plug_config.json',"r") as f:
            try:
                config = json.load(f)[id]['plugin_on']
                print 'have'
                print config
            except:
                config = json.load(open('config/plug_config.json',"r"))['default']['plugin_on']
        return config


    def open_plugin(self,id,plugname):
        if plugname in plugin_list:
            with open('config/plug_config.json',"r") as f:
                raw_config = json.load(f)
                if id in raw_config:
                    old_config = raw_config[id]
                    if plugname in raw_config[id]['plugin_on']:
                        pass
                    else:
                        old_config['plugin_on'].append(plugname)
                        raw_config[id]['plugin_on'] = old_config['plugin_on']
                        fp = open('config/plug_config.json',"w")
                        fp.write(json.dumps(raw_config))
                        return  1
                else:
                    old_config = {"plugin_on":["base","rubik_tool","rubik_scramble"]}
                    old_config['plugin_on'].append(plugname)
                    raw_config[id] = old_config
                    fp = open('config/plug_config.json',"w")
                    fp.write(json.dumps(raw_config))
                    return  1
            return 2
        return None

    def close_plugin(self,id,plugname):
        if plugname in plugin_list and plugname!='base':
            with open('config/plug_config.json',"r") as f:
                raw_config = json.load(f)
                print raw_config
                if id in raw_config:
                    old_config = raw_config[id]
                    if plugname in old_config['plugin_on']:
                        plugarr = old_config['plugin_on']
                        plugarr.remove(plugname)
                        raw_config[id]['plugin_on'] = plugarr
                        fp = open('config/plug_config.json',"w")
                        fp.write(json.dumps(raw_config))
                        return 1

                else:
                    if plugname in ["base","rubik_tool","rubik_scramble"]:
                        plugarr = ["base","rubik_tool","rubik_scramble"]
                        plugarr.remove(plugname)
                        new_config ={"plugin_on":plugarr}
                        raw_config[id] = new_config
                        fp = open('config/plug_config.json',"w")
                        fp.write(json.dumps(raw_config))
                        return 1
            return 2
        return None

plugmanager =PluginManager()
# plugmanager.close_plugin('ff','rubik_tool')

weiwx = weixin.WebWeixin()
weiwx.start()


def handlemsg(r):
    for msg in r['AddMsgList']:
            print '[*] 你有新的消息，请注意查收'
            logging.debug('[*] 你有新的消息，请注意查收')

            # if True:
            #     fn = 'msg' + str(int(random.random() * 1000)) + '.json'
            #     with open(fn, 'w') as f:
            #         f.write(json.dumps(msg))
            #     print '[*] 该消息已储存到文件: ' + fn
            #     logging.debug('[*] 该消息已储存到文件: %s' % (fn))

            msgType = msg['MsgType']
            srcName = weiwx.getUserRemarkName(msg['FromUserName'])
            dstName = weiwx.getUserRemarkName(msg['ToUserName'])
            content = msg['Content'].replace('&lt;', '<').replace('&gt;', '>')

            msgid = msg['MsgId']

            # if msgType == 1:
            #     cc = weiwx.getNameById(msg['FromUserName'])
            #     print cc

            if msgType == 1:
                    #群聊 获取文字
                # if '<br/>' in content:
                #     [name,content] = content.split('<br/>')
                if msg['FromUserName'][:2] == '@@':
                    config_save_name = weiwx.getGroupName(msg['FromUserName']).decode('utf')        #这里要解码否则会无法匹配到
                else:
                    config_save_name = str(weiwx.getAttrStatusById(msg['FromUserName']))
                    print config_save_name
                plugin_list_user_or_group = plugmanager.load_config(config_save_name)
                print plugin_list_user_or_group


                for plug in plugin_list_user_or_group:
                    plugin=__import__("plugins."+plug, fromlist=[plug])
                    ans = plugin.run(content)
                    if ans is not None :      #插件设置模块
                        if ans.startswith('command'):
                            print ans
                        if ans == 'command list plugin':
                            ans = str(plugmanager.load_config(config_save_name))
                        elif ans.startswith('command open plugin'):
                            plugname = ans.split(':')[1]
                            status = plugmanager.open_plugin(config_save_name,plugname)
                            if status == 1:
                                ans = '插件' + plugname + '成功开启'
                            else:
                                ans ='插件' + plugname + '开启失败'
                        elif ans.startswith('command close plugin'):
                            plugname = ans.split(':')[1]
                            status = plugmanager.close_plugin(config_save_name,plugname)
                            if status == 1:
                                ans = '插件' + plugname + '成功删除'
                            else:
                                ans ='插件' + plugname + '关闭失败'
                        else:
                            pass
                        weiwx.webwxsendmsg(ans, msg['FromUserName'])


def listenMsgMode(wx):
        print '[*] 进入消息监听模式 ... 成功'
        logging.debug('[*] 进入消息监听模式 ... 成功')
        wx._run('[*] 进行同步线路测试 ... ', wx.testsynccheck)
        playWeChat = 0
        redEnvelope = 0
        while True:
            lastCheckTs = time.time()
            [retcode, selector] = wx.synccheck()
            print 'retcode: %s, selector: %s' % (retcode, selector)
            if retcode == '1100':
                print '[*] 你在手机上登出了微信，债见'
                logging.debug('[*] 你在手机上登出了微信，债见')
                break
            elif retcode == '1101':
                print '[*] 你在其他地方登录了 WEB 版微信，债见'
                logging.debug('[*] 你在其他地方登录了 WEB 版微信，债见')
                break
            elif retcode == '0':
                if selector == '2'or '6':
                    r = wx.webwxsync()
                    if r is not None:
                        handlemsg(r)
                elif selector == '7':
                    playWeChat += 1
                    print '[*] 你在手机上玩微信被我发现了 %d 次' % playWeChat
                    logging.debug('[*] 你在手机上玩微信被我发现了 %d 次' % playWeChat)
                    r = wx.webwxsync()
                elif selector == '0':
                    time.sleep(1)
            # if (time.time() - lastCheckTs) <= 10:
            #     time.sleep(10 - time.time() + lastCheckTs)
            print str(time.time()-lastCheckTs)

listenMsgMode(weiwx)







