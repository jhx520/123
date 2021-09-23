#!/usr/bin/python3

# -*- coding: utf-8 -*-

import requests
import re
import urllib.request
import json
import sys
import os

headers = {'Content-Type': 'application/json;charset=utf-8'}

##拷贝企业微信机器人生成的webhook

webhook = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=92e4a7c4-bda0-4758-95e0-2dd1d408b6cd"

def msg(text):

message= {
"msgtype": "text",
"text": {
"content": text, ##注意后面跟【逗号】
},
"at": {
"isAtAll": True
}
}
print(requests.post(webhook,json.dumps(message),headers=headers).content)
url = "https://tianqi.moji.com/weather/china/jiangsu/huqiu-district" ##要爬取天气预报的网址(china后面是各个省市的地址)
par = '()'
opener = urllib.request.build_opener()
urllib.request.install_opener(opener)
html = urllib.request.urlopen(url).read().decode("utf-8")
##提取需要爬取的内容
data = re.search(par,html).group(2)
msg(data)