---
title: HTTP请求消息标头介绍
date: 2020-11-20 19:24:30.607
updated: 2020-11-20 19:24:30.607
url: https://www.timberkito.com/?p=9
categories: Java
tags: JavaWeb
---

# HTTP请求消息标头介绍
## 请求消息报文
GET /login.html HTTP/1.1
Host: localhost
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36 Edg/86.0.622.68
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: Idea-fe725cb4=de840fe3-c2ef-4646-bc17-d7e2c9b63008
If-None-Match: W/"408-1605348268629"
If-Modified-Since: Sat, 14 Nov 2020 10:04:28 GMT

## 1.请求行
### 请求方式 请求url 请求协议/版本
**GET /login.html HTTP/1.1**
### HTTP协议有7种请求方式，常用的有两种
#### GET：
1.请求参数在请求行中
http:／／localhost／demo03?username=timber
2.请求的url长度有限制的
3.不安全（暴露在网址栏）

#### POST：
1.请求参数在请求体中
2.请求的url长度没有限制
3.安全

## 2.请求头：客户端告诉服务器一些信息
### 请求头名称：请求头值
### 常见的请求头值：
#### 1.User-Agent:
浏览器告诉服务器，我访问你使用的浏览器版本信息
*可以在服务器端获取此头信息，解决兼容问题
#### 2.Referer：
告诉服务器，当前请求从哪里来
*防盗链：
*统计工作：
#### 3.Connection: keep-alive
链接方式
keep-alive 保持长连接为HTTP1.1版本才有的特性
## 3.请求空行
空行，用于分割POST请求头，和请求体的。
## 4.请求体：
封装POST请求消息的请求参数的