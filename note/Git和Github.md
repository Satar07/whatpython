# git和github

## 初始化git

```bash
git init
```

这是 `Git` 的初始化操作，作用是**将一个已存在文件夹，置于 Git 的控制管理之下。**

## 提交代码

Git 提交代码的基本流程是这样的：

- 创建或修改 **本地文件**
- 使用 **git add** 命令，将创建或修改的文件添加到本地的 **暂存区**，这里保存的是你的临时更改
- 使用 **git commit** 命令，提交文件到 **本地仓库**
- 使用 **git push** 命令，将本地代码库同步到 **远端仓库**

![图片描述](https://doc.shiyanlou.com/courses/uid8504-20190523-1558600871270)

### git add

使用 `git add + 文件名/目录名` 命令，可以将你需要同步的文件，添加到本地的暂存区。我们先进入 DEMO 目录，然后把 README.md 文件添加一下：

```bash
git add README.md
```

输入 `git status` ，可以检测当前目录和暂存区的状态，查看哪些修改被暂存了：

### git commit

`git commit` 提交是你工作的一个里程碑 —— **每当你完成一些工作，都可以创建一次提交，保存当前的版本。**

这样一来，无论你何时修改了文件，都创建一个新版本的文件，你可以很方便地查看以往所有版本的文件和内容。

**在提交之前，你必须先设置你的名字和 email**，这是你在提交 commit 时的签名，每次提交记录里都会包含这些信息。

使用 git config 命令进行配置：

```bash
git config --global user.name "YourName"
git config --global user.email "YourEmail@xxx.com"
```

完成配置后，我们可以创建提交了，请输入：

```bash
git commit -m "first commit"
```

`commit` 的语法结构是 `git commit -m "注释"`，通过上个命令，你创建了一条注释为 “first commit” 的 Git 提交。

![图片描述](https://doc.shiyanlou.com/courses/uid8504-20190523-1558603780044)

> **⚠️ 注意：**
>
> 每次提交，你都必须用 `-m + '注释'` 编辑注释信息 。它不仅能协助我们辨别不同的版本，而且能让你理解，自己当时对文件做了什么修改。
>
> 比如当你每次在文件中添加了新的代码后，你可以写一句提交信息：“添加了 XXX 代码” —— 当你一个月后回来看提交记录或者 Git 日志 时，你还能知道当时做了什么。

###  连接 Github 仓库

使用如下命令，将本地仓库连接到 GitHub 仓库中：

```bash
git remote add origin 仓库链接
```

仓库链接请在这里复制，并用剪切板功能粘贴进去：

![图片描述](https://doc.shiyanlou.com/courses/uid8504-20190523-1558606913216)

`add` 很容易明白 —— 添加。`git remote add` 表示通知 Git 去添加一个远程仓库，后面接上的 `origin` 是这个仓库的小名，方便以后沟通，通常默认用 `origin` 来表示；最后再接上远程仓库的地址，即你刚刚创建的 Github 仓库链接。

![图片描述](https://doc.shiyanlou.com/courses/uid8504-20190523-1558607911486)

### push 命令

**push** 顾名思义，就是推送， 使用 **push** 可以把本地仓库推送到远端仓库中。

具体命令如下：

```bash
git push origin master
```

执行后，GitHub 服务器 需要验证你的身份，按提示输入你的用户名和密码即可完成 push 同步。

> **⚠️ 注意：**在 Linux 中输入密码是不可见的，输完后直接按回车键即可。

![图片描述](https://doc.shiyanlou.com/courses/uid8504-20190523-1558609198353)

### 分支的概念

分支在多人协作中经常会被用到，但前期我们用不到这个功能。 Git 管理的项目进程中，有一条默认的主分支 - `master` 即可。（想象 Git 是一棵树，`master` 就是树干，树干上还可以生出很多分支来，如 master 2.0、master 3.0 等）

`git clone` 命令，它可以帮你拷贝一个 Git 仓库到本地，让自己能够查看该项目，或者进行修改。

![图片描述](https://doc.shiyanlou.com/courses/uid8504-20190523-1558610914428)

如果你想要复制一个项目，看看代码，或者把自己的远程仓库复制到本地，可以执行命令：

```bash
git clone [url]
```

`[url] `指的就是你想复制的仓库



## 总结

![图片描述](https://doc.shiyanlou.com/courses/uid8504-20190523-1558613911512)

