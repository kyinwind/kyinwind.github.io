---
title: "Q&A"
description: "RightClickMate technical support and help center."
---
- F&Q

## **FAQ-1: Cannot Find Extension Switch?**

Different versions of macOS have different Finder extension switch interfaces. On macOS 15.1 System Settings, you indeed cannot find the RightClickMate extension switch.

If after installing RightClickMate, you cannot see custom menus like 'New' and 'Copy Path' when right-clicking on the desktop, please open Terminal and copy and run the following two commands in order:

Restart Finder Plugin

pluginkit -e use -i com.michaeldev.RightClickMate.MyFinderSyncExtension

Restart Finder

killall Finder

After running these two commands, you should see the custom menus when right-clicking on the desktop.
