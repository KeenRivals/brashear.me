---
layout: post
title: "Microsoft Visual C++ 2012 Redist Broken After Windows 10 1607 Upgrade"
date: 2016-09-20 18:33:44 -0400
comments: true
categories: windows sysadmin deployment wsus
---
I've been deploying the Windows 10 build 1607 feature upgrade (also known as the Anniversary Update) via WSUS to a test lab at work. The machines are upgrading from 1511. Today I was informed that Autodesk 3ds Max & AutoCad would not launch on those machines. 3dsmax.exe gave an error: *"The procedure entry point __crtCreateSymbolicLinkW could not be located in the dynamic link library C:\WINDOWS\SYSTEM32\MSVCP110.dll."* 

<!-- more -->

# Cause

It seems like the in-place upgrade breaks the installed MS VC++ 2012 libs by replacing them with weird versions. The only evidence I can find online is [KB3119142](https://support.microsoft.com/en-us/kb/3119142 "Update for Microsoft Visual C++ 2012 Update 4 Redistributable Package") from January 2016 which specifically mentions this sort of error with Windows 10. That update supposedly fixes the issue, but there's a lot of [griping online about that update](http://news.softpedia.com/news/microsoft-acknowledges-kb3119142-update-repeated-install-issues-provides-fix-501036.shtml "Microsoft Acknowledges KB3119142 Update Repeated Install Issues, Provides Fix") causing problems. I can't find that update on my WSUS server, so I'm not sure if it's even available for or applicable for Windows 10 build 1607. It you have any idea on that one, please [let me know](mailto:web@brashear.me)! The KB article recommends running a repair install to fix the issue. I can work with that.

# Resolution

To fix the issue, I created an immediate scheduled task which runs the [Visual C++ Redist Installers](https://www.microsoft.com/en-us/download/details.aspx?id=30679 "Visual C++ Redistributable for Visual Studio 2012 Update 4") in repair mode. I used a WMI filter on my Group Policy Object to make the task run only on Windows 10 build 1607 machines.

## The Scheduled Task

Create a GPO which creates an immediate scheduled task. Create a folder on the network available to your machines with the redistributable installers from the link above: *vcredist_x86.exe*, and *vcredist_x64.exe*. Create an action to run ``vcredist_x86.exe /repair /quiet /norestart`` and then ``vcredist_x64.exe /repair /quiet /norestart`` to repair the installation. *Technically* a reboot is needed to complete the install, but the issue is resolved without a reboot. I elect to not reboot because I figure the machines will reboot eventually and I don't want to interrupt someone using the machine.

## The WMI Filter

Since I want this to *only* run on Windows 10 1607. I needed the following WMI filter on my GPO. Namespace ``root\CIMv2`` with the query ``Select BuildNumber from Win32_OperatingSystem WHERE BuildNumber = 14393`` does the job.
