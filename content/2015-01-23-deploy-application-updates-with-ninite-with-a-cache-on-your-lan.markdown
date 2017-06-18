title: Deploy Application Updates with Ninite with a Cache on your LAN
date: 2015-01-23 13:10:47 -0500
tags: sysadmin, deployment, ninite, powershell, windows
summary:  Recently we purchased [Ninite Pro](https://ninite.com/pro) for our organization and have implemented silent application updating via a scheduled task with PowerShell. This process uses a cache on our LAN to store updates and speed the whole process along. After some thinking I decided I wanted to get this working off-site so that when students take their laptops home over the summer, they can continue to receive updates.

Recently we purchased [Ninite Pro](https://ninite.com/pro) for our organization and have implemented silent application updating via a scheduled task with PowerShell. This process uses a cache on our LAN to store updates and speed the whole process along. After some thinking I decided I wanted to get this working off-site so that when students take their laptops home over the summer, they can continue to receive updates.

# Overview

The goal here is to cover two update scenarios:

1. When on-site, update from our cache on the LAN.
2. When off-site, update without a cache.

To accomplish this, we deploy a PowerShell script and a copy of Ninite Pro to the computers' C:\Windows\Temp directory. From there a scheduled task runs daily to run the PowerShell script. The script checks for the availability of a local cache and if that's not available it updates without it. Ninite will save a report for the computer to your server's *Reports* directory.

# Configure your on-site cache and report folder

For your on-site cache to work via this method, you need to create a network folder which is accessible to the computers in your domain. In that folder, you need two special directories: *Cache* and *Reports* which are writable by your *Domain Computers* Active Directory group. This is necessary so that computers can cache their downloads and save their reports. Your directory tree will look something like this:

* `\\example.com\Ninite\`
    * **Cache\\** - Directory writeable by Domain Computers group.
    * **Reports\\** - Directory writeable by Domain Computers group.
    * **Ninite-Offsite.ps1** - PowerShell script for deployment.
    * **NinitePro.exe** - Ninite Pro installer.

# Configure Ninite-Update.ps1

The script below is what enables the magic. In summary, it tests if it can connect to your file server, *file.example.com*. If it can, it updates applications using the installer and cache on the server. If it cannot access your file server, it updates from C:\Windows\temp\Ninite instead. We will use a GPO to push *NinitePro.exe* and *Ninite-Offsite.ps1* to C:\Windows\temp a little later.

In this script, Ninite is run in update-only mode for specifically listed applications. The installer will prevent the creation of shortcuts and auto-update functions by the installed applications.

	:::ps1
	# Ninite Pro App Selection List
	# https://ninite.com/applist/pro.html
	Set-Variable APPS -option constant -value '"7-Zip" QuickTime Acrobat Air Audacity Firefox Flash "Flash (IE)" "Google Drive" "Google Earth" GIMP Inkscape Java "KeePass 2" "Notepad++" Reader Shockwave SumatraPDF VLC'
	 
	 
	function updateOnsite ($apps) {
		$dir = "\\example.com\Ninite"
		Push-Location $dir
		
		& .\NinitePro.exe /silent $dir\Reports\$env:computername.txt /updateonly /select $apps /cachepath $dir\Cache /disableautoupdate /disableshortcuts
	} 
	 
	function updateOffsite($apps) {
		$dir = "C:\Windows\temp\Ninite\"
		Push-Location $dir
		
		& .\NinitePro.exe /silent $dir\$env:computername.txt /updateonly /select $apps /disableautoupdate /disableshortcuts
	}
	 
	function main () {
		if (Test-Connection file.example.com -quiet) {
			updateOnsite $APPS
		} elseif (Test-Path "C:\Windows\Temp\Ninite\NinitePro.exe" ){
			updateOffsite $APPS
		}
	}
	 
	main

You need to customize this script to fit your environment. 

1. **Line 3**: Customize this list with the applications you wish to update.
2. **Line 8**: Change this to your Ninite installer folder.
3. **Line 22**: Change *file.example.com* to your file server's hostname.

# Create a GPO to deploy Ninite Pro and Schedule Updating

1. In Group Policy Management, create a new policy named *Update Applications with Ninite*. 
2. Go to **Computer Configuration** > **Preferences** > **Windows Settings** > **Files**.
3. Right-click and choose *New* > *File*.
4. Set *Action* to **Replace**. 
5. Set the source file to **`\\example.com\Ninite\NinitePro.exe`**.
6. Set the destination file to C:\Windows\Temp\Ninite\NinitePro.exe.
7. Click **OK**.
3. Right-click and choose **New** > **File*.
4. Set *Action* to **Replace**. 
5. Set the source file to **`\\example.com\Ninite\Ninite-Offsite.ps1`**.
6. Set the destination file to **C:\Windows\Temp\Ninite\Ninite-Offsite.ps1**.
7. Click **OK**.

Now you just need to create a scheduled task to run Ninite-Offsite.ps1. The goal is that the task should run once a day during an eight hour window (while the kids are at school) between 7am and 3pm.

1. Viewing the GPO, go to **Computer Configuration** > **Control Panel Settings** > **Scheduled Tasks**.
2. Right-click in the window and choose **New** > **Scheduled Task (At least Windows 7)**.
3. On the *General* tab:
    1. Set the name to **Ninite-Update**.
    2. Run the task as **NT AUTHORITY\System**. Check **Run with highest privileges**.
    4. Click **OK**.
4. On the *Triggers* tab, create a new trigger:
    1. Begin the task on a schedule.
    2. Run the task daily.
    3. Set the start for today @ 7am. 
    4. Delay the task for up to 8 hours.
    5. Make sure the **Enabled** box is checked.
    4. Click **OK**.
5. On the *Actions* tab, create a new action:
    1. The action should be **Start a program**.
    2. Program/script: **powershell**
    3. Add arguments: **-ExecutionPolicy Bypass -file C:\Windows\Temp\Ninite\Ninite-Offsite.ps1**
    4. Click **OK**.
6. On the *Conditions* tab, check the **Start only if the following network connection is available** then select **Any connection**.
7. On the *Settings* tab:
    8. Check **Allow task to be run on demand**. This helps with testing.
    9. Check **Run task as soon as possible after a scheduled start is missed**. This makes it so if a PC is offline during a scheduled start, it starts ASAP when it comes back online.
8. Click **OK**. Your task is ready.

From here you are ready to test.

# Testing your scheduled task

You can test your Ninite deployment task by opening up the Windows Task Scheduler and finding your scheduled task. If you right-click the task you can run it on demand. Check `\\example.com\Ninite\Reports\` for a log indicating success. Ninite logs normally list what applications were updated. If the log contains only **OK**, then no apps were available for update.

## Common Issues

When I was setting this up I ran into some problems. If you have trouble, try checking these first:

* Make sure the permissions on your file share are correct. The *computer account* needs access to the file share when you run a task as *NT AUTHORITY\System*.
* Make sure your destination files are explicitly set in your GPO. Copying *`\\example.com\Ninite\NinitePro.exe`* to C:\Windows\Temp\Ninite doesn't do what you expect! You need to specify the destination file name!

Good luck out there!
