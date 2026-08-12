---
title: "发音字典"
description: "TTSMate 技术支持与帮助中心。"
---
<grid>
<column width-ratio="0.500000">
![发音字典 screenshot](/help-assets/ttsmate/zh/pronunciation-dictionary/pronunciation-dictionary-01.png)
</column>
<column width-ratio="0.500000">
![发音字典 screenshot](/help-assets/ttsmate/zh/pronunciation-dictionary/pronunciation-dictionary-02.png)
</column>
</grid>

 

如上图所示，左边是 Apple TTS 引擎以及 Qwen3TTS、MOSSTTSNano等引擎的发音字典设置页面，右图是 Azure TTS 引擎的发音字典设置页面。

### 所有引擎

方法：替换多音字

Qwen3TTS、MOSSTTSNano等引擎并没有明确的 API 可以设置指定多音字发音，所以语音字典的实现方式就是将多音字替换为有明确发音的短语或短句。

例如“一行数字”中的行，我们希望行念 hang，而不做特殊处理的话有时候就会念成行 xing，所以替换规则就是把把“一行数字”替换为“一航数字”。（请注意，替换后的字最好不是多音字，这样发音就可以如我们所指定的那样发音）

这种方法其实适用于所有引擎，只不过 Apple 本地引擎和 Azure 引擎还有更明确的指定多音字发音方法。

### Apple 本地 TTS 引擎

方法：直接用拼音

Apple 本地 TTS 引擎支持拼音发音，例如：

长安城中长老讲长经，为了确保发音正确，可以替换为：chang2安城中zhang3老讲chang2经

拼音后面加上 1,2,3,4 声调即可。

### Azure TTS 引擎

对于 Azure 的 TTS 引擎，则可以用 SSML 格式支持多音字的指定发音。

对于 TTS 发音错误的文字，例如地藏经，有时候念成di cang jing，那么这个时候就需要进行发音设置，以纠正 TTS 引擎的发音。

![发音字典 screenshot](/help-assets/ttsmate/zh/pronunciation-dictionary/pronunciation-dictionary-03.png)

例如我们增加一条地藏经的字典记录。如上图。

原内容：地藏经

替换为：地<sub alias="zàng">藏</sub>经

这种写法是微软 TTS 引擎规定的 SSML (Speech Synthesis Markup Language) 语法，可以指定某个字的发音。

网友们可能困恼于无法打出带语调的字母，例如：zàng，其中à不容易用输入法打出。我的经验是可以问大模型，例如 deepseek，豆包、文心、qwen 都可以。

提示词为：帮我给出“地藏经”三个字的读音拼音，带声调。大模型回答后直接复制即可。

维护好自己常用的字典后，可以导出保存，也可以导入。

维护好发音字典后，后续转换的音频文件会自动应用发音字典的替换规则。
