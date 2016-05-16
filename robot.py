__author__ = 'hanzhao'
# coding = utf-8



import weixin
import multiprocessing


webwx = weixin.WebWeixin()
webwx.start()


listenProcess = multiprocessing.Process(target=webwx.listenMsgMode)
listenProcess.start()



