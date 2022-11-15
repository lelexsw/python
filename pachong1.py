import requests

url = "https://movie.douban.com/j/chart/top_list"
# url = "https://www.dytt89.com/"
param = {
    "type": "11",
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20,
}

dic ={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

resp = requests.get(url = url, params=param,headers=dic)

# resp = requests.get(url = url,headers=dic)

print(resp.request.url)
print(resp.text)

print(resp.request.headers)

resp.close()