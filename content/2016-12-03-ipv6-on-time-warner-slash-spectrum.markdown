title: IPv6 on Time Warner / Spectrum
date: 2016-12-03 02:51:27 -0500
modified: 2017-04-30T17:14-04:00
tags: networking, ipv6
summary:  I recently moved and had to give up my beloved Fioptics gigabit Internet service. They were great, but the only thing they are behind on is IPv6 deployment. In 2015 when I switched to Fioptics, I asked them about their IPv6 plan and got a vague answer along the lines of "we're working on it". Time Warner had working IPv6 for a long time. Now that I'm back on Time Warner, it's time to get some sweet sweet IPv6 again.

I recently moved and had to give up my beloved Fioptics gigabit Internet service. They were great, but the only thing they are behind on is IPv6 deployment. In 2015 when I switched to Fioptics, I asked them about their IPv6 plan and got a vague answer along the lines of "we're working on it". Time Warner had working IPv6 for a long time. Now that I'm back on Time Warner, it's time to get some sweet sweet IPv6 again.

<!-- more -->

# Background

If you don't know, [IPv6](https://en.wikipedia.org/wiki/IPv6) is the future of the Internet. Everyone is on [IPv4](https://en.wikipedia.org/wiki/IPv4) right now, but IPv4 has some [serious limitations](https://en.wikipedia.org/wiki/IPv4_address_exhaustion) that mean it's time to migrate. Internet Service Providers are dragging their asses big time. To Time Warner's credit, they've done a good job with their IPv6 rollout already.

If you get phone service through Time Warner, this might change what you need for this to work. Someone I knew purchased a modem and realised there was no way to connect their phone to it. TV service would probably be okay with a [cheap splitter](http://amzn.to/2gycLSh)—you may already have one!

# Choosing a Modem

To use IPv6 with Time Warner / Spectrum, you need a modem and a router that support IPv6. You can consult their approved list of modems and narrow it down from there. I've had good luck with the Arris/Motorola Surfboard line. I discovered back in the day that many of the router/modem combos Time Warner distributed don't support IPv6. I've tested the [Motorola SB6141](http://amzn.to/2gxZsRX) and the [ARRIS SURFboard SB6190](http://amzn.to/2gyb9YW) and have had good experiences with both of them. The best thing is that once you have your own modem, you'll save about $10/month in modem fees. Either modem will pay for itself in less than a year!

Don't be tempted to buy a modem/router combo. In general, they suck. On top of that, you have a lot more options when it comes to capabilities if you use a dumb modem and whatever router you like.

The SB6141 is a bit dated and only supports up to 100mbps. The SB6141 supports up to 1400mbps. The price difference is fairly small, so I'd suggest going for the [SB6190](http://amzn.to/2gyb9YW) to make sure you're ready if Time Warner ever gets around to deploying 300mbps Internet in your area.

# Choosing a Router

You need a wireless router that's IPv6 compatible. Most recent models by big brand are, but many have some limitations. The [Netgear Nighthawk routers](https://www.amazon.com/gp/search/ref=as_li_qf_sp_sr_il_tl?ie=UTF8&tag=brashearme-20&keywords=netgear nighthawk&index=aps&camp=1789&creative=9325&linkCode=xm2&linkId=4df7aa8f8e021216bcc5f1f2686b2db0) are fairly good, but don't give you much control over the IPv6 firewall (it's either on of off). I am very happy with my [ASUS RT-AC88U](http://amzn.to/2gXLxS3), which gives me more control than the Netgear device did. The [ASUS RT-N66U](http://amzn.to/1jadh79) is a cheaper option with IPv6 capabilities—you'll only lose out on some wireless speed.

# Installation

Installation of the modem and router is fairly easy. The only catch is that you need to call Time Warner support and tell them you're switching modems. They will activate your new modem over the phone. It takes about 5–10 minutes. Once that's done you can return your old modem. Once the modem is returned, you'll no longer be charged a modem fee!

On both the Netgear Nighthawk and the ASUS RT-AC88U, you need to explicitly enable IPv6—it's disabled by default. On the ASUS:

1. Go to the IPv6 page and change it from *Disabled* to *Native*
2. Enable DHCP-PD. 
3. The Auto Configuration Setting should be *Stateless*.

Similar steps should be followed on other devices. Once the setting is applied, you should see your devices start grabbing IPv6 addresses over the next few minutes!