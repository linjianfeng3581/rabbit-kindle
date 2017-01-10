#!/usr/bin/python
# coding:utf8

import os.path
import sys

reload(sys)
sys.setdefaultencoding('gbk')

rotDir = "/dev/disk6s1/"
srcDir = "kindle/"
extends = []
totalFiles = 0

# 统计后缀类型
for parent, _, filenames in os.walk(rotDir + srcDir):
    totalFiles += len(filenames)
    for filename in filenames:
        ext = os.path.splitext(filename)[1].lower()
        extends.append(ext)

print("后缀类型有:" + str(set(extends)))
print("后缀个数：" + str(len(set(extends))))
print("文件总数: " + str(totalFiles))

