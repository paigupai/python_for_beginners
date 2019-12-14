# python_for_beginners
## python爬虫入门教学  
#### hello_World
> [在线ide gitpod](https://gitpod.io/workspaces/)如何使用  
>>使用GitHub账户进行登陆，并关联，在GitHub仓库的网址前添加https://www.gitpod.io/# 即可生成workspace  
> 学习[print](https://github.com/paigupai/python_for_beginners/blob/master/hello_world.py)   
> 单击右上角的绿色三角，执行代码  

如果想要在本地环境下运行python，需要安装[python环境](https://www.python.org/)，下载[IDE vscode](https://code.visualstudio.com/)(也可以直接使用PyCharm 社区版),并安装python插件

#### [novel](https://github.com/paigupai/python_for_beginners/blob/master/novel.py)
> 学习最简单的python爬虫  
> 掌握如何导入python库  
> 学习通过requests库的get方法批量爬取小说并储存  
> 使用过的命令行： 
>> 安装以下库
>> pip3 install requests  
>> pip3 install BeautifulSoup4  
>> pip3 install lxml  

本sample实现了一个批量爬取小说，并保存为txt文件。通过使用BeautifulSoup4将html转换为树形结构的lxml，进行内容抓取。也可以不使用BeautifulSoup4，直接使用正则，从字符串中进行抓取，[例子](https://github.com/paigupai/ghost_soldier/blob/master/ghost_soldier.py)  
缺点:因为直接使用.text方法直接取得，(<br>)换行符缺失，最终生成的小说正文，缺少换行符。  

盗版小说网站基本上都是套用一样的html结构，稍微修改下，可以适用于绝大多数盗版小说网站  

#### TODO  
> 如何通过gitpod进行pull,push  
> 学习通过post的方法取得  
> python中如何使用sqlie  
> 如何使用[postman](https://www.getpostman.com/)  
> 学习mongodb
