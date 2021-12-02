---
title: CentOS 7 安装Tomcat和部署Web项目
date: 2020-12-14 16:23:57.531
updated: 2020-12-14 16:31:42.602
url: https://www.timberkito.com/?p=16
categories: Java | Linux系统
tags: JavaWeb
---

# 在这之前

### ++你需要jdk环境，详细操作流程参见以下文章++
**++https://www.timberkito.com/?p=12++**

# 一、从Apache Tomcat官网获取安装包
> 官网地址：http://tomcat.apache.org/
本案例以Tomcat9为例

![image.png](https://www.timberkito.com/upload/2020/12/image-cd43105196a54c76a77f7cf98db0b860.png)

### 选择tar.gz格式安装包下载
![image.png](https://www.timberkito.com/upload/2020/12/image-d7ed997d8b9749e4afa94a43df63409d.png)
> 复制下载链接：https://mirrors.tuna.tsinghua.edu.cn/apache/tomcat/tomcat-9/v9.0.41/bin/apache-tomcat-9.0.41.tar.gz

### 在CentOS系统中下载安装包

创建文件夹
```shell
mkdir /usr/tomcat
cd /usr/tomcat
```
使用wget命令下载链接
```shell
wget https://mirrors.tuna.tsinghua.edu.cn/apache/tomcat/tomcat-9/v9.0.41/bin/apache-tomcat-9.0.41.tar.gz

```
# 二、解压缩安装包，安装Tomcat

```shell
tar -zxvf apache-tomcat-9.0.41.tar.gz
```
# 三、启动Tomcat服务
### 进入Tomcat服务bin目录
```shell
cd apache-tomcat-9.0.41/bin/
```
### 启动服务
```shell
bash startup.sh 
```
![image.png](https://www.timberkito.com/upload/2020/12/image-6ee3ade8a952447fa2007c42bc786448.png)
### 浏览器输入地址：8080默认端口查看
![image.png](https://www.timberkito.com/upload/2020/12/image-adcb3349439d409189d383fe4111c854.png)
# 四、在Tomcat服务上部署Web应用
### 在IDEA上打包项目
![image.png](https://www.timberkito.com/upload/2020/12/image-6eb164379c154b008fc5c8ebf8686092.png)
### 将war包放入tomcat目录中webapps目录下即可
![image.png](https://www.timberkito.com/upload/2020/12/image-daf95b45a16345f88a4e83862f3ff65e.png)
![image.png](https://www.timberkito.com/upload/2020/12/image-aef80cc2f9fc48ce80d09926d1ec97cd.png)