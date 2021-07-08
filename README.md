# docts
document translate, read &amp; translate &amp; write

借助 [pygtrans](https://github.com/foyoux/pygtrans) 链接谷歌机器翻译

 ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/docts) ![PyPI](https://img.shields.io/pypi/v/docts) ![GitHub last commit](https://img.shields.io/github/last-commit/foyoux/docts)



## 概述

此项暂时只用来结合**Sisulizer**翻译**CHM帮助文档**

实际案例: [InstallShield2020-Documents](https://github.com/foyoux/InstallShield2020-Documents)

简单步骤总结如下:

1. 使用 **Sisulizer** 提取 **字符串** 并导出为 **xlf** 或 **xls**
2. 使用此项目进行翻译并导出为`xls`文件
3. 在 **Sisulizer** 中导入 **xls** 文件
4. 编译, 完成

效果可参考: [InstallShield2020-Documents](https://github.com/foyoux/InstallShield2020-Documents)



## CHM相关

- 微软推出的一种[帮助文档格式](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/htmlhelp/microsoft-html-help-1-4-sdk), 实际上是一个 **压缩包**+**自定义块数据**

- 通过解压缩工具或 `hh.exe -decompile folder file.chm` 命令可进行反编译, 此命令系统自带

- 重编译需要 **HTML Help Workshop** (项目 **files** 目录下有提供), 官网已经找不到下载了, 网上能找到最新版本是`1999年发布`的, 😂, 但是可以用.

- 注意: 反编译的是不支持直接重新编译的, 因为缺少 **.hhp** 工程文件, `hhc.exe project.hhp` 命令可编译 **CHM** 文件, 依赖 **HTML Help Workshop**

- 网上找到两款免费可以重编译 **CHM** 文件的工具

  1. KeyTools: 亲测可用, 项目 **files** 目录下有提供
  2. Precision Helper: 未测试

- 翻译 **CHM文档** 的一般套路如下:

  1. 反编译CHM
  2. 借助工具翻译HTML文件
  3. 重编译

  此项目借助 **Sisulizer** 直接支持CHM文档的特性进行操作, 个人觉得这个方法更Nice, 因为我想没有哪个本地化程序是无限制提供免费机器翻译的, 并且也不可能达到 **10万条句子**/**10s** 的速度.

- **Sisulizer** 本身是支持 **机器翻译** 的, 可能由于盗版问题严重, 已全面停用了这一功能.

- 软件本地化工具:  都好久没更新了, 三年吧

  1. [Sisulizer](https://www.sisulizer.com/): 使用简单, 功能强大, 我比较喜欢, 最新版是2018发布的 **374** 版

     [(2018版, 似乎也是最新版)支持的文件类型](images/image-20210626142536447.png)

  2. [SDL Passolo](https://www.trados.com/products/passolo/): 这个比较出名, 不过用得很少, 最新版也是2018出的

     [(2018版, 似乎是最新版)支持的所有文件类型](images/image-20210626142113761.png)

  3. Radialix : 这个也用得很少, 没前面两个出名

- 文件本地化工具:

  1. [SDL Trados Studio](https://www.trados.com/products/trados-studio/): 和 **SDL Passolo** 同家, 目前最厉害的文件本地化工具吧

     [(2021版)支持的所有文件类型](images/image-20210626141828377.png)

> 2021年07月08日22时14分53秒



## 环境准备

1. 安装Sisulizer4

   > 此项目测试环境为 Sisulizer4 374 版

   大家可自行搜索, 推荐: [软件本地化工具 Sisulizer Enterprise Edition 4.0 Build 374 中文免费版](http://www.dayanzai.me/sisulizer.html)

2. 安装HTML Help Workshop

   可自行搜索下载, 项目 **files** 目录下也有提供 **htmlhelp.exe**

3. 配置Sisulizer

   在菜单: 工具->平台->HTML, [如图设置](images/image-20210626144042156.png)



## 快速入门

todo
