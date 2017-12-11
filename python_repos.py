import requests

# 执行API调用，并存储响应
url = 'https://api.gthub.com/search/repositores?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应存储仔一个变量中
response_dict = r.json()

# 处理结果
print(response_dict.keys())