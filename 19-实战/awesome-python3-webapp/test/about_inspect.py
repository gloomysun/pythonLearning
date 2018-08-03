#!/usr/bin/env python
# encoding: utf-8
'''
@file: about_inspect.py
@time: 2018/8/3 17:16
@desc:
POSITIONAL_ONLY、
VAR_POSITIONAL、
KEYWORD_ONLY、
VAR_KEYWORD、
POSITIONAL_OR_KEYWORD
'''
import inspect


def a(a, b=0, *c, d, e=1, **f):
    pass


aa = inspect.signature(a)
print("inspect.signature（fn)参数是:%s" % aa)
print("inspect.signature（fn)的类型：%s" % (type(aa)))

bb = aa.parameters
print("signature.paramerters属性是:%s" % bb)
print("ignature.paramerters属性的类型是%s" % type(bb))
for cc, dd in bb.items():
    print("mappingproxy.items()返回的两个值分别是：%s和%s" % (cc, dd))
    print("Parameter.kind属性是:%s:%s" % (dd.default,dd.kind))
