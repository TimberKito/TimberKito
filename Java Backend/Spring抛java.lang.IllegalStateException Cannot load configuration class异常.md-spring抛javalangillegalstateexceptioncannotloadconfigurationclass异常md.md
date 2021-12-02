---
title: Spring抛java.lang.IllegalStateException Cannot load configuration class异常.md
date: 2021-06-05 23:30:24.783
updated: 2021-06-05 23:32:19.735
url: https://www.timberkito.com/?p=99
categories: Java
tags: JavaWeb
---

# Spring抛java.lang.IllegalStateException: Cannot load configuration class异常

## 解决方案

#### 将项目SDK从jdk_16换成jdk_1.8即可

参考：https://teratail.com/questions/153773
![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1622906211247.png)

## 开发环境

- 系统：Windows 10 x64
- 项目SDK环境：jdk_16
- 开发工具：IntelliJ IDEA 2021.1 x64
- pom.xml如下

```xml
   <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.12</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-context</artifactId>
            <version>5.0.5.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>javax.annotation</groupId>
            <artifactId>jsr250-api</artifactId>
            <version>1.0</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-test</artifactId>
            <version>5.0.5.RELEASE</version>
        </dependency>
```

## 异常产生

### 项目结构
![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1622905765984.png)

#### 所有类均按照Spring注解配置正确，运行测试代码时抛错

```java
    AnnotationConfigApplicationContext applicationContext = new AnnotationConfigApplicationContext();
    applicationContext.register(SpringConfiguration.class);
    applicationContext.refresh();
    UserService userService = applicationContext.getBean("userService", UserService.class);
    userService.save();
```

### 异常如下（部分）

```shell
Exception in thread "main" java.lang.IllegalStateException: Cannot load configuration class: com.timber.config.SpringConfiguration
	at org.springframework.context.annotation.ConfigurationClassPostProcessor.enhanceConfigurationClasses(ConfigurationClassPostProcessor.java:414)
	at org.springframework.context.annotation.ConfigurationClassPostProcessor.postProcessBeanFactory(ConfigurationClassPostProcessor.java:254)
	at org.springframework.context.support.PostProcessorRegistrationDelegate.invokeBeanFactoryPostProcessors(PostProcessorRegistrationDelegate.java:
```

## 异常解决
### 将项目SDK从jdk_16换成jdk_1.8
![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1622906434983.png)
### 重启IDEA，重新加载项目，异常解决
![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1622906536172.png)

## 参考：https://teratail.com/questions/153773