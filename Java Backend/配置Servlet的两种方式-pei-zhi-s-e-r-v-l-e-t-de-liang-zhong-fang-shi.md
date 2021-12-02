---
title: 配置Servlet的两种方式
date: 2020-11-18 09:13:34.378
updated: 2020-11-18 09:14:23.747
url: https://www.timberkito.com/?p=7
categories: Java
tags: JavaWeb
---

# 配置Servlet的两种方式
## 方法一：在web.xml中部署Servlet
```xml
<!--配置Servlet-->
    <servlet>
        <servlet-name>demo2</servlet-name> //创建的Servlet名字
        <servlet-class>cn.timber.web.servlet.ServletDemo02</servlet-class> //完整路径：包名+类名
        <!--指定Servlet的创建时机
            1.第一次被访问时，创建
                <load-on-startup>的值为负数
            2.在服务器启动时，创建
                <load-on-startup>的值为0或正整数
            -->
        <load-on-startup>5</load-on-startup>
    </servlet>

    <servlet-mapping> //映射位置
        <servlet-name>demo2</servlet-name>
        <url-pattern>/demo2</url-pattern> //Servlet的映射路径
    </servlet-mapping>
```

## 方法二：使用注解配置Servlet
```java
@WebServlet("/demo01") 
public class ServletDemo01 implements Servlet{
}
```
#### 一个Servlet可以定义多个访问路径
@WebServlet ({"/d4" , "/dd4" , "/ddd4"})
#### 路径的定义规则：
   1./xxx
   2./xxx/xxx (多层路径)
  3.*.do (*为通配符，任意字符)


