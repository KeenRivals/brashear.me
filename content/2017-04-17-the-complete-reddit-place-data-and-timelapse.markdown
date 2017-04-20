---
layout: post
title: "The Complete Reddit Place Data and Timelapse"
date: 2017-04-17 15:45:27 -0500
comments: true
categories: reddit
---

After place ended I became fascinated with the time lapses. Unfortunately, every one I saw was incomplete. Most began some time after the start of /r/place, and had a resolution of several minutes or worse. Thanks to a lucky break I was able to construct a complete time lapse of /r/place with 1-second resolution.

I was browsing the [Hacker News thread](https://news.ycombinator.com/item?id=14109158) on /r/place and found [a comment which linked to the raw place data](https://news.ycombinator.com/item?id=14110015) which has since been removed. Nevertheless, I had a copy to work with, so I got started. The result is a glorious 60fps timelapse with 1-second resolution that's nearly 1.5 hours long. Be warned that it starts out VERY slowly. My guess is it's the admins testing stuff.

Here's the [9-minute time lapse on YouTube](https://youtu.be/BfF7gtPA5HY). The real action starts about [1:38](https://youtu.be/BfF7gtPA5HY?t=98) in.

<!-- more -->

# The Data

The data was in timestamp,username,x_coordinate,y_coordinate,color tuples. If I started from the earliest timestamp I could reconstruct /r/place one second at a time! Here is a [copy of the CSV file I used](
https://mega.nz/#!E0gQ2KiY!n6HnDfR8bpQz79fKv4GtTt06S4iLSBq7bDfeo-rxuUU
). I have scrubbed the usernames. Given that the original source data was deleted, I don't want to be the guy to release usernames if releasing them was unintentional in the first place.

The only problem with the data is the times are to the second. If users placed pixels within the same second, it's possible that the order is going to be wrong. This is probably why my [final frame](https://i.imgur.com/0NR4NRB.png) is slightly different from other published final frames.

Here's my script to generate frames from the pixel data:

{% codeblock lang:python render_place.py %}
#!/usr/bin/python

import csv
from PIL import Image, ImageDraw, ImageColor
from multiprocessing import Pool

def save_image(image,ts):
	image.save('frames/{0}.png'.format(ts))
	
# Hex color table
colors = ["#FFFFFF","#E4E4E4","#888888","#222222","#FFA7D1","#E50000","#E59500","#A06A42","#E5D900","#94E044","#02BE01","#00E5F0","#0083C7","#0000EA","#E04AFF","#820080"]

# Convert the colors to RGB tuples
for i in range(0,len(colors)):
	colors[i]=ImageColor.getrgb(colors[i])

with Pool(processes=32) as pool:
	with open ('sorted_pixels.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		ts = 1490918687000
		im = Image.new("RGB",(1001,1001),"white")
		pixels = im.load()
		for row in reader:
			rowTimestamp = int(row['ts'])
			for i in range(ts,rowTimestamp,1000):
				pool.apply(save_image, args=(im, i,)) 

			ts = rowTimestamp
			pixels[int(row['x_coordinate']),int(row['y_coordinate'])] = colors[int(row['color'])]
		pool.apply(save_image, args=(im,ts))
{% endcodeblock %}
			
# Making the Video
			
After many hours, 16,559,898 pixel changes were converted into 320,048 PNG frames totaling 129GB. These frames can be *losslessly* composed into a 60fps mp4 using FFmpeg:

    ffmpeg -f image2 -r 60 -pattern_type glob -i *".png" -qp 0 -vf crop=1000:1000:0:0 Place-Timelapse.mp4

The resulting video is about 1.5 hours long, but may be interesting for anyone looking to build their own time lapses since it has *every* frame. You can [download it here](
https://mega.nz/#!MxIAiByD!_FcePrDFno-Gl2CqUcLwxzzVfD3uQLwexkVRR1UULDY
). Be advised that many video players have trouble playing lossless x264 video (especially at 60fps). You can use Ffmpeg to extract the individual frames if you need to. You'll need at least 130gb free! Alternatively you could generate them from the raw data using my Python script. That took about 24hrs on my i3-6300.

	ffmpeg -i Place-Timelapse.mp4 frame_%10d.png

To make the version sped up 10x from that, I used:

	ffmpeg -f image2 -r 600 -pattern_type glob -i *".png" -qp 0 -vf crop=1000:1000:0:0,fps=60 Place-Timelapse10x.mp4

This is the one on YouTube, but you can download the lossless version too.

## A note on scaling

Since this is pixel art, you want to be picky about what filter to use when scaling. I recommend using no interpolation, or nearest neighbor. This preserves 
the hard edges in the art. In ffmpeg, use ``-sws_flags neighbor``. For example, to make the 2000x2000 version for YouTube I used ``-sws_flags neighbor -vf scale=iw*2:-1``.

# Archive.org

I notice the [data on Archive.org](https://archive.org/details/reddit-place-timelapse-daily-img-archive) is missing the first bits. I think a lot of folks built from that. Given that I have a more complete set of data I'm open to working with someone to preserve it, but I have no idea where to begin.