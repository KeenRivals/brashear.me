Title: How to Deploy Windows 10 Default Taskbar Settings
Date: 2018-02-21T09:56-05:00
Tags: Deployment, Sysadmin, Windows

Windows 10 adds quite a few default buttons to the taskbar. Most of my users don't need or want them, so I've taken to hiding them by default. I don't want to use Group Policy for this, as I want users to be able to change it if they want. I accomplish this by baking some defaults into the image.

The method is documented in my [Win10-Default-Taskbar-Settings](https://github.com/KeenRivals/Win10-Default-Taskbar-Settings) repository on GitHub. In summary, I load the Default users' registry hive, apply some registry edits, then unload the hive. New users will get these registry settings when their profile is created.

Here's the script at time of writing.

	:::batch
	:: Default Taskbar Settings
	:: Apply some defaults to the appearance of the user taskbar.

	:: Load the default user's registry hive.
	reg load HKLM\DefaultUsers C:\Users\Default\ntuser.dat

	:: Hide the taskbar search button by default.
	reg add HKLM\DefaultUsers\Software\Microsoft\Windows\CurrentVersion\Search /v SearchboxTaskbarMode /t REG_DWORD /d 0

	:: Hide the Task View button by default.
	reg add HKLM\DefaultUsers\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v ShowTaskViewButton /t REG_DWORD /d 0

	:: Hide the People button by default
	reg add HKLM\DefaultUsers\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced\People /v PeopleBand /t REG_DWORD /d 0

	:: Unload the default user's hive
	reg unload HKLM\DefaultUsers