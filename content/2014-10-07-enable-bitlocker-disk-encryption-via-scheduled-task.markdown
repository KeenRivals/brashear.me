title: Enable Bitlocker Disk Encryption Via Scheduled Task
date: 2014-10-07 10:26:47 -0400
tags: windows, bitlocker, deployment
summary: I've been working on deploying Bitlocker across our Active Directory domain via a scheduled task. The advantage of using a scheduled task to enable Bitlocker (versus a startup or shutdown script) is that I can configure it to run when the computer is idle. I liked this solution over a startup script because my users on laptops very *very* rarely reboot their computers, and so startup scripts very *very* rarely get a chance to run.

I've been working on deploying Bitlocker across our Active Directory domain via a scheduled task. My goals here were as such:

 * Enable encryption on any platform which is capable of running it.
 * Prepare the disk for encryption (if necessary).
 * On some of our devices (HP EliteBooks) the TPM was not enabled by default, so I needed to enable it.

The advantage of using a scheduled task to enable Bitlocker (versus a startup or shutdown script) is that I can configure it to run when the computer is idle. I liked this solution over a startup script because my users on laptops very *very* rarely reboot their computers, and so startup scripts very *very* rarely get a chance to run.

# Prepare the Script

We only have two vendors worth of laptops in our environment: Lenovo and HP. Our Lenovos are all ThinkPad Yoga units, which are capable of running Bitlocker already. The HPs (EliteBook 2730p, 2740p, and 2760p units) were not configured correctly by me when imaged, and so I need to tweak them before I can enable encryption. Namely, they:

 * Do not have the proper disk layout (no dedicated system partition).
 * Do not have their TPM enabled.

Both of these issues are relatively easy to remedy:

 * To fix the disk layout, I need to run `bdehdcfg -target default -quiet` and then reboot the machine. 
 * To enable the TPM, I need to apply a BIOS change and then reboot the machine.

These two steps can be completed at the same time. Once the machine is rebooted, we can enabled encryption. 

I created a PowerShell script that handles all of this for me. This script is reproduced below, but be aware that you will probably need to customize it a little for your environment. In short, it detects if the disk is encrypted via WMI, then if the vendor is HP, it applies a BIOS configuration change and corrects the disk layout if necessary. From there, if there is an encryptable C: volume, it encrypts that volume. On the HPs, there will not be an encryptable volume until the machine reboots. If the machine is a Lenovo, enable the encryption. In our environment the Lenovos are already set up properly so we just enable the encryption. 

Note:

 * Before doing this you should have already set up your group policies so that Bitlocker keys are automatically backed up to Active Directory.
 * This script uses the Get-TPM cmdlet, which is only available on Windows 8.1 (I believe). If you are using Windows 7 or Windows 8, you will need to use WMI. I chose to use the cmdlet because everyone here is on Windows 8.1 and I find WMI to be kind of gross.

		:::powershell
		
		# Name:	Enable-Bitlocker.ps1
		# Usage: Enable-Bitlocker.ps1
		# Description: 
		#	Enables the Trusted Platform Module (TPM) on HP EliteBook machines so that 
		#	Bitlocker encryption with TPM unlock can be used. It can also prepare the 
		#	disk drive on HPs for encryption.
		#
		#	If conditions are correct, encrypt the drive.

		# Returns the directory from which the script is running.
		function Get-ScriptDirectory {
			$Invocation = (Get-Variable MyInvocation -Scope 1).Value
			Split-Path $Invocation.MyCommand.Path
		}

		pushd (get-scriptDirectory)

		# Get the target volume's encryption properties.
		$volume = Get-WmiObject win32_EncryptableVolume `
			-Namespace root\CIMv2\Security\MicrosoftVolumeEncryption `
			-Filter "DriveLetter = 'C:'"

		# Get the target system's manufacturer.	
		$manufacturer = (get-wmiobject win32_computersystem).Manufacturer

		# If the manufacturer is HP, and the volume is not encrypted, prepare it.
		if ( $manufacturer -eq "Hewlett-Packard" -and ( $volume.encryptionmethod -eq 0 -or !$volume) ) {
			
			$tpm = get-TPM
			
			# Is the TPM not enabled? Enable it.
			if ( $tpm.TpmReady -eq $false ) {
				.\BiosConfigUtility64.exe /SetConfig:Enable-TPM.cfg /cspwd:biospassword /cspwd:""
			} 
			
			# Is there not an encryptable volume? Make C: encryptable with bdehdcfg.
			if ( -not $volume ) {
				bdehdcfg -target default -quiet
			} 
			
			# Is the TPM ready and the volume encryptable? Encrypt it.
			if ($tpm.TpmReady -eq $true -and $volume ) {
				manage-bde -on c: -s -rp
			}	
		} 

		# If this is a Lenovo machine that is not encrypted, encrypt it.
		if ( $manufacturer -eq "LENOVO" -and $volume.encryptionmethod -eq 0 ) {
			manage-bde -on c: -s -rp
		}

The script uses the [HP BIOS Configuration Utility (BCU)](http://ftp.hp.com/pub/caps-softpaq/cmit/HP_BCU.html) available for HP devices as part of the HP System Software Manager. The configuration file used in my script is below. This is confirmed to work on the HP EliteBook 2730p, HP EliteBook 2740p, and the HP EliteBook 2760p. In the BiosConfigUtility64 command, you will need to specify your BIOS admin password with the `/cspwd:` parameter. One handy feature is that you can supply multiple passwords with multiple `/cspwd` parameters. A (kind of) hidden setting in the HP BIOS is the `Embedded Security Activation Policy` feature. This isn't exposed in the BIOS UI, but when you use the BCU to get the BIOS's configuration it will be there. This setting determines whether or not your users will be given the chance to accept or reject activation of the TPM when the machine is rebooted. Naturally, I did not want to give my users the chance to reject enabling their TPM, so the setting is changed to `No prompts`.

	English
	TPM Reset to Factory Defaults
		Yes
		*No
	Reset of TPM from OS
		*Disable
		Enable
	OS Management of TPM
		Disable
		*Enable
	Activate Embedded Security On Next Boot
		Disable
		*Enable
	Embedded Security Device Availability
		*Available
		Hidden
	Embedded Security Activation Policy
		F1 to Boot
		Allow user to reject
		*No prompts

Once you have the script ready, you need to put it and the BCU (if needed) somewhere accessible via your domain computers. I chose a public install share, \\example.local\Install\Bitlocker\.

# Schedule a Task to Enable Bitlocker via PowerShell

Once the script is ready, it is time to use Group Policy to create a Scheduled Task on our computers to run the script. 

 1. Create a new GPO and navigate to Computer Configuration\Preferences\Control Panel Settings\Scheduled Tasks. 
 2. Create a new task (Enable Bitlocker).
 3. Use Action: Update.
 4. Run as the NT Authority\System user.
 5. Check "Run with highest privileges".
 6. Configure for: "Windows 7".
 8. Trigger: On idle.
 9. Actions: Start a program.
   * Program/script: powershell
   * Add arguments(optional): -ExecutionPolicy Bypass -file \\example.local\Install\Bitlocker\Enable-Bitlocker.ps1
   * Start in(optional): \\example.local\Install\Bitlocker\
 10. Conditions
   * Check *Start the task only if the computer is idle for 1 minute.*
   * Wait for idle for: 2 hours
 11. Settings
   * *Allow task to be run on demand* (helps with testing).
   * Run task as soon as possible after a scheduled start is missed
   
Now you have your scheduled task created. If you want to test some computers, run `gpupdate /force` on them. View the task scheduler and in the library you should see your task to enable Bitlocker. If you run it manually, the disk should start encrypting if the script determines conditions are right. Note that in the action, we set powershell's execution policy to *bypass*. This is very important on machines which may have their execution policy set to something restrictive. Your scheduled task will run, but PowerShell will not actually run the script if you do not use the `-ExecutionPolicy Bypass` parameter to `powershell.exe`. This is the key to running *any* PowerShell script via a scheduled task. This execution policy "feature" was driving me crazy while I was in testing.
