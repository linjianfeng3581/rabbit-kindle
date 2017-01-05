#!/usr/bin/python
# coding:utf8


def try_decode(s, decoding='utf-8'):
    try:
        print(s.decode(decoding))
    except UnicodeDecodeError as err:
        print(err)

b = b'$'     # Bytes
try_decode(b)            # 默认用 UTF-8 进行解码
try_decode(b, "ascii")   # 尝试用 ASCII 进行解码
try_decode(b, "GB2312")  # 尝试用 GB2312 进行解码

b = b'\xd3\xea'  # 上面例子中通过 GB2312 编码得到的 Bytes
try_decode(b)           # 默认用 UTF-8 进行解码
try_decode(b, "ascii")  # 尝试用 ASCII 进行解码
try_decode(b, "GB2312")  # 尝试用 GB2312 进行解码
try_decode(b, "GBK")    # 尝试用 GBK 进行解码
try_decode(b, "Big5")    # 尝试用 Big5 进行解码
