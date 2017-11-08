#!/usr/bin/python
# -*- coding: utf-8 -*-
# zabbix notification confirmation script
# python2.7 or above

import requests
import json
import os
import sys

Toparty = "2" 
AgentID = 1000002  


CropID = 'ww20bde9d7168ee5eb'
Secret = 'YH-fWCFRnEpofA7HBcQ2sii68MK1R_zJvki7_H8TZLQ'


Gtoken ="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid="+ CropID + "&corpsecret=" + Secret
headers = {'Content-Type': 'application/json'}
json_data = json.loads(requests.get(Gtoken).content.decode())
token = json_data["access_token"]


Purl = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + token


def msg(title,message):
    weixin_msg = {
         "toparty" : Toparty,
         "msgtype" : "textcard",
         "agentid" : AgentID,
         "textcard" : {
             "title" : title,
             "description" : message,
             "url" : "www.wzlinux.com",
             "btntxt":"more"
          }
      }
    print requests.post(Purl,json.dumps(weixin_msg),headers=headers)



if __name__ == '__main__':
    title = sys.argv[1]        
    message = sys.argv[2]     
    msg(title,message)
