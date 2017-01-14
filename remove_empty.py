#!/usr/bin/python
# coding:utf8

import os.path
import datetime

import sys

reload(sys)
sys.setdefaultencoding('gbk')

rotDir = "D:/"

srcDir = "kindle/2017-01-04"
disDir = "org-kindle/"
logDir = "log/"
extends = []

today = datetime.date.today().isoformat()
logFile = open(rotDir + logDir + "log-" + today + ".txt", "a+")

# 删除空文件夹
for parent, _, filenames in os.walk(rotDir + srcDir):
    if not os.listdir(parent):
        print parent
        try:
            os.rmdir(parent)
        except Exception, e:
            print "---------------------------------"
            print "CANNOT DELETE", parent, e
            print "---------------------------------"
        print>> logFile, parent
