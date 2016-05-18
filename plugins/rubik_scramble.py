# encoding:utf-8
__author__ = 'hanzhao'




import sys
import requests
import urllib
import urllib2
import json
import re

# http://www.zhtimer.cn:2014/scramble/.json?=333*1

SCRAMBLE_URL = 'http://www.zhtimer.cn:2014/scramble/.json?='



def run(msg):
    print '[info] 魔方小工具模块载入中。。'
    print msg
    if msg in ['.2','222','二阶打乱']:        #
        print '[tool]自动回答'
        puzzle_type = '222'
        scramble_api = SCRAMBLE_URL + puzzle_type
        scramble_raw = json.loads(requests.post(scramble_api).text)
        scramble_text = str(scramble_raw[0]['scrambles'][0])
        print scramble_text
        return scramble_text
    elif msg in ['.3','333','三阶打乱']:        #
        print '[tool]自动回答'
        puzzle_type = '333'
        scramble_api = SCRAMBLE_URL + puzzle_type
        scramble_raw = json.loads(requests.post(scramble_api).text)
        scramble_text = str(scramble_raw[0]['scrambles'][0])
        print scramble_text
        return scramble_text
    elif msg in ['.4','444','四阶打乱']:        #
        print '[tool]自动回答'
        puzzle_type = '444'
        scramble_api = SCRAMBLE_URL + puzzle_type
        scramble_raw = json.loads(requests.post(scramble_api).text)
        scramble_text = str(scramble_raw[0]['scrambles'][0])
        print scramble_text
        return scramble_text
    elif msg in ['.5','555','五阶打乱']:        #
        print '[tool]自动回答'
        puzzle_type = '555'
        scramble_api = SCRAMBLE_URL + puzzle_type
        scramble_raw = json.loads(requests.post(scramble_api).text)
        scramble_text = str(scramble_raw[0]['scrambles'][0])
        print scramble_text
        return scramble_text
    elif msg in ['.6','666','六阶打乱']:        #
        print '[tool]自动回答'
        puzzle_type = '666'
        scramble_api = SCRAMBLE_URL + puzzle_type
        scramble_raw = json.loads(requests.post(scramble_api).text)
        scramble_text = str(scramble_raw[0]['scrambles'][0])
        print scramble_text
        return scramble_text
    elif msg in ['.7','777','七阶打乱']:        #
        print '[tool]自动回答'
        puzzle_type = '777'
        scramble_api = SCRAMBLE_URL + puzzle_type
        scramble_raw = json.loads(requests.post(scramble_api).text)
        scramble_text = str(scramble_raw[0]['scrambles'][0])
        print scramble_text
        return scramble_text
    elif msg in ['.3bf','333ni','三盲打乱']:        #
        print '[tool]自动回答'
        puzzle_type = '333ni'
        scramble_api = SCRAMBLE_URL + puzzle_type
        scramble_raw = json.loads(requests.post(scramble_api).text)
        scramble_text = str(scramble_raw[0]['scrambles'][0])
        print scramble_text
        return scramble_text
    elif msg in ['.4bf','444ni','四盲打乱']:        #
        print '[tool]自动回答'
        puzzle_type = '444ni'
        scramble_api = SCRAMBLE_URL + puzzle_type
        scramble_raw = json.loads(requests.post(scramble_api).text)
        scramble_text = str(scramble_raw[0]['scrambles'][0])
        print scramble_text
        return scramble_text
    elif msg in ['.5bf','555ni','五盲打乱']:        #
        print '[tool]自动回答'
        puzzle_type = '555ni'
        scramble_api = SCRAMBLE_URL + puzzle_type
        scramble_raw = json.loads(requests.post(scramble_api).text)
        scramble_text = str(scramble_raw[0]['scrambles'][0])
        print scramble_text
        return scramble_text
    elif msg in ['.minx','五魔打乱']:        #
        print '[tool]自动回答'
        puzzle_type = 'minx'
        scramble_api = SCRAMBLE_URL + puzzle_type
        scramble_raw = json.loads(requests.post(scramble_api).text)
        scramble_text = str(scramble_raw[0]['scrambles'][0])
        print scramble_text
        return scramble_text
    elif msg in ['.py','pyram','金字塔打乱']:        #
        print '[tool]自动回答'
        puzzle_type = 'pyram'
        scramble_api = SCRAMBLE_URL + puzzle_type
        scramble_raw = json.loads(requests.post(scramble_api).text)
        scramble_text = str(scramble_raw[0]['scrambles'][0])
        print scramble_text
        return scramble_text
    elif msg in ['.sq','.sq1','square1','sq1打乱']:        #
        print '[tool]自动回答'
        puzzle_type = 'sq1'
        scramble_api = SCRAMBLE_URL + puzzle_type
        scramble_raw = json.loads(requests.post(scramble_api).text)
        scramble_text = str(scramble_raw[0]['scrambles'][0])
        print scramble_text
        return scramble_text
    elif msg in ['.sk','skewb','斜转打乱']:        #
        print '[tool]自动回答'
        puzzle_type = 'skewb'
        scramble_api = SCRAMBLE_URL + puzzle_type
        scramble_raw = json.loads(requests.post(scramble_api).text)
        scramble_text = str(scramble_raw[0]['scrambles'][0])
        print scramble_text
        return scramble_text
    elif msg in ['.cl','clock','魔表打乱']:        #
        print '[tool]自动回答'
        puzzle_type = 'clock'
        scramble_api = SCRAMBLE_URL + puzzle_type
        scramble_raw = json.loads(requests.post(scramble_api).text)
        scramble_text = str(scramble_raw[0]['scrambles'][0])
        print scramble_text
        return scramble_text
    else :
        print '[tool]未找到匹配值'
        return None

