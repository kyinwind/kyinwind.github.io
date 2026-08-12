---
title: "批量修改文件名"
description: "RightClickMate 技术支持与帮助中心。"
---
- 批量修改文件名

![批量修改文件名 screenshot](/help-assets/rightclickmate/zh/batch-rename-files/batch-rename-files-01.png)

选择多个文件（不能包含文件夹，否则不会显示批量修改文件名的App菜单），点击右键，点击“批量修改文件名”，即可进入批量文件重命名界面。

界面的上半部分是本次修改的文件列表，列表中，左边是文件原名，右边是预计修改后的名称。

如果打勾，说明修改预计没有问题。如果有报错信息，则说明所选择的修改规则有问题，例如文件重名。

如图，假设有以上文件，我们想要去掉无意义的日期和数字，添加拍摄场景、人物等信息，就需要

1、添加“替换文本”动作

将"iShot_2026-04-11"替换为空字符串  
2、添加“添加前缀”动作

添加前缀："0411去运河公园踏青-家人特写"

3、然后再添加“删除字符”动作

这个时候文件后面还有一些无意义的字符，长度都是9

![批量修改文件名 screenshot](/help-assets/rightclickmate/zh/batch-rename-files/batch-rename-files-02.png)

选择删除字符动作，如上图

此时所有文件名都变得一样了，所以列表的右边有了警告，先不用管，因为后面我们要添加序号。

![批量修改文件名 screenshot](/help-assets/rightclickmate/zh/batch-rename-files/batch-rename-files-03.png)

如图，添加序号，前面、后面都可以

![批量修改文件名 screenshot](/help-assets/rightclickmate/zh/batch-rename-files/batch-rename-files-04.png)

加好了序号，这时候文件列表的告警消失了

此时如果确认这样就可以，点击确定，即真正对文件进行改名。

*如果有某些动作会经常使用，也可以点击“保存规则”，将规则保存下来，后续直接调出可用。

*添加错误的动作，可以点击删除，重新再添加

## 动作列表介绍

动作列表包含了可以对文件名进行修改的各种规则，包括：

- 添加前缀

![批量修改文件名 screenshot](/help-assets/rightclickmate/zh/batch-rename-files/batch-rename-files-05.png)

输入要添加的前缀文本即可

- 添加后缀

![批量修改文件名 screenshot](/help-assets/rightclickmate/zh/batch-rename-files/batch-rename-files-06.png)

需要注意，后缀是加载文件名的后面，不是文件扩展名的后面。

- 插入文本

![批量修改文件名 screenshot](/help-assets/rightclickmate/zh/batch-rename-files/batch-rename-files-07.png)

可以选择三个位置来插入文本

第一是文件的开头

第二是文件的结尾，意思是加载扩展名的最后，一般这种情况会破坏现有的文件扩展名

第三是文件扩展名前，即文件名的最后，不破坏扩展名

- 删除字符

![批量修改文件名 screenshot](/help-assets/rightclickmate/zh/batch-rename-files/batch-rename-files-08.png)

删除字符可以“从文件开头”计算删除指定数量的字符，也可以从“文件名最后”计算删除指定数量的字符。

- 替换文本

![批量修改文件名 screenshot](/help-assets/rightclickmate/zh/batch-rename-files/batch-rename-files-09.png)

普通模式，即是把一个指定的字符串替换为一个新的字符串，例如把“2025”替换为“2026”

正则表达式是为了一些开发人员准备的功能，例如下面这个例子：

在批量修改文件名的时候，我想要替换字符，但是不想全部替换，怎么办？

答：使用替换的正则表达式来处理。

find pattern：^([^]*)

replace with ：\$1.

意思是把文件名第一个出现的下划线，替换为.

- 顺序编号

![批量修改文件名 screenshot](/help-assets/rightclickmate/zh/batch-rename-files/batch-rename-files-10.png)

在多个文件需要编号的时候需要使用“顺序编号”动作

如上图所示，可以在文件开头添加一个两位的数字，从1开始，逐项加1，不足两位补零。

![批量修改文件名 screenshot](/help-assets/rightclickmate/zh/batch-rename-files/batch-rename-files-11.png)

位置有三种，如上图。

- 文本转换

![批量修改文件名 screenshot](/help-assets/rightclickmate/zh/batch-rename-files/batch-rename-files-12.png)

这个动作是处理字符之间的连接，以及大小写

- 插入日期

<grid>
<column width-ratio="0.543577">
![批量修改文件名 screenshot](/help-assets/rightclickmate/zh/batch-rename-files/batch-rename-files-13.png)
</column>
<column width-ratio="0.456423">
![批量修改文件名 screenshot](/help-assets/rightclickmate/zh/batch-rename-files/batch-rename-files-14.png)
</column>
</grid>

可以在文件的开头、结尾、扩展名前插入时间，时间有两种，一种是创建时间，一种是修改时间，时间信息从文件本身的信息取。

- 修改扩展名

![批量修改文件名 screenshot](/help-assets/rightclickmate/zh/batch-rename-files/batch-rename-files-15.png)

- 删除开头数字

![批量修改文件名 screenshot](/help-assets/rightclickmate/zh/batch-rename-files/batch-rename-files-16.png)
