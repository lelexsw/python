# from urllib.request import urlopen
import requests

# url = "http://www.baidu.com/"
# resp = urlopen(url)
# # print(resp.read())
# # print(resp.read().decode("utf-8"))
#
# with open("mybaidu.html",mode="w") as f:
#     f.write(resp.read().decode("utf-8"))
#
# print('over')
import requests
url = 'http://www.sogou.com/web?query=%E5%91%A8%E6%9D%B0%E4%BC%A6'
# url2 = 'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=88093251_115_hao_pg&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6'
dic = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
}
#
resp = requests.get(url,headers=dic)
#
print(resp)
# print(resp.text)

url = "https://fanyi.baidu.com/sug"
dat = {
    "kw":"boy"
}

resp = requests.post(url, data= dat)

print(resp.json())