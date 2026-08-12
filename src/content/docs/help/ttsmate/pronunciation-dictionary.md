---
title: "Pronunciation Dictionary"
description: "TTSMate technical support and help center."
---
<grid>
<column width-ratio="0.500000">
![Pronunciation Dictionary screenshot](/help-assets/ttsmate/en/pronunciation-dictionary/pronunciation-dictionary-01.png)
</column>
<column width-ratio="0.500000">
![Pronunciation Dictionary screenshot](/help-assets/ttsmate/en/pronunciation-dictionary/pronunciation-dictionary-02.png)
</column>
</grid>

As shown above, the left image shows the Pronunciation Dictionary settings page for the Apple TTS engine and engines like Qwen3TTS and MOSSTTSNano. The right image shows the dictionary page for the Azure TTS engine.

### All Engines

Method: Polyphonic Character Replacement

Engines such as Qwen3TTS and MOSSTTSNano do not have an explicit API for specifying polyphonic character pronunciation. Therefore, the dictionary implementation works by replacing polyphonic characters with phrases or short sentences that have unambiguous pronunciation.

For example, in the phrase "一行数字" (a row of numbers), the character "行" should be pronounced "hang" (row). Without special handling, it may sometimes be pronounced as "xing" (to walk). So the replacement rule replaces "一行数字" with "一航数字". (Note: the replacement character should ideally not itself be polyphonic, so the pronunciation matches as intended.)

This method actually works for all engines, but the Apple local engine and Azure engine also have more explicit methods for specifying polyphonic pronunciation.

### Apple Local TTS Engine

Method: Use Pinyin Directly

The Apple local TTS engine supports Pinyin-based pronunciation. For example:

For the phrase "长安城中长老讲长经", to ensure correct pronunciation, it can be replaced with: "chang2安城中zhang3老讲chang2经"

Add 1, 2, 3, or 4 after the Pinyin to indicate the tone.

### Azure TTS Engine

For the Azure TTS engine, polyphonic character pronunciation can be specified using SSML format.

For characters mispronounced by TTS—for example, "地藏经" may sometimes be read as "di cang jing" instead of the correct pronunciation—pronunciation rules need to be set up to correct the engine's output.

For example, we add a dictionary entry for "地藏经" as shown above.

Original text: 地藏经

Replacement: 地藏经

This syntax follows the SSML (Speech Synthesis Markup Language) specification defined by Microsoft's TTS engine, which allows specifying the pronunciation of a particular character.

Users may struggle with typing characters with tone marks, such as "zàng", where "à" is difficult to input with standard input methods. My suggestion is to ask a large language model like DeepSeek, Doubao, Wenxin, or Qwen for help.

Prompt: "Please provide the Pinyin pronunciation with tone marks for the three characters '地藏经'." After the model responds, simply copy the result.

Once you've maintained your commonly used dictionary, you can export it for backup or import an existing one.

After maintaining the pronunciation dictionary, subsequent audio file conversions will automatically apply the dictionary's replacement rules.
