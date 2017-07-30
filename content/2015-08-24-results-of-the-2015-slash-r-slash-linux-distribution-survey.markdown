title: Results of the 2015 /r/Linux Distribution Survey
date: 2015-08-24 19:43:06 -0400
tags: data, linux, distribution, survey
summary: About three years ago after seeing a failed comment survey on /r/Linux I decided to create a "real" survey using Google docs to find out what Linux Distributions the folks at /r/Linux were using. These past three years, the results of those surveys were very well received so I wanted to continue the tradition. You can still view the [2012 survey](http://constantmayhem.com/ty-stuff/linuxsurvey/report.html), the [2013 survey](http://constantmayhem.com/ty-stuff/linuxsurvey/2013.html), and the [2014 survey](https://brashear.me/blog/2014/05/18/results-of-the-2014-slash-r-slash-linux-distribution-survey/).
slug: results-of-the-2015-slash-r-slash-linux-distribution-survey

# Introduction

About three years ago after seeing a failed comment survey on /r/Linux I decided to create a "real" survey using Google docs to find out what Linux Distributions the folks at /r/Linux were using. These past three years, the results of those surveys were very well received so I wanted to continue the tradition. You can still view the [2012 survey](http://constantmayhem.com/ty-stuff/linuxsurvey/report.html), the [2013 survey](http://constantmayhem.com/ty-stuff/linuxsurvey/2013.html), and the [2014 survey](https://brashear.me/blog/2014/05/18/results-of-the-2014-slash-r-slash-linux-distribution-survey/).

As always, I'd like to prefix this by saying I’m no statistician. My stats knowledge is limited to a college class I took four years ago and can barely remember. If you feel like I’m representing anything incorrectly or have any kind of constructive feedback I’d appreciate a [reddit PM](http://www.reddit.com/message/compose/?to=TyIzaeL) about it or a comment on this page's reddit thread.

<!-- more -->

I'd like to apologize for the absolutely insane delay between making this survey and delivering the results. There's no good excuse. I've mismanaged my time and allocated too much to video games (League of Legends) and books (The Horus Heresy) and not enough to getting these results in order. My work ethic here has been quite poor and I'm sorry.

## Methods

Before we get down to business, I’d like to make the usual disclaimer about online polls (courtesy of Slashdot):

<blockquote>This whole thing is wildly inaccurate. Rounding errors, ballot stuffers, dynamic IPs, firewalls. If you’re using these numbers to do anything important, you’re insane.</blockquote>

The survey was active from 2015-04-29 00:50:50 UTC to 2015-05-10 15:10:29 UTC. During that time, a total of 3,196 responses were collected. This is a significant decrease from 2014 (10,292 total), 2013 (7,698 total), and 2012 (4,932 total). The only possible explanation I can come up with is that this year's survey thread was upvoted significantly less compared to previous years. Compare 162 points for 2015 versus 614 for 2014, 574 for 2013, and 353 for 2012. Fewer upvotes means fewer people saw it on their front page and fewer people took the survey. My suspicion is that since this year's survey thread was stickied very soon after creation, fewer people vote on stickies and hence it got fewer votes all together. That's just pure speculation on my part―maybe you guys are just tired of these! Unfortunately, you could argue that the results are biased towards users who actively browse /r/Linux (and would see the sticky) instead of all /r/Linux subscribers. Again, this is speculation on my part.

In the questions where manual entry was allowed, I had to do a lot of cleanup to merge similar entries. I couldn’t come up with an automated way to do this (and it really doesn’t take that long by hand). Sorry if there are any errors in the category names!

The results were dumped into a spreadsheet and processed with Excel (sorry guys) and Notepad++. This year, charts are done with gnuplot. I decided against PyGal this year because I disliked the JS requirement and it was a giant pain to stroke properly to get working. One of these days I'll ~~go insane~~ grow up and render the graphs with R. Graphs are embedded into this page as SVG. If you're not using an SVG-capable user-agent by now I'm sorry but you need to get with the times!

As always, you can [download the complete set of data for this survey if you like]({attach}/files/2015 rLinux Distro Survey Results.7z).

# Results

The results are broken up by question. Many questions are broken up into the "Top X" responses plus an "other" category. The "other" category includes all responses that didn't make the chart. If you're interested in seeing the omitted results I recommend downloading my raw data.

## Do you run Linux on any non-server computers?

As per-usual, we see that the *vast* majority of /r/Linux is running Linux on non-server computers (henceforth referred to as desktops). We see 97% is using Linux on Desktops and 3% is not. This is pretty much spot-on with last year's result of 96% vs 4%.

![Graph - Do you run Linux on any non-server computers?]({filename}/images/DistroSurvey2015/01%20-%20Do%20you%20run%20Linux%20on%20any%20non-server%20computers.svg)

## Do you use Linux on a server computer?

In some questions, I try to use this to gauge if users of servers have different preferences compared to people who do not use servers. Funny enough, this breakdown is the exact proportion as it was last year!

![Graph - Do you use Linux on a server computer?]({filename}/images/DistroSurvey2015/07%20-%20Do%20you%20use%20Linux%20on%20a%20server%20computer.svg)

| Do you use Linux on a server computer? | # of Responses | % of Responses |
| -------------------------------------- | -------------- | -------------- |
| Yes | 1854 | 58% |
| No | 1342 | 42% |

## Do you run Linux for fun or profit?

In this category, we combine the results of desktop & server usage and compare whether they are used for fun or profit.

![Graph - Do you use Linux for fun or profit?]({filename}/images/DistroSurvey2015/02.1%20-%20Do%20you%20run%20Linux%20for%20fun%20or%20profit.svg)

| Do you run Linux for fun or profit? | Desktop Linux | Server Linux |
| ----------------------------------- | ------------- | ------------ |
| Both | 1497 | 935 |
| Fun | 1544 | 653 |
| Profit | 37 | 252 |

## Desktop Linux Questions

Questions in this section were only displayed to users who indicated they used Linux on desktop computers. 

### Do you run desktop Linux for fun or profit?

It's a close call, it seems that half of /r/Linux users are running desktop Linux for fun (50%) while 49% use it for fun and profit. Only about 1% of respondents use desktop Linux purely for profit.

![Graph - Do you run desktop Linux for fun or profit?]({filename}/images/DistroSurvey2015/02%20-%20Do%20you%20run%20desktop%20Linux%20for%20fun%20or%20profit.svg)

### Which Linux distribution do you primarily use on your desktop computers?

Arch Linux remains king of /r/Linux for another year. In fact, this year the margin of Arch Linux's dominance increased by about 4%!

![Graph - Which Linux distribution do you primarily use on your desktop computers?]({filename}/images/DistroSurvey2015/03%20-%20Which%20Linux%20distribution%20do%20you%20primarily%20use%20on%20your%20desktop%20computers.svg)

| Linux Distribution | Number of Responses | Percentage | Previous Year Percentage |
| ------------------ | ------------------- | ---------- | ------------------------ |
| Arch Linux| 881| 28.47%| 24.01%|
| Ubuntu| 697| 22.53%| 21.01%|
| Debian| 308| 9.95%| 9.60%|
| Fedora| 262| 8.47%| 7.07%|
| Linux Mint| 209| 6.76%| 8.77%|
| Xubuntu| 117| 3.78%| 3.87%|
| Kubuntu| 99| 3.20%| 2.11%|
| Gentoo| 97| 3.14%| 2.28%|
| OpenSUSE| 58| 1.87%| 2.27%|
| Other| 366| 11.83%| 9.74%|

#### Comparison vs Server Usage

Here, we compare the desktop distribution preferences of folks who also use Linux on servers versus those who do not use server Linux. Interestingly, it seems like Arch Linux is losing its server-user bias and moving a bit more towards the average. Last year it had a 7% bias towards server users, but this year that bias has shrunk to about 2%.

![Graph - Which Linux distribution do you primarily use on your desktop computers? (Server Usage Comparison)]({filename}/images/DistroSurvey2015/03.1%20-%20Server%20Usage%20Comparison.svg)

| Linux Distribution | Non-server Users | Server Users |
| ------------------ | ---------------- | ------------ |
| Arch Linux | 40% | 60% |
| Ubuntu | 35% | 65% |
| Debian | 35% | 65% |
| Fedora | 39% | 61% |
| Linux Mint | 62% | 38% |
| Xubuntu | 59% | 41% |
| Kubuntu | 47% | 53% |
| Gentoo | 31% | 69% |
| OpenSUSE | 66% | 34% |
| Other | 52% | 48% |
| Average | 42% | 58% |

From these results, we can see that people who also use Linux on servers tend to prefer the following desktop distros:

 * Gentoo
 * Ubuntu
 * Debian

People who do not use Linux on servers tend to prefer the following desktop distros:

 * OpenSUSE
 * Linux Mint
 * Xubuntu
 * Other
 * Kubuntu

These distros did not exhibit a strong preference:

 * Arch Linux
 * Fedora

### Which other Linux distributions do you use on your desktop computers?

In this question, users were asked to check boxes for each *other* distributions they used on their desktop computers. In general, it's a nice look at what distributions /r/Linux users are interested in as non-primary distros.

![Graph - Which other Linux distributions do you use on your desktop computers?]({filename}/images/DistroSurvey2015/04%20-%20Which%20other%20Linux%20distributions%20do%20you%20use%20on%20your%20desktop%20computers.svg)

| Distribution | Number of Responses |
| ------------ | ------------------- |
| Debian | 560 |
| Ubuntu | 546 |
| Fedora | 469 |
| Arch Linux | 390 |
| Kubuntu | 330 |
| Linux Mint | 234 |
| CentOS | 190 |
| Xubuntu | 184 |
| OpenSUSE | 122 |
| Kali | 120 |
| Other | 933 |

### What hardware platform do you primarily run your primary desktop distributon on?

In this question we ask what platforms folks are using for their desktop distros.

![Graph - What hardware platform do you primarily run your primary desktop distributon on?]({filename}/images/DistroSurvey2015/05%20-%20What%20hardware%20platform%20do%20you%20primarily%20run%20your%20primary%20desktop%20distributon%20on.svg)

| Distributon | # of Responses | % of Responses |
| ----------- | -------------- | -------------- |
| Laptop | 1622 | 53% |
| Desktop PC | 1114 | 36% |
| Workstation | 262 | 9% |
| Virtual Machine | 64 | 2% |
| RaspPi/similar | 11 | 0% |
| Other | 8 | 0% |


### What other hardware platforms do you run desktop Linux on?

This question asks for what *other* platforms folks are running desktop Linux on. From this question and the previous, we can see that Linux as "desktop" Linux is running on a surprisingly high number of laptops!

![Graph - What other hardware platforms do you run desktop Linux on?]({filename}/images/DistroSurvey2015/06%20-%20What%20other%20hardware%20platforms%20do%20you%20run%20desktop%20Linux%20on.svg)

| Platform | Number of Responses |
| -------- | ------------------- |
| Virtual Machine | 1197 |
| Laptop | 1119 |
| Raspberry Pi (or similar) | 830 |
| Desktop PC | 749 |
| Workstation | 346 |
| Rack Server | 330 |
| Tablet | 185 |
| Embedded | 181 |
| Other | 69 |

## Server Linux Questions

The questions in this section were only displayed to users who indicated they used Linux on a server computer.

### Which Linux distribution do you primarily use on your server computers?

This year, we see Ubuntu has dethroned Debian as the server distro of choice for /r/Linux. 

![Graph - Which Linux distribution do you primarily use on your server computers?]({filename}/images/DistroSurvey2015/08%20-%20Which%20Linux%20distribution%20do%20you%20primarily%20use%20on%20your%20server%20computers.svg)

| Linux Distribution | Number of Responses | Response Percentage | Previous Year Percentage |
| ------------------ | ------------------- | ------------------- | ------------------------ |
| Ubuntu | 633 | 34% | 27% |
| Debian | 539 | 29% | 31% |
| CentOS | 214 | 12% | 15% |
| Arch Linux | 183 | 10% | 9% |
| Red Hat Enterprise Linux | 83 | 5% | 4% |
| Gentoo | 51 | 3% | 2% |
| Fedora | 34 | 2% | 2% |
| Slackware | 22 | 1% | 1%  |
| OpenSUSE | 12 | 1% | 1% |
| Scientific Linux | 10 | 1% | 1% |
| Other | 62 | 3% | 6% |

Digging into the percentages, we can see that the biggest movers here are Ubuntu and Debian. The other distributions have remained (comparatively) stable.

### What other Linux distributions do you use on your server computers?

![Graph - What other Linux distributions do you use on your server computers.svg]({filename}/images/DistroSurvey2015/09%20-%20What%20other%20Linux%20distributions%20do%20you%20use%20on%20your%20server%20computers.svg)

| Linux Distro | Percentage of Responses | Previous Year Percentage |
|--------------|-------------------------|--------------------------|
| Debian       | 22%                     | 22%                      |
| Ubuntu       | 20%                     | 21%                      |
| CentOS       | 19%                     | 20%                      |
| Arch Linux   | 10%                     | 8%                       |
| Other        | 10%                     | 3%                       |
| RHEL         | 7%                      | 8%                       |
| Fedora       | 6%                      | 4%                       |
| Gentoo       | 3%                      | 2%                       |
| OpenSUSE     | 2%                      | 2%                       |
| Amazon Linux | 2%                      | 2%                       |
| Other        | 8%                      | 11%                      |

### What hardware platform do you primarily run your primary server distributon on?

![Graph - What hardware platform do you primarily run your primary server distributon on?]({filename}/images/DistroSurvey2015/10%20-%20What%20hardware%20platform%20do%20you%20primarily%20run%20your%20primary%20server%20distributon%20on.svg)

### What is your favorite Linux graphical environment?

GNOME continues to be the favorite GUI of /r/Linux! This year it pulls significantly further ahead of the competition.

![Graph - What is your favorite Linux graphical environment?]({filename}/images/DistroSurvey2015/11%20-%20What%20is%20your%20favorite%20Linux%20graphical%20environment.svg)

| What is your favorite Linux graphical environment? | Number of Responses |
|----------------------------------------------------|---------------------|
| GNOME                                              | 681                 |
| Unity                                              | 474                 |
| KDE                                                | 460                 |
| XFCE                                               | 352                 |
| i3                                                 | 312                 |
| Cinnamon                                           | 244                 |
| MATE                                               | 115                 |
| Openbox                                            | 114                 |
| Awesome                                            | 104                 |
| Other                                              | 295                 |

### What is your most hated Linux graphical environment?

Not surprisingly, Unity continues to be /r/Linux's most hated GUI. This is a little funny, considering that it's the second favorite GUI. It really is a love or hate it sort of thing. :)

![Graph - What is your most hated Linux graphical environment?]({filename}/images/DistroSurvey2015/12%20-%20What%20is%20your%20most%20hated%20Linux%20graphical%20environment.svg)

### Controlling GUI Hate Vs Love

I was thinking, and it seems like popular GUIs are more likely to have higher numbers of users loving/hating them. In the chart below, we see a calculation which subtracts the number of users who hate a particular GUI from the number of users who love it. Higher numbers mean more people love it, lower (negative) numbers mean people hate it.

Here we see that XFCE is well loved, Unity is *very* well hated, and people seem neutral towards LXDE, Compiz, and GNOME.

![Hate Index]({filename}/images/DistroSurvey2015/13%20-%20Hate%20Index.svg)

## Demographic Questions

These are some questions I added just for fun to get a feel for the /r/linux community.

### What is your age?

It doesn't seem like we fall outside the standard reddit distribution here.

![Graph - What is your age?]({filename}/images/DistroSurvey2015/14%20-%20What%20is%20your%20age.svg)

### What operating system does your mobile phone run?

/r/Linux so overwhelmingly uses Android that other OSes barely register!

![What operating system does your mobile phone run?]({filename}/images/DistroSurvey2015/15%20-%20What%20operating%20system%20does%20your%20mobile%20phone%20run.svg)

### Which CPU vendor do you prefer for Linux?

A big win for Intel among /r/Linux users. I don't think this is surprising considering the quality of Intel drivers on Linux, though I know there are many other factors at play (such Intel's performance reign, as well as Intel's dominance in the server market).

![Graph - Which CPU vendor do you prefer for Linux?]({filename}/images/DistroSurvey2015/16%20-%20Which%20CPU%20vendor%20do%20you%20prefer%20for%20Linux.svg)

### Which GPU vendor do you prefer for Linux?
Poor AMD... I was not expecting such a showing from NVIDIA here. I personally though Intel would edge out due to superior Linux support. I suppose NVIDIA is where it's at if you want some modicum of video performance out of your rig.

![Graph - Which GPU vendor do you prefer for Linux?]({filename}/images/DistroSurvey2015/17%20-%20Which%20GPU%20vendor%20do%20you%20prefer%20for%20Linux.svg)

# Closing Statements

Another year, another survey. /r/Linux remains a very diverse Linux community—covering everyone from newbs to greybeards. I appreciate you guys' patience in waiting for me to get these results together, and I hope I haven’t fallen short this year. Feel free to [PM me on reddit](http://www.reddit.com/message/compose/?to=TyIzaeL) if you have any questions or suggestions. I’d be especially interested to hear of better ways to represent this data as well as ideas for questions in future polls.

# License

<p xmlns:dct="http://purl.org/dc/terms/" xmlns:vcard="http://www.w3.org/2001/vcard-rdf/3.0#"><a rel="license" href="http://creativecommons.org/publicdomain/zero/1.0/"><img src="https://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0"></a><br />To the extent possible under law, <a rel="dct:publisher" href="https://brashear.me">https://brashear.me</a> has waived all copyright and related or neighboring rights to <span property="dct:title">2015 /r/Linux Distro Survey Results</span>. This work is published from: <span property="vcard:Country" datatype="dct:ISO3166" content="US" about="https://brashear.me"> United States</span>.</p>
