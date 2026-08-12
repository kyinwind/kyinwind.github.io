---
title: "常见问题列表"
description: "RightClickMate 技术支持与帮助中心。"
---
## 问题1： 我找不到 App 在系统设置的扩展开关，怎么办？

- 请见问题： 我找不到扩展开关，怎么办？

MacOS在不同的版本，Finder扩展的开关界面不太一样。 在mac15.1的系统设置的确找不到RightClickMate的扩展开关，如果安装RightClickMate之后，在桌面上点击右键看不到新建、复制路径等自定义的菜单，那么请打开终端，按照顺序复制并运行以下两条命令：

1. 重启Finder插件
2. pluginkit -e use -i com.michaeldev.RightClickMate.MyFinderSyncExtension
3. 重启访达
4. killall Finder
5. 这两条命令运行完毕后，在桌面上点击右键，应该就可以看到自定义的菜单出现了。

## 问题2、我安装、更新了 RightClickMate，点击右键菜单，发现看不到自定义菜单了

答：这件事情偶尔有发生，推测问题出现在 Finder 没有及时加载安装、更新的自定义菜单上。

按照下面的操作来重启 Finder 恢复自定义右键菜单，或者干脆重启电脑也可以（如果你懒得看文档）。

最快的解决方法就是重启 Finder。

1、点击“通用设置”的“2、系统设置”区域的“需要帮助？”的右侧空白区域

![常见问题列表 screenshot](/help-assets/rightclickmate/zh/faq-list/faq-list-01.png)

![常见问题列表 screenshot](/help-assets/rightclickmate/zh/faq-list/faq-list-02.png)

 2、在弹出的帮助按钮中，点击"复制重启 Finder 的命令"，此时 App 会帮你打开终端 App，同时把重启 Finder 命令复制到系统粘贴板，command+V 复制到终端，回车执行。

![常见问题列表 screenshot](/help-assets/rightclickmate/zh/faq-list/faq-list-03.png)

此时，你会发现右键菜单自定义菜单已经出现了。

## 问题 3：为什么在系统 iCloud 同步的目录，无法看到自定义的右键菜单？

答：受系统限制，RightClickMate 自定义右键菜单无法在 iCloud 同步目录显示。

RightClickMate 自定义右键菜单是由系统 Finder 应用加载的，在 iCloud 同步目录Finder不加载 App 的自定义菜单。
