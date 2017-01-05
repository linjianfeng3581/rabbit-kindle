#!/usr/bin/python
# coding:utf8


def try_encode(s, encoding="utf-8"):
    try:
        print s.encode(encoding)
    except UnicodeEncodeError as err:
        print err


s1 = 'z'
try_encode(s1)
try_encode(s1, "ascii")

s2 = u'雨'
try_encode(s2)
try_encode(s2, "ascii")
try_encode(s2, "GB2312")




