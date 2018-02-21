Title: Tell Windows to Ignore Touch Input When Using the Pen By Default
Date: 2018-02-21T11:29-05:00
Tags: Deployment, Windows, Sysadmin

Windows 10 has a setting to ignore touch input when using the pen. This is pretty nice, as I've found Wacom et. al's palm rejection to be not very good. It's simple enough for users to change themselves if they're aware of the setting, but I don't expect students to figure it out. Thankfully, you can modify the registry for the default user to set the default. When a new user logs in for the first time they'll have the setting applied.

	:::batch
	REM Default the "Ignore touch input when I'm using my pen" setting to on

	REM Load the default users hive
	reg load HKLM\DefaultUsers C:\Users\Default\ntuser.dat

	REM Set the default setting.
	reg add "HKLM\DefaultUsers\Software\Microsoft\Windows NT\CurrentVersion\Windows\Pen" /v PenArbitrationType /t REG_DWORD /d 0x00000001 /f

	REM Unload the default users hive
	reg unload HKLM\DefaultUsers

I have no idea why this setting is off by default. Having it on really improves the pen+touch stylus input for us on our Lenovo Yoga laptops. If you want to change the setting for the current user, you'll change HKCU\Software\Microsoft\Windows NT\CurrentVersion\Windows\Pen instead.