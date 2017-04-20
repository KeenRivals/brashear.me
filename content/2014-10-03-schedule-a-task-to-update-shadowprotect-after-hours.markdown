---
layout: post
title: "Schedule a Task to Update ShadowProtect After Hours"
date: 2014-10-03 13:47:10 -0400
comments: true
categories: ShadowProtect Deployment Windows
---

Recently I needed to deploy some updates to some computers running [StorageCraft ShadowProtect](http://www.storagecraft.com/products/overviews/storagecraft-shadowprotect). In doing this, I was faced with three problems:

1. After installing the update, backups cannot be performed until you reboot.
2. I cannot reboot the servers during work hours.
3. I am going out of town this evening to see my girlfriend and I don't want to update remotely.

The solution here is a little automation with the help of a little batch and `schtasks` on my workstation.

<!-- more -->

Silently Installing ShadowProtect
=================================

[StorageCraft's documentation](http://www.storagecraft.com/support/kb/article/200) on silently installing ShadowProtect is worth a read. The most important parameter is *OMIT*. The *OMIT* parameter specifies which products you wish to install. If you only want the backup capability on this machine, you can omit everything except *Agent* (as I do). Delete OMIT parameters for features you want. Using this information, I've now got a batch file that will install ShadowProtect on a server and reboot it:

{% codeblock lang:bat Update-ShadowProtect.bat %}
pushd %~dp0

start /wait ShadowProtectSetup_5.2.0.exe install IACCEPT=STORAGECRAFT.EULA LANG=en OMIT=Console OMIT=Mount OMIT=VirtualBoot
shutdown /r /t 30
{% endcodeblock %}

This script will run *ShadowProtectSetup_5.2.0.exe* from the script's directory in silent mode and install *only* the agent. To deploy using this script, copy it to a share accessible by your server(s), and then you can proceed with scheduling a task to deploy it. In my example, I've got the deployment script and installer at "\\example.com\Install\StorageCraft ShadowProtect 5.2.0\install.bat".

Using Schtasks to Schedule a Task to Deploy ShadowProtect
=======

The [schtasks](http://msdn.microsoft.com/en-us/library/windows/desktop/bb736357%28v=vs.85%29.aspx) tool is the magic here. It allows me to schedule processes that will run on a remote computer at whatever time I specify. The template command we will use is the following:

{% codeblock lang:bat %}
schtasks /create /S server /tn "Install ShadowProtect" /tr "\"\\example.com\Install\StorageCraft ShadowProtect 5.2.0\install.bat" /sc once /st 20:00 /ru "System"
{% endcodeblock %}

This tells `schtasks` to create on **server** a task called **Install ShadowProtect** that runs the command **\\example.com\Install\StorageCraft ShadowProtect 5.2.0\install.bat** **once** at **20:00** (8pm) local time as the **System** account. For each of our servers, replace *server* with the server name and the task will be scheduled. Note that this will only work if:

 * Your firewall doesn't block the task scheduler RPC server.
 * The path for your *install.bat* script is accessible to the server's computer account.
 * The time 20:00, is *after* the current time. I've noticed that since we did not specify a startdate with */sd*, if the time is before the time you run the command (even if it's midnight) schtasks will complain. If you want this task to run at midnight the next day, you will need to specify */sd* in the command (see the [schtasks reference](http://msdn.microsoft.com/en-us/library/windows/desktop/bb736357%28v=vs.85%29.aspx) for details.
 * Your server is Windows Server 2008 or later. I've had Windows Server 2003 hosts not like the specification of the SYSTEM user for schtasks. The way I got it to work was to create the task manually on those hosts, but there may be some other workaround (thankfully, I don't have many 2k3 hosts).

Check the output from the schtasks command, and if it does not complain you can expect your task to run as scheduled. I highly recommend starting with a test host or two and creating the task for 1-2 minutes in the future so you can verify your program/script runs correctly. Once you have that ironed out, it's safe to deploy to your other servers.
