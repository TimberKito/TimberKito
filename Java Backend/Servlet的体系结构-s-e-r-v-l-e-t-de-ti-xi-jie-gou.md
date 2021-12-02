---
title: Servlet的体系结构
date: 2020-11-19 09:23:23.64
updated: 2020-11-19 09:23:23.64
url: https://www.timberkito.com/?p=8
categories: Java
tags: JavaWeb
---

# Servlet的体系结构
### Servlet -- 接口
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
### GenericServlet -- 抽象类

```java
/*
    将Servlet中其他的方法做了默认的空实现，只将servlet（）方法作为抽象
    可以继承GenericServlet，实现service（）方法
*/
public class ServletDemo02 extends GenericServlet {

    @Override
    public void service(ServletRequest servletRequest, ServletResponse servletResponse)
            throws ServletException, IOException {
        System.out.println("demo02....");
    }
```

### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
### HttpServlet -- 抽象类
```java
/*
    对http协议的一种封装，简化操作。
 */
@WebServlet("/demo03")
public class ServletDemo03 extends HttpServlet {

    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        super.service(req, resp);
    }

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {
        super.doGet(req, resp);

        System.out.println("get....启动");
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {
        super.doPost(req, resp);
        System.out.println("post...启动");
    }
}
```
