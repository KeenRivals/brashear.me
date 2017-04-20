---
layout: post
title: "Fix non-working G930 headset after Windows 10 upgrade"
date: 2016-02-26 20:23:00 -0500
comments: true
categories: windows
---

I like my [Logitech G930 wireless headset](http://amzn.to/1Qj2vbV), but I also like running Windows 10 Preview builds. It seems like after every upgrade my headset stops working. I simply get no audio out of it. Reinstalling the application does not solve the problem. After every upgrade, I follow these steps to fix the audio:

1. Exit the Logitech Gaming Software application.
1. Open Explorer.
2. In the address bar, go to ``%userprofile%\AppData\Local\Logitech``
2. Delete the ``Logitech Gaming Software`` folder.
2. Restart the Logitech Gaming Software application.

Audio should work again!
