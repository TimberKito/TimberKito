---
title: Spark安装与部署实现文档
date: 2020-12-15 01:44:45.316
updated: 2021-06-04 10:08:44.679
url: https://www.timberkito.com/?p=17
categories: Linux系统
tags: Linux
---

# 开发环境
### ++你需要jdk环境，详细操作流程参见以下文章++
**++https://www.timberkito.com/?p=12++**
### ++两台CentOS系统，推荐配置内存2GB以上++

# 一、从spark官方获取spark安装包

### 本案例使用spark-3.0.1为例
![image.png](https://www.timberkito.com/upload/2020/12/image-820d800917ed4a0397098d182ebd22f4.png)
下载地址 https://www.apache.org/dyn/closer.lua/spark/spark-3.0.1/spark-3.0.1-bin-hadoop2.7.tgz

### 使用wget 命令获取spark安装包

```shell
mkdir /usr/spark
cd /usr/spark
wget https://mirror.bit.edu.cn/apache/spark/spark-3.0.1/spark-3.0.1-bin-hadoop2.7.tgz
```
### 使用tar命令解压安装包
```shell
tar -zxvf spark-3.0.1-bin-hadoop2.7
```

# 二、配置spark环境变量

### 进入spark-3.0.1目录中conf目录下
```shell
cd spark-3.0.1-bin-hadoop2.7/conf/
```
### 将spark-env.sh.template文件重命名为spark-env.sh

```shell
mv spark-env.sh.template spark-env.sh
```
![image.png](https://www.timberkito.com/upload/2020/12/image-e67c89475df74d87bd92fcd0dc4df78b.png)
> 使用vim在文件末尾添加如下变量
export JAVA_HOME=/usr/java/jdk1.8.0_271/
export SPARK_MASTER_HOST=192.168.94.129
export SPARK_MASTER_PORT=7077

### ++注意：JAVA_HOME=为你的jdk路径 SPARK_MASTER_HOST=为你的master主机ip地址++

### 将slaves.template文件重命名为slaves
```shell
mv slaves.template slaves
```
![image.png](https://www.timberkito.com/upload/2020/12/image-458d04d19091402da025b7ec2d1624e0.png)

### ++将localhost改为你的宿主机IP地址++

# 三、配置Workers环境变量
### 启动第二台CentOS，重复以上所有步骤
> ++注意：Workers环境变量与上面配置一样，只要将 SPARK_MASTER_HOST=设置为你的Master主机ip即可（本案例Master主机为192.168.94.129）slaves中的保持不变为localhost++

# 四、启动Spark通过Web UI观察cluster
### 进入spark3.0目录中的sbin目录
```shell
cd /usr/spark/spark-3.0.1-bin-hadoop2.7/sbin
```
### 启动Spark
```shell
bash start-all.sh
```
### 输入Workers服务器密码
![MK1B8DGSXP04EOTGOZ4.png](https://www.timberkito.com/upload/2020/12/M%25K1B8DGSXP0%5B4%7DEOTGOZ$4-d289db32594340829a51ddf9adf63e21.png)
### 在浏览器中输入master主机ip：8080端口
![image.png](https://www.timberkito.com/upload/2020/12/image-62611986c6a949eca6eac58cf1db6da1.png)
# 五、在cluster mode下，计算Pi值
### 在Master主机中调用Spark官方演示程序
```shell
cd /usr/spark/spark-3.0.1-bin-hadoop2.7
./bin/spark-submit --class org.apache.spark.examples.SparkPi --master spark://192.168.11.128:7077 examples/jars/spark-examples_2.12-3.0.1.jar
```
### 看到以下输出结果即为成功
![AR~QHGE7QIBX5VG~TIL.png](https://www.timberkito.com/upload/2020/12/AR%7B%7B~QHGE7QIB%25X5VG%5B~TIL-11d9874859ab4f4f91abdad7308e0834.png)
![image.png](https://www.timberkito.com/upload/2020/12/image-92f69929e455496fa3dd3cf2b2cdc2c0.png)
