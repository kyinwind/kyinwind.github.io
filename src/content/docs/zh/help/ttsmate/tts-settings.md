---
title: "TTS 设置"
description: "TTSMate 技术支持与帮助中心。"
---
TTS 设置

# TTS 引擎核心能力对比表（纯个人主观对比）

## 评分标准说明

- ★★★★★：行业顶尖 / 完全满足需求，无明显短板
- ★★★★☆：表现优秀，仅存在极细微的可忽略不足
- ★★★☆☆：表现合格，能满足基础需求，有明显优化空间
- ★★☆☆☆：表现一般，仅能覆盖极简单场景，短板突出
- ★☆☆☆☆：不支持 / 完全无法满足需求

<sheet sheet-id="FwYnOg" token="PoLrsJbhthPofJtb4CMcWGmlnvh"></sheet>

##  苹果本地内置 TTS

![TTS 设置 screenshot](/help-assets/ttsmate/zh/tts-settings/tts-settings-01.png)

音色点评（个人观点，仅供参考，每个人喜欢的音色可能不尽相同）：

婷婷、美嘉音色还凑合，其他音色忽略吧。

## Qwen3TTS 引擎（本地）

![TTS 设置 screenshot](/help-assets/ttsmate/zh/tts-settings/tts-settings-02.png)

Qwen3 需要下载模型、加载模型后使用。模型大约需要 1.1G，需要从huggingface下载。

音色、感情方面我觉得都还可以，但是有个问题就是说话速度有点不稳，整体转写质量不是很稳定。

我不清楚是模型本身问题，还是用的开源框架的问题，对于个人播客使用，对质量容忍度比较高的场景使用我觉得 ok，如果想要质量稳定一些，就需要选择商业收费的云端引擎了。

## MOSSTTS引擎（本地）

![TTS 设置 screenshot](/help-assets/ttsmate/zh/tts-settings/tts-settings-03.png)

模型大约 760M，需要先下载加载后使用。

内置 6 个中文音色，音质都还不错。因为这个开源框架并没有面向 swift 开发的官方开发包，我是用 codex 自己攒了一个，跑起来还算可以，但是因为没有经过充分测试，所以不能保证没有吞字的现象。

大家如果发现有吞字吞句的问题，可以发邮件给我反馈，把转写的文本也发一份，我来分析修正。

## KoKoroTTS引擎（本地）

![TTS 设置 screenshot](/help-assets/ttsmate/zh/tts-settings/tts-settings-04.png)

这个引擎也需要下载加载模型，约350M。

这个引擎的亮点音色主要是英文，大家可以看音色后面的 ABCD，意思是质量，A 是最好的。

只关注中文的网友可以忽略这个引擎。

## AzureTTS 引擎（云端）

![TTS 设置 screenshot](/help-assets/ttsmate/zh/tts-settings/tts-settings-05.png)

右图为 Azure 的 TTS 引擎配置，需要输入 key 和 region，这两部分信息将会以密文形式保存在苹果本地的 keychain

如果您是 Azure 的用户则可以选择 Azure 的 TTS 引擎，因为是商业化引擎，所以音色、质量、稳定度都没得说，我平时用的多的音色是云扬、晓颜。

说明：macOS 上的 **Keychain（钥匙串）** 是系统内置的**加密凭证管理系统**，本质是一个受密码保护的加密容器，以确保只有机器的主人才能访问。keychain用来安全存储密码、证书、密钥、Wi‑Fi 信息、信用卡号、安全备注等敏感数据，并提供自动填充、跨设备同步与系统级权限控制，是 macOS 安全与便捷的核心组件。

## 本地开源 TTS 引擎

![TTS 设置 screenshot](/help-assets/ttsmate/zh/tts-settings/tts-settings-06.png)

这是给一些有动手能力的网友留的口子，具体思路就是自己在机器上跑一个 TTS 的 web 服务，由 TTSMate 来调用。感兴趣的请关注：

https://github.com/kyinwind/LocalTTS
