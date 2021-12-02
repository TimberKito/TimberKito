# Windows环境下配置GitHub GPG签名

> 使用 GPG 或 S/MIME，您可以在本地对标记和提交进行签名。 这些标记或提交在 GitHub 上标示为已验证，便于其他人信任更改来自可信的来源。
>
> GitHub官方文档：https://docs.github.com/cn/authentication/managing-commit-signature-verification/about-commit-signature-verification

## 一、在Windows环境下安装GPG

### 下载地址

https://www.gnupg.org/download/index.html

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1638341808218.png)

#### 安装完成后会有两个软件，都是管理密钥的，下文会讲到

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1638342277744.png)

### 配置系统环境变量

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1638341914681.png)

> 注：配置环境变量时选择你所安装软件的路径
>
> 此处为默认安装路径

#### 检查环境变量是否生效

终端中输入

```shell
gpg --version
```

输出如下则环境变量生效

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1638342069811.png)



## 二、使用GPG生成密钥

### 1.打开终端或者 Git Bash 输入

```shell
gpg --full-generate-key
```

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1638342752224.png)



### 2.设置生成密钥

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1638343057855.png)

> 1. 由于GitHub签名认证密钥必须使用 RSA
>
>    所以我们选择（1）RSA and RSA (default)
>
> 2. 设置密钥尺寸选择4096，密钥尺寸越长加密越强。
>
> 3. 设置密钥的有效期限，这里我选择的是密钥永不过期。

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1638343484915.png)

> 设置密钥的姓名，邮箱，描述
>
> **建议设置为GitHub用户名，GitHub绑定的邮箱**
>
> 检查无误后输入O下一步

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1638343633626.png)

> 这时会弹窗提示你设置管理密钥的密码
>
> 此密码以后提交代码时候也要输入，请记牢

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1638343837496.png)

> 输入以下内容则密钥生成完成
>
> 打开可视化软件也能看见密钥已生成

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1638342277744.png)

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1638344068530.png)

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1638344101953.png)

## 三、新增 GPG 密钥到 GitHub 帐户

### 1.查看密钥

在终端中输入

```shell
gpg --list-secret-keys --keyid-format=long
```

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1638344664913.png)

> 图中 sec 所在行  rsa4096为你的密钥尺寸/**后面为你的密钥ID**
>
> 我这里是3BECCAC113E09805

在终端中输入

```shell
gpg --armor --export 你的密钥ID
```

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1638344648411.png)

> 复制 GPG 密钥，从 `-----BEGIN PGP PUBLIC KEY BLOCK-----` 开始，到 `-----END PGP PUBLIC KEY BLOCK-----` 结束。

## 2.将GPG密钥添加到GitHub账户

#### 单击个人资料照片，然后单击Settings

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1638345132906.png)

#### 用户设置侧边栏中，单击 SSH and GPG keys

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1638345177668.png)

#### 单击 New GPG key（新 GPG 密钥）

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1638345223353.png)

#### 在 "Key"（密钥）字段中，粘贴在终端复制的 GPG 密钥

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1638345243143.png)

#### 设置完成

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1638345462845.png)

## 四、在本地Git中配置密钥

#### 1.查找你的GPG 密钥 ID 

```shell
gpg --list-secret-keys --keyid-format=long
```

![](https://timber.oss-cn-chengdu.aliyuncs.com/img/utool_up/1638344664913.png)

#### 2.在 Git 中设置 GPG 签名密钥

```shell
git config --global user.signingkey 3BECCAC113E09805
```

#### 3.设置Git提交时使用签名密钥

全局设置

```shell
git config --global commit.gpgsign true
```

当前项目设置

```shell
git config commit.gpgsign true
```

### 若提交代码时报错

**gpg: skipped "3BECCAC113E09805": No secret key**

### 在Git中设置gpg的启动路径

```shell
git config --global gpg.program "C:\Program Files (x86)\GnuPG\bin\gpg.exe"
```

