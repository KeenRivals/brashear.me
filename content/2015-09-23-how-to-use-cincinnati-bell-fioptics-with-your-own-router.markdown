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

# General Guide

## Set up IGMP snooping on your router

For Fioptics TV to work, you need to enable IGMP snooping and tell it what port your set-top box (STB) is connected to. If you don't need TV you're all set. These steps are specific to the ASUS router but I suspect you will find similar settings in other routers.

1. On your router, enable IGMP Snooping and IGMP Proxying. On the ASUS RT-AC86U, this is on the *LAN* > *IPTV* page. 
	1. Set *Enable multicast routing* to **Enable**.
	1. Set *Enable efficient multicast forwarding* to **Enable**.
1. Set the IPTV STB port to the port the set top box is connected to (LAN1). On Fioptics, this may be the wireless bridge that connects to your STB.
1. Apply the settings and your TV should be working. You may [view this screenshot of my settings for reference]({static}/images/RT-N66U-IPTV-Settings.png "ASUS RT-AC86U IPTV Settings for Fioptics").

## Testing

That should be all you need to get your Fioptics Internet service to work with your own router. Test everything and then box that piece of crap up! I'm sure they'll want it back if you ever terminate service. I've heard that you can convince them to take the equipment back and avoid the modem fee, but it seems like some persistence is required.

# Troubleshooting poor wireless performance on Fioptics

Shortly after getting my router hooked up  I noticed  our 2.4GHz wireless performance was awful in the evening. It seemed like watching TV was correlated with problems. The wireless ZyXEL bridge devices our Fioptics installer used to connect our set top box were causing interference. These things use 802.11n on the 2.4GHz band and can cause huge packet loss and latency on your wireless network.

It doesn't seem like the ZyXEL bridge devices are configurable. My solution ended up being to use a [Ethernet over Powerline Adapter](https://amzn.to/2Snrr7p) to get wired connectivity from my router to the set-top box and remove the ZyXEL bridges from the environment. This worked very well and I saw a lot less signal interruption on the TV set than I used to. These two ZyXEL devices got added to the box of Cincinnati Bell crap I will never use.