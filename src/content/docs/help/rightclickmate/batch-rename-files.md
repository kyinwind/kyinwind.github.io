---
title: "Batch Rename Files"
description: "RightClickMate technical support and help center."
---
- Batch Rename Files

## Operation Guide

Select multiple files (cannot include folders, otherwise the batch rename menu will not appear), right-click, and click 'Batch Rename' to enter the batch file renaming interface.

The upper part of the interface shows the file list for this rename operation. In the list, the left side is the original file name, and the right side is the expected new name.

If there is a checkmark, the rename is expected to proceed without issues. If there is an error message, the selected rename rules have problems, such as file name conflicts.

As shown in the figure, assuming we have these files, if we want to remove meaningless dates and numbers, and add shooting scenes, person information, etc., we need to:

1. Add 'Replace Text' action

Replace 'iShot_2026-04-11' with an empty string

1. Add 'Add Prefix' action

Add prefix: '0411-Canal Park Spring Outing-Family Portrait'

1. Then add 'Delete Characters' action

At this point, there are still some meaningless characters at the end of the file names, all 9 characters long.

Select the delete characters action, as shown above.

At this time, all file names become the same, so there is a warning on the right side of the list. Don't worry about it for now, because we will add sequence numbers later.

As shown in the figure, add sequence numbers, can be at the front or back.

After adding the sequence numbers, the warning on the file list disappears.

At this point, if you confirm this is what you want, click 'Confirm' to actually rename the files.

*If some actions are frequently used, you can click 'Save Rule' to save the rule for later use.

*If you add a wrong action, you can click 'Delete' and re-add.

## Action List Introduction

The action list contains various rules that can modify file names:

Add Prefix

Simply enter the prefix text to add.

Add Suffix

Note that the suffix is added to the end of the file name, not the end of the file extension.

Insert Text

You can choose three positions to insert text:

First is the beginning of the file

Second is the end of the file, which means after the extension, generally this will break the existing file extension

Third is before the file extension, which is the end of the file name, not breaking the extension

Delete Characters

Delete characters can start counting from the beginning of the file to delete a specified number of characters, or start from the end of the file name to delete a specified number of characters.

Replace Text

Normal mode replaces a specified string with a new string, for example replacing '2025' with '2026'.

Regular expression mode is for developers, for example:

When batch renaming, I want to replace characters but not replace all of them. What should I do?

Answer: Use regular expression replacement.

Find pattern: ^([^]*)

Replace with: \$1.

This means replacing the first underscore in the file name with a dot.

Sequential Numbering

When multiple files need numbering, use the 'Sequential Numbering' action.

As shown in the figure above, you can add a two-digit number at the beginning of the file, starting from 1, incrementing by 1 each time, padding with zeros if less than two digits.

There are three positions, as shown above.

Text Transform

This action handles the connection between characters and uppercase/lowercase.

Insert Date

You can insert time at the beginning, end, or before the extension of the file. There are two types of time: creation time and modification time. The time information is taken from the file itself.

Change Extension

Delete Leading Numbers
