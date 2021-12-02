---
title: bs4实现网页图片内容爬取
date: 2021-11-03 10:41:47.386
updated: 2021-11-05 10:11:53.372
url: https://www.timberkito.com/?p=136
categories: Python
tags: Python
---

# bs4实现网页图片内容爬取

## 项目信息

> 作者：Timber
>
> 指导教师：CQIPC_Bai
>
> 操作系统：Windows 11 x64
>
> 开发工具：IntelliJ PyCharm 2021.1.3 (Professional Edition)

## 项目需求

- 对给定天气预报网站进行图片爬取（代码+注释截图）
- 运行结果截图
- 梳理代码流程及说明文档的截图
- 特别说明：每一个截图需包含个人信息，否则影响作业得分


## 项目结构

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1635216187907.png)

## 项目依赖库

```python
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit  # BS内置库，用于推测文档编码
import urllib.request  # 发起请求，获取响应
```

## 源代码

```python
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
# @Time    : 2021/10/19 15:58
# @Author  : Timber
# @Id      : 201950130527
# @File    : get_weather_website_graphics.py
# @说明/注释: bs4实现网页图片内容爬取
"""
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit  # BS内置库，用于推测文档编码
import urllib.request  # 发起请求，获取响应


def image_spider(start_url):
    global count  # 记录图片数量
    # 抓bug
    try:
        req = urllib.request.Request(start_url, headers=headers)  # 创建请求对象
        data = urllib.request.urlopen(req)  # 发起请求
        data = data.read()  # 获得响应体
        dammit = UnicodeDammit(data, ["utf-8", "gbk"])
        data = dammit.unicode_markup  # 解码
        # 指定Beautiful的解析器为 html.parser
        soup = BeautifulSoup(data, "html.parser")
        # 查找img标签
        images = soup.select("img")
        for image in images:
            # 抓bug
            try:
                src = image["src"]
                url = src
                count = count + 1
                # 调用download函数
                download(url, count)
            # 抓到bug的处理
            except Exception as err:
                print(err)
    except Exception as err:
        # 打印这个错误对象
        print(err)


def download(url, count):
    try:
        if url[len(url) - 4] == ".":  # 如果 图片url的长度的倒数第四位 = .
            ext = url[len(url) - 4:]
        else:
            ext = ".jpg"

        req = urllib.request.Request(url, headers=headers)
        data = urllib.request.urlopen(req, timeout=100)
        data = data.read()  # 读取文件
        # 以images+序号命名；wb表示以二进制写方式打开，只能写文件， 如果文件不存在，创建该文件；如果文件已存在，则覆盖写
        fobj = open("images" + str(count) + ext, "wb")
        fobj.write(data)  # 写入文件
        fobj.close()  # 关闭文件
        print("downloaded" + str(count) + ext)  # 打印下载(爬取)信息
    except Exception as err:
        print(err)


# 目标url
start_url = "http://www.weather.com.cn/weather/101280601.shtml"

# User-Agent会告诉网站服务器，访问者是通过什么工具来请求的
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50"
}

count = 0

# 调用函数
image_spider(start_url)

print("The end...")

```

## 函数及接口说明

```python
def image_spider(start_url):
```
> 项目主函数，获取网站源码并查找img标签内容
> 传入参数 start_url 为目标网址

```python
def download(url, count):
```

> 项目下载函数，获取网站img标签内容中的图片
>
> 传入参数图片下载地址

## 运行结果

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1635217288465.png)