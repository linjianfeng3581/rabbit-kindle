#!/usr/bin/python
# coding:utf8


def try_decode(s, decoding='utf-8'):
    try:
        print(s.decode(decoding))
    except UnicodeDecodeError as err:
        print(err)


b = b'$'  # Bytes
# 默认用 UTF-8 进行解码
try_decode(b)
try_decode(b, "ascii")
try_decode(b, "GB2312")

b = b'\xd3\xea'
try_decode(b)
try_decode(b, "ascii")
try_decode(b, "GB2312")
try_decode(b, "GBK")
try_decode(b, "Big5")
