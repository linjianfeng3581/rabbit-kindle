#!/usr/bin/python
# coding:utf8

import os.path
import datetime

import sys

reload(sys)
sys.setdefaultencoding('gbk')

rotDir = "D:/"

srcDir = "kindle/2017-01-09"
disDir = "org-kindle/"
logDir = "log/"

today = datetime.date.today().isoformat()
logFile = open(rotDir + logDir + "log-" + today + ".txt", "a+")

specChar = ['•', '·', '?']

for parent, _, filenames in os.walk(os.path.join(rotDir, srcDir)):
    for filename in filenames:
        for c in specChar:
            if filename.find(c) != -1:
                print filename
                no_problem_name = filename.replace(c, '')
                print no_problem_name
                os.rename(os.path.join(parent, filename), os.path.join(parent, no_problem_name))
