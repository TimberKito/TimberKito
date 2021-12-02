---
title: CentOS 7 安装JDK 1.8 环境教程
date: 2020-12-08 12:00:08.871
updated: 2021-06-05 22:36:34.277
url: https://www.timberkito.com/?p=12
categories: Linux系统
tags: Linux
---

# 方法一：使用yum安装jdk环环境
## 1.查看云端yum库中目前支持安装的jdk软件包

```shell
yum search java|grep jdk
```

![11115.png](https://www.timberkito.com/upload/2020/12/11115-a79e9ed15dcd4a71989486666996645c.png)

## 2.选择版本安装jdk
```shell
 yum install -y java-1.8.0-openjdk*
```
## 3.安装完成后，验证是否安装成功
```shell
java -version
```
![版本.png](https://www.timberkito.com/upload/2020/12/%E7%89%88%E6%9C%AC-8aa892e99e9647ecb19fd6af41b7de97.png)

## 4.查找jdk安装位置
```shell
find / -name 'java'
```
![image.png](https://www.timberkito.com/upload/2020/12/image-73e1befe123d413b9e543a0e3b657dd5.png)

> 默认安装路径一般为：
/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.151-5.b12.el7_4.x86_64/jre/bin/java

# 方法二：从Oracle获取安装包，手动安装
## 1.从Oracle官网中获取jdk安装包
### 本案例使用jdk8演示
> 下载地址：https://www.oracle.com/cn/java/technologies/javase-downloads.html

![image.png](https://www.timberkito.com/upload/2020/12/image-b7720e2ed69a4b9b9e7abffe519d46a3.png)

### 根据系统版本和位数选择tar.gz
![image.png](https://www.timberkito.com/upload/2020/12/image-0ce0659c9ad74eab81e80d04b1000db2.png)

### 复制下载链接
![image.png](https://www.timberkito.com/upload/2020/12/image-971d274b30404abcb2618a5eff5e4fc3.png)

https://download.oracle.com/otn-pub/java/jdk/8.0.1+9/51f4f36ad4ef43e39d0dfdbaf6549e32/jdk-8.0.1_linux-x64_bin.tar.gz
### 创建文件夹，使用wget命令获取安装包
```shell
mkdir /usr/java
cd /usr/java
wget https://download.oracle.com/otn/java/jdk/8u271-b09/61ae65e0886
```
### 等待下载
![image.png](https://www.timberkito.com/upload/2020/12/image-435954996e4a48838819a60001475e6b.png)

## 2.解压安装jdk
### 使用tar命令解压安装包
```shell
tar zxvf jdk-8.0.1_linux-x64_bin.tar.gz
```
## 3.配置系统环境变量
### 用Vim打开profile
```shell
vim /etc/profile
```
### 在文档末尾此处添加系统环境变量
![image.png](https://www.timberkito.com/upload/2020/12/image-f353469bb51044c9b984d0df016afa79.png)
### 键盘上按i键进入编写

```shell
export JAVA_HOME=/usr/share/jdk1.6.0_14
export PATH=$JAVA_HOME/bin:$PATH
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
```
### ++注意：JAVA_HOME的路径是你实际解压后的JDK的路径++

### 按esc退出编辑模式，再按shift+Q输入x保存

### 输入命令使profile生效
```shell
source /etc/profile
```

## 4.安装完成后，验证是否安装成功
```shell
java -version
```
![版本.png](https://www.timberkito.com/upload/2020/12/%E7%89%88%E6%9C%AC-8aa892e99e9647ecb19fd6af41b7de97.png)
