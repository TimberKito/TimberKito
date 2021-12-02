---
title: 关于Vue路由笔记(VueRouter)
date: 2021-05-31 00:10:11.551
updated: 2021-06-04 10:08:19.366
url: https://www.timberkito.com/?p=97
categories: 前端
tags: Vue
---

# Vue路由(VueRouter)

**导入vue地址**

```html
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```

**导入axios地址**

```html
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

**导入vue路由地址**

```html
<script src="https://unpkg.com/vue-router/dist/vue-router.js"></script> 

```


### 1.1 路由

-----

​	`	路由：根据请求的路由按照统一的路由规则进行请求的转发从而帮助我们实现统一的请求管理`



### 11.2 作用

----

​	`作用：用来在vue中实现组件之间的动态切换`



### 1.3 使用路由

----



​	1.引入路由

```html
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
//vue路由
<script src="https://unpkg.com/vue-router/dist/vue-router.js"></script> 
```
2. 创建组件对象

   ```js
   //声明登录组件模板
   const login={
       template : '<h1>用户登录</h1>',
   };
   
   //声明注册组件模板
   const register={
       template : '<h1>用户注册</h1>',
   };
   ```

3. 定义路由对象规则

   ```js
   //创建一个路由对象
   const router=new VueRouter({
      routes : [
          {path : "/   login",complate : login},  //path:路由的路径	component：路由对应组件
          {path : "/register",complate : register}
   
      ]
   });
   ```

4. 将路由对象注册到vue实例

   ```js
   const app=new Vue({
       el : "#app",
       data : {},
       methods : {},
       router : router ,//设置路由对象
   });
   ```

5. 在页面中显示路由组件

   ```js
       <!--显示路由的组件-->
       <router-view></router-view>
   
   ```

6. 根据链接切换路由

   ```html
   <a href="#/login">点我登录</a>
   <a href="#/register">点我注册</a>
   ```



### 1.4 router-link使用

----

`作用：用来代替我们在切换路由时使用a标签切换路由`
`好处：可以自动的给路由路径加入#号 不需要手动加入`

```html
        <!--router-link-好处：书写路由不需要# to：用来书写路由路径-->
        <router-link to="/login" tag="button">点我登录</router-link>
        <router-link to="/register" tag="button">点我注册</router-link>
```

```markdown
# 总结
	1.router-link 用来替换使用a标签实现路由切换 好处是不需要书写#号直接书写路由路径
	2.router-link to属性:用来书写路由路径	tag属性:用来将router-link渲染成指定的标签
```



### 1.5 默认路由

-----

​	`作用：用来在第一次进行界面显示一个默认路由`

```js
//创建路由对象
const router=new VueRouter({
   routes : [
       // {path:"/",component:login},
       {path:"/",redirect:"/login"}, //redirect:用来当访问的默认路由"/"时，跳转到指定的路由展示 推荐使用
       {path:"/login",component:login},
       {path:"/register",component:register}
   ]
});
```



### 1.6 路由传递

----

##### 第一种方式传递参数--传统方式

1.  通过？形式拼接参数

   ```html
   <router-link to="/login?uid=1&name=zhangsan">点我登录</router-link>
   ```

   2.组件中获取参数

```js
//声明组件模板
const login={
    template:"<h1>用户登录</h1>",
    data(){return{}},
    methods:{},
    created(){
      console.log("=======>>"+this.$route.query.uid);
      console.log("=======>>"+this.$route.query.name);
    },
};
```

##### 第二种方式传递参数--restful方式

1.通过使用路径方式传递参数

```js
<router-link to="/register/21/lisi">点我注册</router-link>
        const router=new VueRouter({
           routes : [
               {path: "/register/:uid/:name",component: register},
           ]
        });
```

2.组件中获取参数

```js
const register={
    template:"<h1>用户注册{{$route.params.name}}</h1>",
    data(){return{}},
    methods:{},
    created(){
        console.log("========>>"+this.$route.params.uid);
        console.log("========>>"+this.$route.params.name);
    },
};
```

​	

### 1.7 Vue CLI安装

-----

#### 安装脚手架

##### 1、配置淘宝镜像

**命令**

```java
npm config set registry https://registry.npm.taobao.org
```

**验证**

```
npm config get registry
```



##### 2、安装vue cli

```bash
npm install -g @vue/cli
npm install vue-cli -g
```

创建vue-cli项目

```
vue init webpack vue-demo
```

##### 4、运行

	npm start 在目录下运行
	http://localhost:8080
	config 
	node_modules 
##### 5、 目录

```markdown
   my-project  --------->>项目名
        build  ------------->>来使用webpack打包使用bulid依赖
        config ------------->>用来整个项目配置
        node_modules-------->>用来管理项目中的依赖
        src	---------------->>用来书写vue的源代码 ··
            assets	---------->>用来存放静态资源 ··
            components 	------>>用来书写vue组件 ··
            router 	---------->> 用来配置项目中的路由 ··
            App.vue ---------->>项目中的组件 ··
            main.js ---------->>项目中的主入口 ··
        static ------------->>其他静态
        .babelrc ----------->>将es6转为es5
        .editorconfig ------>>项目编辑配置
        .gitignore --------->>git版本控制
        .postcssrc.js ------>>源码
        index.html --------->>项目的主页
        package.json ------->>类似于pom.xml文件(依赖管理)
        package-lock.json -->>对package.json加锁文件
        README.md ---------->>阅读文件W
```

##### 6、在脚手架中使用axios

```mathematica
安装axios
	npm install axios --save-dev
	
配置axios
    import axios from 'axios'
    Vue.prototype.$http=axios
    
#使用axios
	在需要发送异步请求的位置this.$http.get('url').then((res)==>{})
	

```

##### 7、在vue中打包部署

```mathematica
#1、在项目的根目录执行命令
	vue run bulid
	注意：vue脚手架打包的项目必须在服务器上运行不能双击运行
	
#2、打包之后项目目录的变化
	在打包之后，项目出现dist目录，dist就是vue脚手架的生产目录(直接部署目录)
	
```

