#!/usr/bin/python
# coding:utf8

import os
import os.path
import zipfile
import rarfile

import sys

reload(sys)
sys.setdefaultencoding('utf8')

srcDir = "/Users/Sirius/Code/Python/rabbit-kindle/zip"
disDir = ""
extends = []


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
    r_file.extractall()
    r_file.close()
    del_file(ful_file_name)


def un_zip(ful_file_name):
    z_file = zipfile.ZipFile(ful_file_name)
    dir_name = os.path.splitext(ful_file_name)[0]
    if os.path.isdir(dir_name):
        pass
    else:
        os.mkdir(dir_name)
    for names in z_file.namelist():
        names = names.decode('gbk')
        print names
        z_file.extract(names, dir_name.decode('gbk'))
    z_file.close()
    del_file(ful_file_name)


# 第一次遍历，就解压缩文件，然后将压缩文件删除
for parent, _, filenames in os.walk(srcDir.decode('gbk')):
    for filename in filenames:
        ext = os.path.splitext(filename)[1].lower()
        if ext == ".rar":
            un_rar(os.path.join(parent, filename))
        if ext == ".zip":
            un_zip(os.path.join(parent, filename))


# 第二次遍历，就将文件拷贝到org-kindle目录夹中


# 第三次遍历，将空文件夹
