# -*- ecoding: utf-8 -*-
# import requests
import re

# lst = re.findall(r"\d+",",,1863541265,,123444")
# print(lst)
#
# it = re.finditer(r"\d+",",,1863541265,,123444")
# print(it)
# for i in it:
#     print(i.group())
# #
# #

# obj = re.compile(r"\d+")
# ret = obj.finditer(",我的,1863541265,,123444")
# for it in ret:
#     print(it.group())

s = """
<div class='jay'><spany. id='1'>gg搞起来l</span></div>
<div class='jj'><spany. id='2'>songtie</span></div>
<div class='jolin'><spany. id='3'>dcm</span></div>
<div class='sylar'><spany. id='4'>fsz</span></div>
<div class='tory'><spany. id='5'>hsbd</span></div>
"""

obj = re.compile(r"<div class='(?P<cl>.*?')><spany. id='(?P<id>.*?)'>(?P<name>.*?)</span></div>",re.S)

result = obj.finditer(s)
for it in result:
    print(it.group("name"))