---
layout: post
title: "Remove All Drivers from a Windows Image by a Certain Vendor"
date: 2014-07-30 18:23:29 -0400
comments: true
categories: [ deployment, sysadmin, dism, powershell ]
---

For when you find that you just need to remove *all* of the drivers from a captured image, or only those of certain makes. PowerShell makes it easy to script this removal so you aren't manually typing a ton of dism commands. I found myself needing to purge some problematic Intel drivers from an image in order to get USB working on some of our older machines. I found that it is possible to remove all drivers from a mounted Windows image and then commit the changes back to the captured WIM completely in PowerShell. Read on if you need the skinny.

<!-- more -->

## Introduction

It's summer time, so naturally I am rebuilding our Windows images for the coming school year. This year we are moving from Windows 7 to Windows 8.1. While we haven't had many issues with incompatible software (Infocus LiteShow, which is garbage on anything other than Windows XP anyways). We have had a lot of problems with getting reliable Windows 8.1 drivers for all of our fleet--which ranges from 5-years-old HP EliteBook 2730p units to brand-spankin' new Lenovo ThinkPad Yoga S1 devices. Naturally, getting Windows 8.1 to run happily on these older devices is complicated by the tendency of <abbr title="Original Equipment Manufacturer">OEM</abbr>s to stop producing drivers for any OS other than the one those in vogue when the device was released. In my tinkering with both <abbr title="Microsoft Deployment Toolkit">MDT</abbr> 2012 and <abbr title="Windows Deployment Services">WDS</abbr> somehow I got some bad Intel chipset drivers in my image that were being used instead of the ones I wanted and causing USB peripherals (but not USB storage) to be nonfunctional. The solution was to purge all of these Intel drivers from my captured WIM files using PowerShell.

Microsoft provides some fairly good documentation on [using DISM within PowerShell](http://technet.microsoft.com/en-us/library/hh825010.aspx). It's definitely worth a looking over. It will help you understand the commands we're using here if you are already familiar with DISM.

### Requirements

  * You need to be running Windows PowerShell 4.0.
  * You need the latest Windows Assessment and Deployment Kit installed.
  
You may also need to import the DISM PowerShell module. There are instructions to [prepare the DISM PowerShell Environment available from Microsoft](http://technet.microsoft.com/en-us/library/hh825010.aspx) (scroll down), but in my case it was already set up.

## Example Scenario

In my example scenario, I have a WIM, *2730p.wim* from which I want to remove *all* of the Intel chipset drivers that were injected into the image at an earlier point in time. I will mount the WIM to D:\Image, and do all of my work there.

Be advised that you need to run PowerShell as an administrator. If you're not running <abbr title="PowerShell">PS</abbr> with admin rights, none of the important bits here will work. You've been warned!

## Mount your Windows Image with PowerShell

Mounting Windows images with PowerShell is handled by ``mount-windowsimage``. In our example, run the following: 

{% codeblock lang:ps1 Mount a Windows image with PowerShell %}
mount-windowsimage -ImagePath D:\2730p.wim -Path D:\Image -Index 1
{% endcodeblock %}

Now, wait while it is mounted. If the ``mount-windowsimage`` cmdlet is not available, make sure you have met the requirements listed above. Once the image is mounted, continue to the next step.

## Get a List of Third-Party Drivers in the Windows Image

Here, we will get a list of all of the drivers in the image and store it in a variable. I like to store it in a variable because fetching the installed drivers takes a long time and I'm a bit impatient so I don't want to wait each time I work with the list of drivers. To fetch a list of installed drivers from the image, use the ``get-windowsdriver`` command. I stored the result in a variable with:

{% codeblock lang:ps1 Get a list of drivers in an image with PowerShell %} 
$drivers = get-windowsdriver -path D:\Image
{% endcodeblock %}

From here, it's a good idea to browse the list of drivers in the image to find out what drivers you want to remove. Type ``$drivers`` followed by enter and you'll get a (long) list. 

## Remove Third-Party Drivers by a Certain Vendor from a Windows Image

Next, I want to use my ``$drivers`` variable and a little filtering to nuke all Intel drivers from the image. To do the filtering, we will use ``where-object``, then for the removing we will pipe the output to ``remove-windowsdriver``. Through the magic of PowerShell, the passed objects will be removed from the image one by one. 

If you want to remove the drivers by a different vendor, take note of the "Provider Name" property for those drivers and use that. In my example I filter by ProviderName, but you could filter by *any* of the properties available with the where-object command. Some handy ones might be ``ClassName`` or ``BootCritical``. See the examples below.

{% codeblock lang:ps1 Remove all Intel drivers from the Windows image %} 
# Remove all Intel drivers from the image
$drivers | where-object {$_."ProviderName" -eq 'Intel' }  | Remove-WindowsDriver -Path D:\Image

# Alternatively, remove all drivers from the image
$drivers | Remove-WindowsDriver -Path D:\Image
{% endcodeblock %}

Once you're done, you can check what drivers are left in the image with:

{% codeblock lang:ps1 Get a list of drivers remaining in the image %} 
$drivers = get-windowsdriver -path D:\Image
{% endcodeblock %}

If everything is good, you are free to commit the image.

## Commit Changes to a Windows Image with PowerShell

Unmounting (and committing) an image is completed with the ``dismount-windowsimage`` command, as below.

{% codeblock lang:ps1 Dismount a Windows image with PowerShell %}
# If you don't want to save the changes, use the -discard option.
Dismount-WindowsImage -Path D:\Image -save
{% endcodeblock %}

From here, you have a nice clean Windows image! No more unruly drivers!
