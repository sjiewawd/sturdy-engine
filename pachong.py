
# import requests
# from bs4 import BeautifulSoup
# import openpyxl

# # 发起HTTP请求获取百度热搜页面内容
# url = 'https://top.baidu.com/board?tab=realtime'
# response = requests.get(url)
# html = response.content
#
# # 使用BeautifulSoup解析页面内容
# soup = BeautifulSoup(html, 'html.parser')
#
# # 提取热搜数据
# hot_searches = []
# for item in soup.find_all('div', {'class': 'c-single-text-ellipsis'}):
#     hot_searches.append(item.text)
#
# # 保存热搜数据到Excel
# workbook = openpyxl.Workbook()
# sheet = workbook.active
# sheet.title = 'Baidu Hot Searches'
#
# # 设置标题
# sheet.cell(row=1, column=1, value='百度热搜排行榜')
#
# # 写入热搜数据
# for i in range(len(hot_searches)):
#     sheet.cell(row=i+2, column=1, value=hot_searches[i])
#
# workbook.save('百度热搜.xlsx')
# print('热搜数据已保存到 百度热搜.xlsx')

# # 导入了必要的模块requests和os
# import requests
# import os
#
#
# # 定义了一个函数get_html(url)，
# # 用于发送GET请求获取指定URL的响应数据。函数中设置了请求头部信息，
# # 以模拟浏览器的请求。函数返回响应数据的JSON格式内容
# def get_html(url):
#     header = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
#     }
#     response = requests.get(url=url, headers=header)
#     print(response.json())
#     html = response.json()
#     print(html)
#     return html
#
#
# # 定义了一个函数parse_html(html)，
# # 用于解析响应数据中的图片信息。通过分析响应数据的结构，
# # 提取出每个图片的URL和标题，并将其存储在一个字典中，然后将所有字典组成的列表返回
# def parse_html(html):
#     rl_list = html['data']['rl']
#     # print(rl_list)
#     img_info_list = []
#     for rl in rl_list:
#         img_info = {}
#         img_info['img_url'] = rl['rs1']
#         img_info['title'] = rl['nn']
#         # print(img_url)
#         # exit()
#         img_info_list.append(img_info)
#     # print(img_info_list)
#     return img_info_list
#
#
# # 定义了一个函数save_to_images(img_info_list)，用于保存图片到本地。
# # 首先创建一个目录"directory"，如果目录不存在的话。然后遍历图片信息列表，
# # 依次下载每个图片并保存到目录中，图片的文件名为标题加上".jpg"后缀。
# def save_to_images(img_info_list):
#     dir_path = 'directory'
#     if not os.path.exists(dir_path):
#         os.makedirs(dir_path)
#     for img_info in img_info_list:
#         img_path = os.path.join(dir_path, img_info['title'] + '.jpg')
#         res = requests.get(img_info['img_url'])
#         res_img = res.content
#         with open(img_path, 'wb') as f:
#             f.write(res_img)
#         # exit()
#
#
# # 在主程序中，设置了要爬取的URL，并调用前面定义的函数来执行爬取、解析和保存操作。
# if __name__ == '__main__':
#     url = 'https://www.douyu.com/gapi/rknc/directory/yzRec/1'
#     html = get_html(url)
#     img_info_list = parse_html(html)
#     save_to_images(img_info_list)

# import requests
# from bs4 import BeautifulSoup
# import time
#
# url ="https://www.kugou.com/yy/rank/home/1-8888.html?from=rank"
# headers ={
# "User-Agent":
# "Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
# }
# web_data=requests.get(url=url,headers=headers)
# soup=BeautifulSoup(str(web_data),'lxml')
# print(soup)
