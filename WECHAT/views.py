# -*- coding: utf-8 -*-
from django.http import HttpResponse
import hashlib
import time
import os
import urllib2,json
# from lxml import etree
import xml.dom.minidom
from django.views.generic.base import View
from django.shortcuts import render
class WeixinInterfaceView(View):
    def get(self, request):
        #得到GET内容
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)
        #自己的token
        token = 'breadmum' #这里改写你在微信公众平台里输入的token
        #字典序排序
        tmpList = [token, timestamp, nonce]
        tmpList.sort()
        tmpstr = '%s%s%s' % tuple(tmpList)
        #sha1加密算法
        tmpstr = hashlib.sha1(tmpstr).hexdigest()

        #如果是来自微信的请求，则回复echostr
        if tmpstr == signature:
            return render(request, 'get.html', {'str': echostr},
                          content_type='text/plain')
    def post(self, request):
        str_xml = request.body.decode('utf-8')    #use body to get raw data
        #xml = etree.fromstring(str_xml)    #进行XML解析

        #toUserName = xml.find('ToUserName').text
        #fromUserName = xml.find('FromUserName').text
        #createTime = xml.find('CreateTime').text
        #msgType = xml.find('MsgType').text
        #content = xml.find('Content').text   #获得用户所输入的内容
        #msgId = xml.find('MsgId').text

        doc = xml.dom.minidom.parseString(str_xml)
        collection = doc.documentElement
        toUserName = collection.getElementsByTagName("ToUserName")[0].childNodes[0].data
        fromUserName = collection.getElementsByTagName("FromUserName")[0].childNodes[0].data
        createTime = collection.getElementsByTagName("CreateTime")[0].childNodes[0].data
        msgType = collection.getElementsByTagName("MsgType")[0].childNodes[0].data
        content = collection.getElementsByTagName("Content")[0].childNodes[0].data
        msgId = collection.getElementsByTagName("MsgId")[0].childNodes[0].data

        return render(request, 'reply_text.xml',
                      {'toUserName': fromUserName,
                       'fromUserName': toUserName,
                       'createTime': time.time(),
                       'msgType': msgType,
                       'content': content,
                       },
                       content_type = 'application/xml'
        )