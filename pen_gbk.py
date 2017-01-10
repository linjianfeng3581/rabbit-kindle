#!/usr/bin/python
# coding:utf8

import os
import os.path
import shutil
import zipfile

import datetime
import rarfile

import sys

reload(sys)
sys.setdefaultencoding('gbk')

rotDir = "/Users/Sirius/Code/Python/rabbit-kindle/"

srcDir = "kindle/"
disDir = "org-kindle/"
logDir = "log/"
extends = []

today = datetime.date.today().isoformat()
logFile = open(logDir + "log-" + today + ".txt", "a+")


def del_file(delete_file):
    if os.path.exists(delete_file):
        os.remove(delete_file)


def un_rar(ful_file_name):
    r_file = rarfile.RarFile(ful_file_name)
    dir_name = os.path.splitext(ful_file_name)[0]
    if os.path.isdir(dir_name):
        pass
    else:
        os.mkdir(dir_name)
    os.chdir(dir_name)
    try:
        r_file.extractall()
    except Exception, e:
        print>> logFile, ful_file_name, e
        pass
    r_file.close()
    del_file(ful_file_name)


def un_zip(ful_file_name):
    z_file = zipfile.ZipFile(ful_file_name, 'r')
    dir_name = os.path.splitext(ful_file_name)[0]
    if os.path.isdir(dir_name):
        pass
    else:
        os.mkdir(dir_name)
    for files in z_file.namelist():
        try:
            z_file.extract(files, dir_name)
        except Exception, e:
            print>> logFile, ful_file_name, e
            pass
    z_file.close()
    del_file(ful_file_name)


# 第一次遍历，就解压缩文件，然后将压缩文件删除
for parent, _, filenames in os.walk(rotDir + srcDir):
    for filename in filenames:
        print>> logFile, filename
        ext = os.path.splitext(filename)[1].lower()
        if ext == ".rar":
            un_rar(os.path.join(parent, filename))
        if ext == ".zip":
            un_zip(os.path.join(parent, filename))

# 第二次遍历，就将文件拷贝到org-kindle目录夹中
for parent, _, filenames in os.walk(rotDir + srcDir):
    for filename in filenames:
        ext = os.path.splitext(filename)[1].lower()
        extDir = ext.split(".")[1]
        extDir = "other" if extDir == "" else extDir
        newDir = rotDir + disDir + extDir + "/" + today + "/"
        if not os.path.exists(newDir):
            os.makedirs(newDir)
        else:
            try:
                if filename.startswith('._'):
                    os.remove(parent + '/' + filename)
                    print>> logFile, parent + '/' + filename, '>>>> WAS DELETE'
                else:
                    shutil.move(parent + '/' + filename, newDir + filename)
                    print>> logFile, parent + '/' + filename, '>>>>TO>>>>', newDir + filename
            except Exception, e:
                print>> logFile, e
                pass

# 第三次遍历，将空文件夹
for parent, _, filenames in os.walk(rotDir + srcDir):
    print parent
    if not os.listdir(parent):
        print("this is empty")
        os.rmdir(parent)
