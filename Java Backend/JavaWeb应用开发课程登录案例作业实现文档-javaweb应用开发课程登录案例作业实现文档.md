---
title: JavaWeb应用开发课程登录案例作业实现文档
date: 2020-12-12 01:31:28.059
updated: 2021-06-02 20:51:45.331
url: https://www.timberkito.com/?p=15
categories: Java
tags: JavaWeb
---

# 作业需求：
![image.png](https://www.timberkito.com/upload/2020/12/image-c002b05965074418a2156579a0786e3d.png)

# 开发环境
- 操作系统：Windows 10
- 软件环境：jdk1.8 、Tomcat9 
- 开发工具：IntelliJ IDEA 2020
# 基本思路
![无标题.png](https://www.timberkito.com/upload/2020/12/%E6%97%A0%E6%A0%87%E9%A2%98-0ca1ec2416f34de7aab661d27477218d.png)
# 代码实现
## 登录页面代码
```jsp
<%--
  Created by IntelliJ IDEA.
  User: Timber
  Date: 2020/12/11
  Time: 9:22
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
  <head>
    <title>登录页面</title>
  </head>
  <body>

  <form action="/JAVAWEB/loginServlet" method="post">
    <label>
      <input type="text" placeholder="请输入用户名" name="username">
    </label><br>
    <label>
      <input type="password" placeholder="请输入密码" name="password">
    </label><br>
    <input type="submit" value="登录">
    <br>
  </form>

  </body>
</html>
```
> 需求中提到密码框不能显示明文，故应使用 type="password"<br> action="/JAVAWEB/loginServlet" 是登录程序Servlet路径<br>method="post" 请求方法为 POST

## LoginServlet实现代码
```java
package cn.timber.servlet;

import cn.timber.mysql.HkMysql;

import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/loginServlet")
public class LoginServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        //获取用户名和密码
        String username = request.getParameter("username");
        String password = request.getParameter("password");

        //后端控制台输出
        System.out.println(username+" "+password);

        //密码匹配接口
        String myPwd = "123456";

        HttpSession session=request.getSession();
        session.setAttribute("username", username);
        
        //信息加入数据库
        String sqlINFO = new HkMysql().mysqlHK(request.getParameter("username"), request.getRemoteAddr(), new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date()));
        System.out.println(sqlINFO);

        //密码判断
        if(password.equals(myPwd)) {
            //重定向到登录成功页面
            response.sendRedirect(request.getContextPath()+"/loginSuccess.jsp?username="+ username);
        }else {
            //重定向到登录失败页面
            response.sendRedirect(request.getContextPath()+"/loginFail.jsp?username="+ username);
        }
        
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        this.doPost(request , response);

    }
}

```

## 创建数据库，建立表格
![image.png](https://www.timberkito.com/upload/2020/12/image-0a87a628461042e18f7b8d7949f958f0.png)
![image.png](https://www.timberkito.com/upload/2020/12/image-c52847e8536b441096c6ee4b18948609.png)

## JDBC连接数据库代码
```java
package cn.timber.mysql;
import java.sql.*;
public class HkMysql {

    static final String JDBC_DRIVER = "com.mysql.cj.jdbc.Driver";
    static final String DB_URL = "jdbc:mysql://0.0.0.0:3306/javaweb?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC";

    // 数据库的用户名与密码
    static final String USER = "root";
    static final String PASS = "123456";

    public String mysqlHK (String username , String ipaddr , String loginTime) {

        Connection conn = null;
        Statement stmt = null;
        Statement statement = null;
        try {
            // 注册 JDBC 驱动
            Class.forName(JDBC_DRIVER);

            // 打开链接
            System.out.println("连接数据库...");
            conn = DriverManager.getConnection(DB_URL, USER, PASS);

            // 执行查询
            System.out.println(" 实例化Statement对象...");
            stmt = conn.createStatement();
            String sql;

            //添加数据
            String sql1 = "insert into javaweb.javaweblogin values ('"+username+"','"+ipaddr+"','"+loginTime+"');";
            statement = conn.createStatement();
            statement.executeUpdate(sql1);

            sql = "SELECT * FROM javaweblogin";
            ResultSet rs = stmt.executeQuery(sql);
            //ResultSet rs1 = stmt.executeQuery(sql);//创建数据对象

            while (rs.next()) {
                // 通过字段检索
                String id = rs.getString("IP地址");
                String name = rs.getString("用户名");
                String time = rs.getString("提交时间");

                // 输出数据
                System.out.print("ip: " + id);
                System.out.print(", 用户名: " + name);
                System.out.print(", 提交时间: " + time);
                System.out.print("\n");
            }
            // 完成后关闭
            rs.close();
            stmt.close();
            conn.close();
        } catch (SQLException se) {
            // 处理 JDBC 错误
            se.printStackTrace();
        } catch (Exception e) {
            // 处理 Class.forName 错误
            e.printStackTrace();
        } finally {
            // 关闭资源
            try {
                if (stmt != null) stmt.close();
            } catch (SQLException se2) {
            }// 什么都不做
            try {
                if (conn != null) conn.close();
            } catch (SQLException se) {
                se.printStackTrace();
            }
        }

        return "已加入数据库";

    }

}
```
> ++注：需要JDBC环境依赖++ <br>下载地址：https://downloads.mysql.com/archives/c-j/
### 在工程项目中导入jar包步骤
![image.png](https://www.timberkito.com/upload/2020/12/image-8f8809b400f34bf2957f52d7d0e2d895.png)
![image.png](https://www.timberkito.com/upload/2020/12/image-a85f84b201d84bd7b42be983b05f3bc9.png)
**在web目录中WEB-INF包中创建lib目录导入jar包即可**

## 登录成功页面代码
```jsp
<%--
  Created by IntelliJ IDEA.
  User: Timber
  Date: 2020/12/11
  Time: 9:43
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title><%
            out.print(request.getParameter("username"));
    %>登录成功</title>

    <script src="jquery-3.5.1.js"></script>

    <script>
        $(function() {
            //toRight
            $("#toRight").click(function() {
                //获取右边的下拉列表对象，append(左边下拉列表选中的option)
                $("#rightName").append($("#leftName > option:selected"));
            });
        });
    </script>
 <style>
        #leftName, #btn, #rightName {
            width: 100px;
            height: 300px;
        }
        #toRight {
            margin-top: 100px;
            margin-left: 30px;
            width: 50px;
        }
        .border {
            height: 500px;
            padding: 100px;
        }
    </style>
</head>
<body>
登陆成功<br>
欢迎您：<br>
<font color="red" size="22" >
    <%
        out.print(request.getParameter("username")+"<br>");
    %>
</font>
<a href="<%=request.getContextPath()%>/index.jsp">重新登录</a>
<form action="/JAVAWEB/heroServlet" method="post" >
    <div class="border">
        英雄：
        <select id="leftName" multiple="multiple">
            <option value="葫芦娃">葫芦娃</option>
            <option value="一只耳">一只耳</option>
            <option value="美国队长">美国队长</option>
            <option value="黑猫警长">黑猫警长</option>
            <option value="唐老鸭的情妇">唐老鸭的情妇</option>
        </select>
        </select> <input type="button" id="toRight" value="-->"> 败类：

        <select id="rightName" name="bailei" multiple="multiple">

        </select>
        <br/>
        <input type="submit" value="提交">
    </div>
</form>

</div>
</body>
</html>
```
## 登录失败页面代码
```jsp
<%--
  Created by IntelliJ IDEA.
  User: Timber
  Date: 2020/12/11
  Time: 9:51
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>登陆失败</title>
</head>
<body>
<h1>用户名<%out.print(request.getParameter("username"));%>与密码不匹配，请重新登录</h1>
<a href="<%=request.getContextPath()%>/index.jsp"><h2>重新登录</h2></a>
</body>
</html>
```

## HeroServlet实现代码
```java
package cn.timber.servlet;

import cn.timber.mysql.HkMysql;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;

@WebServlet("/heroServlet")
public class HeroServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        //获取选择败类的String数组
        String[] bailei = request.getParameterValues("bailei");

        HttpSession session=request.getSession();
        String username = (String)session.getAttribute("username");
        System.out.println(username);

        //转发到jsp
//        request.getAttribute("name", username);
        request.setAttribute("loginname" , username);
        request.setAttribute("s" , bailei);
        request.getRequestDispatcher("hero.jsp").forward(request , response);

    }
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        this.doPost(request , response);
    }
}
```
> ++这里的“bailei”由于是多选项，所以一定要用getParameterValues方法来获取并用String[] 来接收，否则会出错++ <br>
关于用户名的获取由于loginServlet生命周期已结束，这里我用的session.getAttribute("username")方法来获取的，若有更好的实现方法，欢迎您的指教

## 选择结果页面代码
```jsp
<%--
  Created by IntelliJ IDEA.
  User: Timber
  Date: 2020/12/11
  Time: 9:48
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>选择结果页面</title>
</head>
<body>

欢迎您：<br>
<font color="red" size="22">
    <%
        String loginname = (String)request.getAttribute("loginname");
        out.print(loginname);
    %>
</font>

发现了混入革命队伍的败类：<br>
<%
    String [] s1 = (String [])request.getAttribute("s");
    for (String s : s1) {
        out.print(s + "<br>");
    }
%>
</body>
</html>
```
# 项目部署
### 关于项目部署参考以下文章
**++https://www.timberkito.com/?p=16++**
# GitHub项目地址（给我一个Star吧QAQ）
**++https://github.com/TimberKito/CQIPC_jsp_login++**