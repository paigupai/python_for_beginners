# 引入库
import requests
import time
from bs4 import BeautifulSoup
# 网站站点
url = "https://www.biquge.com.cn/book/32135/"
# 写入User-Agent模拟浏览器上网,避免出现个别网站拒绝访问的情况
# User-Agent缺失会导某些网站返回403
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",}
# get发送请求
response = requests.get(url,headers=headers)
# 将网页编码方式转换为utf-8
# 部分中文网站会使用GBK编码，会出现中乱码的现象
response.encoding = 'utf-8'
# 网站源码
html = response.text
# lxml化
soup = BeautifulSoup(html,'lxml')
# 取得图书信息
book_info = soup.find('div',id="info")
# 取得书名
book_name = book_info.find('h1').text
print(book_name)
# 取得章节div
item_div = soup.find('div', id="list")
# 章节list
item_list = item_div.find_all('dd')
# 新建文件保存小w说内容
# w为write的意思，文件不存在的情况下自动创建，r为read
f = open(f"{book_name}.txt",'w',encoding="utf-8")
for item in item_list:
 # 反爬
 #time.sleep(1)
 #章节名
 chapter_name = item.text
 print(chapter_name)
 #取得href
 href = item.find('a').attrs['href']
 #去除多余
 href = href.replace('/book/32135/','')
 #生成每章链接
 item_url = url + href
 print(item_url)
 # get发送请求
 item_response = requests.get(item_url,headers=headers)
 # 将网页编码方式转换为utf-8
 item_response.encoding = 'utf-8'
 # 网站源码
 item_html = item_response.text
 # lxml化
 soup = BeautifulSoup(item_html,'lxml')
 #text
 text = soup.find('div',id = "content").text
 # 清洗提取的数据
 book_content = text.replace(' ','')
 #写入
 f.write(f"{chapter_name}\n")
 f.write(f"{book_content}\n")
 # 只第一章
 #break
