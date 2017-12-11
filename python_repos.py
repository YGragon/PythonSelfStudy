import requests

# 执行API调用，并存储响应
url = 'https://api.github.com/search/repositories?q=tetris+language:python&sort=stars&order=desc'
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应存储仔一个变量中
response_dict = r.json()
print("Total repositores:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositores returned:", len(repo_dicts))

# 研究第一个仓库
repo_dict = repo_dicts[0]
# print("\nSelected information about first repository:")

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print('Name-项目名:', repo_dict['name'])
    print('Owner-作者:', repo_dict['owner']['login'])
    print('Stars-点赞数:', repo_dict['stargazers_count'])
    print('Repositores-项目地址:', repo_dict['html_url'])
    print('Create-创造时间:', repo_dict['created_at'])
    print('Updated-更新时间:', repo_dict['updated_at'])
    print('Description-描述:', repo_dict['description'])

print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

# 处理结果
# print(response_dict.keys())