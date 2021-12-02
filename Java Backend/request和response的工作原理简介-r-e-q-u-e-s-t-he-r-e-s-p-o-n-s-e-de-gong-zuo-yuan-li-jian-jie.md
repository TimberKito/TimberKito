---
title: request和response的工作原理简介
date: 2020-11-26 11:38:09.331
updated: 2020-11-26 11:40:32.031
url: https://www.timberkito.com/?p=11
categories: Java
tags: JavaWeb
---

# request和response的工作原理简介

> 一、tomcat servers会根据请求url中的资源路径，创建对应的ServletDemo01的对象。

### url：http://localhost/project/demo01

> 二、tomcat servers会创建request和response对象，其中request对象中会封装请求消息数据。

### ServletRequest

```java
@WebServlet("/demo01")
public class ServletDemo01 implements Servlet{
}
```

> 三、tomcat servers将request和response两个对象传递给ServletDemo01中的service方法，并且调用service方法。

```java
@WebServlet("/demo01")
public class ServletDemo01 implements Servlet{
	@Override
	public void service (ServletRequest servletRequest, ServletResponse servletResponse)
            throws ServletException, IOException{
    }
}
```

> 四、程序员，可以通过request对象获取请求消息数据，通过response对象来设置响应消息数据
### ServletResponse 

> 五、服务器在给浏览器做出响应之前，会从response对象中拿取程序员设置的响应消息数据。