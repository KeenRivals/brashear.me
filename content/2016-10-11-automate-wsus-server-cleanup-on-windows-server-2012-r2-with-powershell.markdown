title: Automate WSUS Server Cleanup on Windows Server 2012 R2 with PowerShell
date: 2016-10-11 12:11:01 -0400
tags: powershell, sysadmin, deployment, windows

I recently wanted to automate cleanup of my WSUS server. A lot of posts around the web advocate using strange PowerShell scripts that make .NET calls to work with WSUS or even use third-party applications to do so. That information all seems outdated. On server 2012 R2 you only need [Invoke-WsusServerCleanup](https://technet.microsoft.com/en-us/library/hh826162.aspx).

In my case I created a scheduled task on my WSUS server to run ``powershell`` with the arguments ``-command Invoke-WsusServerCleanup -CleanupObsoleteComputers -CleanupObsoleteUpdates -CleanupUnneededContentFiles -CompressUpdates -DeclineExpiredUpdates -DeclineSupersededUpdates`` on a weekly basis.
