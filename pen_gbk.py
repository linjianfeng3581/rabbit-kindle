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
# for parent, _, filenames in os.walk(rotDir + srcDir):
#     for filename in filenames:
#         print>> logFile, filename
#         ext = os.path.splitext(filename)[1].lower()
#         if ext == ".rar":
#             un_rar(os.path.join(parent, filename))
#         if ext == ".zip":
#             un_zip(os.path.join(parent, filename))

ignoreExtends = ['.rar', '.zip', '.7z', '.tar', '.iso']
deleteExtends = ['', '.db', '.ebk3', '.003zip', '.flv', '.downloading', '.014', '.chm', '.jpg', '.006', '.torrent',
                 '.ps', '.htm', '.019', '.011', '.010', '.xlsx', '.012', '.015', '.017', '.016', '.prc', '.log', '.url',
                 '.018', '.cue', '.se!', '.html', '.dkp', '.uvz', '.020', '.umd', '.008', '.009', '.007',
                 '.004', '.002', '.003', '.mbp', '.ape', '.cfg', '.pdb', '.013', '.exe', '.opf']


# 将文件拷贝到org-kindle目录夹中
# 统计
ignoreFiles = 0
deleteFiles = 0
moveToFiles = 0
for parent, _, filenames in os.walk(rotDir + srcDir):
    for filename in filenames:
        ext = os.path.splitext(filename)[1].lower()
        extDir = "" if ext == "" else ext.split(".")[1]
        extDir = "other" if extDir == "" else extDir
        newDir = rotDir + disDir + extDir + "/" + today + "/"

        if ext in ignoreExtends:
            print>> logFile, 'IGNORE>>>>', parent + '/' + filename
            ignoreFiles += 1
            pass
        elif ext in deleteExtends or filename.startswith('._'):
            os.remove(parent + '/' + filename)
            deleteFiles += 1
            print>> logFile, 'DELETE>>>>', parent + '/' + filename
            pass
        else:
            if not os.path.exists(newDir):
                os.makedirs(newDir)
            else:
                try:
                    shutil.move(parent + '/' + filename, newDir + filename)
                    moveToFiles += 1
                    print>> logFile, 'MOVETO>>>>', parent + '/' + filename, newDir + filename
                except Exception, e:
                    print>> logFile, e
                    pass

print("忽略的文件个数为:" + str(ignoreFiles))
print("删除的文件个数为:" + str(deleteFiles))
print("移动的文件个数为:" + str(moveToFiles))

# 删除空文件夹
for parent, _, filenames in os.walk(rotDir + srcDir):
    if not os.listdir(parent):
        os.rmdir(parent)
