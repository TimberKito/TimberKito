---
title: Linux 修改swap虚拟内存
date: 2021-06-01 18:21:49.423
updated: 2021-06-04 10:07:43.537
url: https://www.timberkito.com/?p=98
categories: Linux系统
tags: Linux
---

# Linux 修改swap虚拟内存

> Linux中Swap（即：交换分区），类似于Windows的虚拟内存，就是当内存不足的时候，把一部分硬盘空间虚拟成内存使用,从而解决内存容量不足的情况。Android是基于Linux的操作系统，所以也可以使用Swap分区来提升系统运行效率。

## 一、增加swap空间

### 1.查看当前系统swap空间

```shell
[root@localhost ~]# free -m
             total       used       free     shared    buffers     cached
Mem:          1006        753        252          3         32        526
-/+ buffers/cache:        195        810
Swap:         100          0       100
```

### 2.增加swap文件

```shell
[root@localhost ~]# cd /usr
[root@localhost usr]# mkdir swap
[root@localhost usr]# cd swap
[root@localhost swap]# ll
总用量 0
[root@localhost swap]# dd if=/dev/zero of=/usr/swap/swapfile1 bs=1M count=2048
```

> <u>bs=1M 表示写入的每个块的大小为1M，count=2048 表示总共建立2048M的swap文件</u>

### 3.查看创建文件大小

```shell
du -sh /usr/swap/swapfile1
```

### 4.将目标文件标识为swap分区文件

```shell
mkswap /usr/swap/swapfile1
```

### 5.激活swap文件

```shell
swapon /usr/swap/swapfile1
```

### 6.修改/etc/fstab文件，在末行增加以下内容

```shell
vim /etc/fstab
```

```shell
/usr/swap/swapfile1 swap swap defaults 0 0
```

### 7.查看是否挂在成功

```shell
[root@localhost ~]# swapon -s
Filename				Type		Size	Used	Priority
/swap                                  	file	266236	266236	-2
/home/swap                             	file	2047996	260500	-3
[root@localhost ~]# 
```

## 二、删除swap空间

### 1.关闭swap

```shell
swapoff /usr/swap/swapfile1
```

### 2.修改/etc/fstab文件，删除以下内容

```shell
/usr/swap/swapfile1 swap swap defaults 0 0
```

## 三、修改swappiness设置swap的使用时机

### 1.查看swap使用比例情况

```shell
cat /proc/sys/vm/swappiness
```

> <u>0意味着“在任何情况下都不要发生交换”。</u>
>
> swappiness＝<u>100的时候表示积极的使用swap分区</u>，并且把内存上的数据及时的搬运到swap空间里面

### 2.临时修改使用比例

```shell
sysctl vm.swappiness=60
```

> 内存在使用到100-60=40%的时候，就开始出现有交换分区的使用。
>
> **注意：临时修改后，重启操作系统会重置默认值。**

### 3.永久修改使用比例

```shell
vim  /etc/sysctl.conf
```

**在sysctl.conf文件中最后一行加入**

```shell
vm.swappiness=60
```

