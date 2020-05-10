title: How to use Cincinnati Bell Fioptics with your own router
date: 2015-09-23 12:37:33 -0400
modified: 2020-05-09T23:16-04:00
tags: networking
summary: I recently purchased gigabit Fioptics Internet service from Cincinnati Bell. At first I was hesitant to go through with it. I did not want to use a crappy ISP router and forgo my wonderful [ASUS RT-AC86U](https://amzn.to/2EMMxcz) or be stuck running some sort of NAT-behind-NAT nightmare network. The day after installation, I took it upon myself to get my ASUS gateway working and remove Cincinnati Bell’s router. I was able to do this while keeping my Fioptics TV and on-demand features working. It was easy, but there is not much guidance out there on the Internet so I figured I would document my setup online. 

I recently purchased gigabit Fioptics Internet service from Cincinnati Bell. At first I was hesitant to go through with it. I did not want to use a crappy ISP router and forgo my wonderful [ASUS RT-AC86U](https://amzn.to/2EMMxcz) or be stuck running some sort of NAT-behind-NAT nightmare network. The day after installation, I took it upon myself to get my ASUS gateway working and remove Cincinnati Bell’s router. I was able to do this while keeping my Fioptics TV and on-demand features working. It was easy, but there is not much guidance out there on the Internet so I figured I would document my setup online. 

Disclosure: This article contains Amazon referral links. I receive a small amount of money if you make a purchase. This keeps my website running and funds my video game habit.

# Requirements

* Your router needs to support [IGMP proxying and IGMP snooping](https://en.wikipedia.org/wiki/IGMP_snooping). The [ASUS RT-AC66U](https://amzn.to/2WhBxdN), [ASUS RT-AC86U](https://amzn.to/2EMMxcz), or the [ASUS RT-AC88U](https://amzn.to/2qdDmI3) are a good choice depending on your budget and performance needs.
	* I'm sure other vendors make home routers with proper IGMP support. This is an exercise I leave to you. Using a [modern wireless router](https://amzn.to/1UtRodX) is a good start. Read the manual!
	* I've looked at the [Netgear Nighthawk routers](https://www.amazon.com/gp/search/ref=as_li_qf_sp_sr_tl?ie=UTF8&tag=brashearme-20&keywords=Netgear Nighthawk&index=aps&camp=1789&creative=9325&linkCode=ur2&linkId=7755e91e846271f4516d8f1c394604e4). They are nice devices but don't support easily support TV service like the ASUS routers do. If you only need Internet, those are an option.
* If you're on gigabit service, your router also needs to support gigabit ethernet. Most routers do these days.
* **Optional**: Your router should support MAC cloning/spoofing. This feature is also common.

# General Guide

## Disconnect your Cincibell gateway and clone its MAC address

This section is optional, and may be paranoia on my part. I want my router to present the same MAC address to Cincinnati Bell as their router. I'm sure that if they really looked they can determine I'm not using their router. I simply don't want to call their support and have the first thing they say be that I'm not using their router. The MAC is printed somewhere on the Cincinnati Bell gateway. Make a note of it. Make sure you get the ethernet MAC address the gateway uses and *not* the WLAN MAC address. 

1. Once you know the gateway's MAC address, it's time to go offline. Disconnect the CB gateway and your router from the Internet. My thinking is I don't want Cincinnati Bell to ever see my router's true MAC if I can help it.
1. Log in to your router and tell it to use the MAC address you got from the gateway. On the ASUS RT-AC86U, this is under *WAN* > *Internet Connection* tab > *Special Requirement from ISP*. You may [view this screenshot for reference]({filename}/images/RT-N66U-MAC-Address-Setting.png).
1. Apply those settings. Once you've done that and given the router time to reboot you can connect it to the Internet again. This is the easy part. You should find that your Internet works just fine. I was a little surprised given how Cincinnati Bell swears up and down that you absolutely *must* use their router.

## Set up IGMP snooping on your router

In order for your Fioptics TV to work, you need to enable IGMP snooping and tell it what port your set-top box (STB) is connected to. These steps might be a little specific to my ASUS router but I suspect you will find similar settings in other routers.

1. On your router, enable IGMP Snooping and IGMP Proxying. On the ASUS RT-AC86U, this is on the *LAN* > *IPTV* page. 
	1. Set *Enable multicast routing* to **Enable**.
	1. Set *Enable efficient multicast forwarding* to **Enable**.
1. On my ASUS router, I set the IPTV STB port to be the port my set top box is connected to (LAN1). On Fioptics, this may be the wireless bridge that connects to your STB (more on that piece of garbage later).
1. Apply the settings and your TV should be working. You may [view this screenshot of my settings for reference]({filename}/images/RT-N66U-IPTV-Settings.png "ASUS RT-AC86U IPTV Settings for Fioptics").

## Testing

That should be all you need to get your Fioptics Internet service to work with your own router. Test everything and then box that piece of crap up! I'm sure they'll want it back if you ever terminate service. I've heard that you can convince them to take the equipment back and avoid the modem fee, but it seems like some persistence is required.

# Troubleshooting poor wireless performance on Fioptics

Shortly after getting my personal router hooked up and ready. I noticed that our 2.4GHz wireless performance was awful in the evening. Keeping an eye on the pattern, it seemed like watching TV was correlated with problems. The wireless ZyXEL bridge devices our Fioptics installer used to connect our set top box were causing interference. These things use 802.11n on the 2.4GHz band and can cause huge packet loss and latency on your wireless network.

It doesn't seem like the ZyXEL bridge devices are configurable. If they were, I would have given them one channel and set my router to use a separate channel. My solution ended up being to use a [Ethernet over Powerline Adapter](https://amzn.to/2Snrr7p) to get wired connectivity from my router to the set-top box and remove the ZyXEL bridges from the environment. So far this is working very well and I'm actually seeing a lot less signal interruption on the TV set than I used to. These two devices got added to the box of Cincinnati Bell crap I will never use.