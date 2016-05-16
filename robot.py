
# encoding:utf-8
__author__ = 'hanzhao'



import weixin
import multiprocessing
import logging
import time

weiwx = weixin.WebWeixin()
weiwx.start()


def listenMsgMode(wx):
        # print '[*] 进入消息监听模式 ... 成功'
        # logging.debug('[*] 进入消息监听模式 ... 成功')
        wx._run('[*] 进行同步线路测试 ... ', wx.testsynccheck)
        playWeChat = 0
        redEnvelope = 0
        while True:
            wx.lastCheckTs = time.time()
            [retcode, selector] = wx.synccheck()
            print 'retcode: %s, selector: %s' % (retcode, selector)
            if wx.DEBUG:
                print 'retcode: %s, selector: %s' % (retcode, selector)
            logging.debug('retcode: %s, selector: %s' % (retcode, selector))
            if retcode == '1100':
                print '[*] 你在手机上登出了微信，债见'
                logging.debug('[*] 你在手机上登出了微信，债见')
                break
            if retcode == '1101':
                print '[*] 你在其他地方登录了 WEB 版微信，债见'
                logging.debug('[*] 你在其他地方登录了 WEB 版微信，债见')
                break
            elif retcode == '0':
                if selector == '2'or '6':
                    r = wx.webwxsync()
                    if r is not None:
                        wx.handleMsg(r)
                elif selector == '7':
                    playWeChat += 1
                    print '[*] 你在手机上玩微信被我发现了 %d 次' % playWeChat
                    logging.debug('[*] 你在手机上玩微信被我发现了 %d 次' % playWeChat)
                    r = wx.webwxsync()
                elif selector == '0':
                    time.sleep(1)
            if (time.time() - wx.lastCheckTs) <= 20:
                time.sleep(time.time() - wx.lastCheckTs)
# listenProcess = multiprocessing.Process(target=webwx.listenMsgMode)
# listenProcess.start()

listenMsgMode(weiwx)






