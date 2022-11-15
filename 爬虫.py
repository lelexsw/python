
"""
1.确定网址
2.搭建关系  发送请求 接受响应
3.筛选数据
4.保存本地

"""

import requests #导入请求模块
from lxml import etree #数据预处理
from urllib import request #下载方法

#1.确定网址
#互联网上的标准资源的地址
url = 'https://v.huya.com/cat/51'

#2.搭建关系 发送请求 接受响应
#爬虫的原理：伪装成浏览器
#字典 键名 键值 键值对 {key:value}
#tab
headers = {
   'User-Agent': 'zilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
#工具
#请求目标网站
result = requests.get(url=url, headers=headers).text


#3.筛选数据  result (re xpath bs4 pyquery json)
res = etree.HTML(result)

data = res.xpath('//img[@class="pic"]')
print(data)

# # #data ==== list 列表
#循环 重复事情
for i in data:
  NewName = i.xpath('./@alt')[0]
  NewUrl = i.xpath('./@data-original')[0]
  # print(NewName,NewUrl)

  # 4.保存本地
  request.urlretrieve(NewUrl,r'C:\Users\EDZ\Desktop\美女\\'+NewName+'.jpg')
  print('下载完成!')




