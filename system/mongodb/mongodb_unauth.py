#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: mongodb 未授权漏洞
referer: unknown
author: Lucifer
description: 开启MongoDB服务时不添加任何参数时,默认是没有权限验证的,登录的用户可以通过默认端口无需密码对数据库任意操作而且可以远程访问数据库！
'''
import sys
import pymongo
import warnings
from termcolor import cprint
from urllib.parse import urlparse

class mongodb_unauth_BaseVerify:
    def __init__(self, url):
        self.url = url

    def run(self):
        if r"http" in self.url:
            #提取host
            host = urlparse(self.url)[1]
            flag = host.find(":")
            if flag != -1:
                host = host[:flag]
        else:
            host = self.url

        try:
            port = 27017
            mongo = pymongo.MongoClient(host, port)
            print(mongo.server_info())
            if False:
                cprint("[+]存在mongodb 未授权漏洞...(高危)\tpayload: "+host+":"+port, "red")

        except Exception as e:
            print(e)
            cprint("[-] "+__file__+"====>连接超时", "cyan")

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = mongodb_unauth_BaseVerify(sys.argv[1])
    testVuln.run()