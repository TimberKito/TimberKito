## Windows 环境下安装与配置Node.js

### 一、下载Node.js安装包

> 下载地址：[http://nodejs.cn/download/](https://)
> 
> 本教程以msi安装包为例

#### 点击Windows 安装包下载

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/1646151977902.png)

<br/>

### 二、安装Node.js

#### 1.打开安装包

> 欢迎页：点击Next

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/1646151561398.png)

#### 2.允许使用条款

> 点击接受条款后Next

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/1646151572239.png)

#### 3.选择安装路径

> 选择你要安装的路径
> 
> **本案例保存默认在C盘路径：C:\Program Files\nodejs**

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/1646151582648.png)

#### 4.安装组件

> 这些是Node.js里面包含的组件，例如运行环境，包管理器等
> 
> **保持默认即可，点击Next**

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/1646151642121.png)

#### 5.安装开发工具

> 开发工具可以等以后实际开发过程中安装
> 
> 这里选择不勾选安装工具

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/1646151649358.png)

#### 6.安装Node.js

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/1646151682989.png)

### 三、查看是否安装成功

#### 1.打开终端

> **使用 Win键+R，输入cmd**

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/1646151739167.png)

#### 2.输入指令

```sh
node -v
```

```sh
npm -v
```

> 出现如下图所示版本号，即为安装成功

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/1646151793731.png)

### 四、配置Node.js （非必须）

#### 1.使用管理员权限打开终端

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/1646153769705.png)

> 移动到Node.js安装目录下

```sh
cd C:\"Program Files"\"nodejs"
```

#### 2.创建全局组件文件夹和缓存文件夹

```sh
mkdir node_global
```

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/1646154080664.png)

```sh
mkdir node_cache
```

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/1646154132904.png)

#### 3.设置npm全局包目录与缓存目录

> 设置全局目录
**双引号内为刚刚创建的 node_global 文件夹路径**

```sh
npm config set prefix "C:\Program Files\nodejs\node_global"
```

> 设置缓存目录
**双引号内为刚刚创建的 node_cache 文件夹路径**

```sh
npm config set cache "C:\Program Files\nodejs\node_cache"
```

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/1646154565842.png)

#### 4.设置系统环境变量

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/1646154866436.png)

> 将环境变量 Path 中的npm路径更换为刚才**自定义的 node_global 全局包**
> 
> 本案例为 C:\Program Files\nodejs\node_global

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/1646154941007.png)

> 新建一个系统变量

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/1646155458711.png)

> 变量名：NODE_PATH
> 
> 变量值：**自定义的 node_global 全局包路径后 + \node_modules**

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/1646155075658.png)

<br/>

> 在Path变量中新建
> 
> %NODE_PATH%

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/1646155114230.png)

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/1646155789028.png)
