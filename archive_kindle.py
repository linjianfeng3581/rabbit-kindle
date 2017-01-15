#!/usr/bin/python
# coding:utf8

import os.path
import shutil
import datetime

import sys

reload(sys)
sys.setdefaultencoding('gbk')

rotDir = "D:/"

srcDir = "kindle/2017-01-06"
disDir = "org-kindle/"
logDir = "log/"
extends = []

today = datetime.date.today().isoformat()
logFile = open(rotDir + logDir + "log-" + today + ".txt", "a+")

ignoreExtends = ['.rar', '.zip', '.7z', '.tar', '.iso']
deleteExtends = ['.db', '.ebk3', '.003zip', '.flv', '.downloading', '.014', '.chm', '.jpg', '.006', '.torrent',
                 '.ps', '.htm', '.019', '.011', '.010', '.xlsx', '.012', '.015', '.017', '.016', '.prc', '.log', '.url',
                 '.018', '.cue', '.se!', '.html', '.dkp', '.uvz', '.020', '.umd', '.008', '.009', '.007',
                 '.004', '.002', '.003', '.mbp', '.ape', '.cfg', '.pdb', '.013', '.exe', '.opf', '.cif', '.bin',
                 '.class', '.cip', '.gif', '.evt', '.ini', '.mf', '.mid', '.pdg', '.png', '.thm', '.wav', '.x3', '.bak',
                 '.bat', '.bmp','.mp3']

# 将文件拷贝到org-kindle目录夹中
# 统计
ignoreFiles = 0
deleteFiles = 0
moveToFiles = 0
for parent, _, filenames in os.walk(os.path.join(rotDir, srcDir)):
    for filename in filenames:
        print os.path.join(parent, filename)
        ext = os.path.splitext(filename)[1].lower()
        extDir = "" if ext == "" else ext.split(".")[1]
        extDir = "other" if extDir == "" else extDir
        newDir = rotDir + disDir + extDir + "/" + today + "/"

        if ext in ignoreExtends:
            print>> logFile, 'IGNORE>>>>', os.path.join(parent, filename)
            ignoreFiles += 1
            pass
        elif ext in deleteExtends or filename.startswith('._'):
            try:
                os.remove(os.path.join(parent, filename))
                deleteFiles += 1
                print>> logFile, 'DELETE>>>>', os.path.join(parent, filename)
            except Exception, e:
                print>> logFile, 'DELETE PROGRESSING---Exception:', e
                pass
        else:
            if not os.path.exists(newDir):
                os.makedirs(newDir)
            else:
                src = os.path.join(parent, filename)
                dis = os.path.join(newDir, filename)
                try:
                    shutil.move(src, dis)
                    moveToFiles += 1
                    print>> logFile, 'MOVETO>>>>', src, dis
                except Exception, e:
                    print>> logFile, 'ERROR MOVETO>>>>', src, dis, e
                    os.remove(parent + '/' + filename)
                    print>> logFile, 'DELETE DUPLICATE>>>>', src
                    pass

print("忽略的文件个数为:" + str(ignoreFiles))
print("删除的文件个数为:" + str(deleteFiles))
print("移动的文件个数为:" + str(moveToFiles))

# 删除空文件夹
for parent, _, filenames in os.walk(os.path.join(rotDir, srcDir)):
    if not os.listdir(parent):
        os.rmdir(parent)

print("删除的文件个数为:" + str(deleteFiles))
print("移动的文件个数为:" + str(moveToFiles))

# 删除空文件夹
for i in range(0, 7):
    for parent, _, filenames in os.walk(os.path.join(rotDir, srcDir)):
        if not os.listdir(parent):
            print parent
            try:
                os.rmdir(parent)
            except Exception, e:
                print "---------------------------------"
                print "CANNOT DELETE", parent, e
                print "---------------------------------"
            print>> logFile, parent
