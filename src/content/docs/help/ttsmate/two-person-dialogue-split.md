---
title: "Two-Person Dialogue Split"
description: "TTSMate technical support and help center."
---
### Dialogue Split Rule Settings

Click the "Dialogue Split" button in the toolbar to enter the dialogue split rule settings interface.

As shown, if your imported document contains dialogue and you want the app to automatically recognize it and use different A/B voices for conversion, you need to configure dialogue split rules.

Generally, each dialogue pattern requires one split rule to be configured.

When entering rules, if you're not familiar with regular expressions, you can click "Reference Examples" for guidance.

Dialogue split rules you create can be exported for backup or imported.

Important: Only after split rules are configured will subsequently imported documents automatically apply split rules for dialogue separation.

The icon shown in the chapter list will change to:

### Supported Dialogue Split Pattern 1 (Question-Answer type, both Q and A are explicit and fixed):

Zhang San: Excuse me, how do I get to XXX neighborhood?

Li Si: Follow this road, turn right at the intersection, and it's 500 meters ahead. The entrance faces south.

Explanation:

This Q&A format is relatively easy to split. All questions are preceded by "Zhang San:", and all answers by "Li Si:", making it easy for the program to identify.

Suggested split rule: 张三\s*[:：]\s*([\s\S]*?)\s*李四\s*[:：]\s*([\s\S]*)

### Supported Dialogue Split Pattern 2 (Q&A where the questioner varies but the answerer is explicit and fixed):

Zhang San:

Master, would a low-level question be okay? Can one wear a dzi bead while practicing with you? Any taboos?

Master:

Zhang San, I have no interest in any bodily ornaments. I never recommend wearing anything. If you fear disturbances, chant the Great Compassion Mantra. Practice one mantra to the utmost, to the point where you can recite it even in dreams, and that will suffice. However, the Great Compassion Mantra carries destructive power, so the chanter should maintain a compassionate heart like Guanyin Bodhisattva. If you chant with a mind of hatred, it can harm other sentient beings.

Explanation:

For example, in the above case, since the questioner is not fixed, it's harder to identify who is asking. But the answerer is consistent—always "Master:".

Moreover, this type of dialogue is a single Q&A exchange that ends, and the program can also support splitting.

Suggested split rule: \s*([\s\S]*?)大师\s*[:：]\s*([\s\S]*)

Strictly speaking, there are no unsupported split rules, but the program currently supports simpler patterns like the two described above. If you have more complex dialogue patterns, please email examples to yangxuehui@outlook.com, and I'll analyze whether they can be supported.
