title: Getting Adobe Creative Cloud Enterprise to Install from a Network Share
date: 2014-04-02 13:19:04 -0400
tags: deployment, msi, sysadmin, adobe

I've been fighting geting Adobe Creative Cloud to install properly from a LiteTouch deployment share. In my troubleshooting, I was always able to install the exceptions just fine, but the MSI package created by Adobe's Creative Cloud Packager would not run successfully from a network share. When I tried to log what was happening, I kept getting a 1603 error in the InstallFinalize step along the lines of the following:
<!-- more -->


	Action start 13:33:43: InstallFinalize.
	CustomAction CADeploy returned actual error code 1603 (note this may not be 100% accurate if translation happened inside sandbox)
	Action ended 13:34:15: InstallFinalize. Return value 3.
	Action ended 13:34:15: INSTALL. Return value 3.

	-- Lines Omitted --

	=== Logging stopped: 4/2/2014  13:34:15 ===
	MSI (s) (B4:2C) [13:34:15:574]: Product: AdobeCreativeCloud -- Installation operation failed.

	MSI (s) (B4:2C) [13:34:15:574]: Windows Installer installed the product. Product Name: AdobeCreativeCloud. Product Version: 1.2.0000. Product Language: 1033. Manufacturer: Adobe Systems Incorporated. Installation success or error status: 1603.


In my experience, error 1603 usually means some sort of file access issue (either it is missing or you don't have permissions to access it). What was confusing was that when I ran the deployment from a local drive it was always successful. After searching forums and Google for many hours I decided to come up with my own workaround. I zipped up the "Build" folder in my created package, and then wrote a batch script to extract the Build folder to a temporary directory and then install from there. This method has worked every time. The only downside is that it is a bit slower than the method that should work (and used to when I created an Adobe CC package around the same time last year).

If you'd like to recreate my resolution:
  1. Download [7-zip](http://7-zip.org) and extract 7z.exe and 7z.dll from the installer. 
  2. Copy these files to your Adobe CC package folder (same one that has *packagename*.ccp).
  3. Create a ZIP file of your Build folder in your Adobe CC package folder. Mine is just Build.zip.
  4. In your silent install script, just extract the Build.zip file to a temporary folder and install the MSI package from there.

You can use my own silent installation script to see how this is all done.

	:::bat
	pushd "%~dp0"

	REM Install Adobe applications that much be installed before the main package.
	start /wait /D "Exceptions" "ExceptionsDeployer" Exceptions\ExceptionDeployer.exe --workflow=install --mode=pre --installLangauge=en_US

	REM Extract the Adobe CC "Build" folder to a temporary directory and install
	start /wait "Adobe CC Extraction" 7z.exe x -o%temp%\AdobeCCBuild Build.zip
	start /wait "Adobe CC Install" msiexec /i %temp%\AdobeCCBuild\Build\AdobeCreativeCloud.msi /qb

	REM Install Adobe applications that must be installed after the main package
	start /wait /D "Exceptions" "ExceptionsDeployer" Exceptions\ExceptionDeployer.exe --workflow=install --mode=post

	REM Update Adobe Acrobat XI to 11.0.06
	start /wait "Acrobat Update" msiexec /p AcrobatUpd11006.msp /qb

	REM Remove the temporary directory we created. 
	rmdir /s /q %temp%\AdobeCCBuild
