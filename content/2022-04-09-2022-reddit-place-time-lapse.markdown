Title: My 2022 Reddit Place Time Lapse
Date: 2022-04-10T09:08:35-04:00
Tags: reddit, ffmpeg, python

The 2022 Reddit Place event has ended. Again the devs were kind enough to [release the raw place data](https://www.reddit.com/r/place/comments/txvk2d/rplace_datasets_april_fools_2022/). Reddit already provided an official time lapse, but my goal was to create a higher quality time lapse where each frame of the 60fps video was one second of the event. You can view [the full-length 60x speed video](https://www.youtube.com/watch?v=_Gd51ei4_iw) or [the fast 600x version](https://www.youtube.com/watch?v=heXgxGs5YlE). These are rendered at 4000p at 60fps (you may or may not see them depending on if YouTube ever finishes processing them). Reddit's is 720p at 30fps. This one was fun and challenging due to the massive amount of data. In 2017 there were 16,559,897 pixel placements. This year there were 160,353,104. Almost ten times as many! You might also [check out the discussion on reddit](https://www.reddit.com/r/place/comments/u14ty9/my_2022_place_time_lapse_1second_resolution_8k/).

<!-- more -->

Starting out I downloaded the big fat 11.5gb compressed dataset and unpacked it to a 20gb csv file. I modified [my old script mentioned here](https://www.reddit.com/r/place/comments/65x14m/place_time_lapse_and_data_from_start_to_finish/) to process the new format in the data. Early on I found the data was not sorted by time and my renders were coming out weird. Sorting the data ended up being much more difficult than I thought it would be.

# Sorting the data

First off, the times were in a really weird format, like YYYY-mm-dd HH:MM:SS with milliseconds and time zone. Date parsing is not fun and the ``sort`` command didn't understand it. I started writing some python to sort it but I was running out of RAM for sorting! My system has 32gb of RAM and I saw my paging file get up over 90gb anyways. It was wild!

To reduce the memory footprint I stripped the user hash from the data. I figured in the same step it would be easy to convert the date to a Unix timestamp so I could sort more easily later.

	:::python strip.py

	#!/usr/bin/env python
	import csv
	from datetime import datetime
	from dateutil import parser
	import time 

	with open ('2022_place_canvas_history.csv') as csvfile:
		reader = csv.reader(csvfile)
		with open ("stripped.csv", 'w',newline='') as csvwriter:
			writer = csv.writer(csvwriter)
			
			# dump the header row and advance the pointer
			writer.writerow(next(reader))

			# Convert timestamp to epoch ms for ease-of-use later, drop the user hash (row[1])
			for row in reader:
				writer.writerow( [int( parser.parse(row[0]).timestamp() * 1000 ), row[2], row[3]] )

Just this step takes the size of the CSV file from 20gb to 5gb! I was still having problems sorting with python and it running out of memory. I was trying to be fancy and use a lambda function to do it. It seemed like it was going to work but after some hours I used ``sort -n -k1`` and was amazed at how quickly it did the job! 

# Rendering the frames

Now we have our pixel placements sorted, it's time to put them to the canvas. The idea with my script is to work through each second of frames, put pixels on the canvas, then save it and continue to the next second. I fork off the save with multiprocessing to get a nice speed boost at the expense of using much more RAM.

A new thing this year is censorship boxes placed by mods, but that was easy enough and didn't seem to be done frequently.

	:::python render-place.py
	#!/usr/bin/env python

	import csv
	from PIL import Image, ImageColor, ImageDraw
	from dateutil import parser
	from datetime import datetime
	from multiprocessing import Pool
	import time

	# Standalone function to dump the frame
	# Allows for multiprocessing to work its magic
	def save_image(image,ts):
		image.save('frames/{0}.png'.format(ts))

	if __name__ == '__main__':
	   
		with open ('sorted.csv') as csvfile:
			 # Too many processes or tasks per child and you'll exhaust your RAM quickly.
			 with Pool(processes=32,maxtasksperchild=64) as pool:
				reader = csv.reader(csvfile)
				# Timestamp just before the first pixel was placed.
				ts = 1648817049
				im = Image.new("RGB",(2000,2000),"white")
				next(reader) #Skip the first row.
				pixels = im.load()
				
				# For each row in the CSV
				for row in reader:
					rowTimestamp = int(int(row[0])/1000) # Current timestamp
					
					# Iterate from the previous known timestamp up to the current timestamp.
					# This makes some duplicate frames to fill gaps where there is no data.
					for i in range(ts,rowTimestamp,1):
						pool.apply_async(save_image, args=(im,i))
					
					# The current timestamp is now the known timestamp
					ts = rowTimestamp 
					
					# Split the coords field into an array.
					coords = row[2].split(",")
					
					# If the coords array has two entries, this is a pixel placement. Place a pixel.
					# Otherwise is a box drawn by a mod to censor something.
					if(len(coords) <= 2):
						pixels[int(coords[0]),int(coords[1])] = ImageColor.getrgb(row[1])
					else:
						ImageDraw.Draw(im).rectangle( xy= (int(coords[0]),int(coords[1]), (int(coords[2])+1),(int(coords[3])+1)), fill=ImageColor.getrgb(row[1] ) )
					
				pool.apply_async(save_image, args=(im,ts))

# Creating the videos

Once the frame rendering was complete I had over 300k png files totalling over 400gb. Merging these to video is no problem with ffmpeg! I used lossless x265 to get a decent file size even though it's slower than mp4.

	:::bash
	ffmpeg -r 60 -pattern_type glob -i 'frames/*.png' -c:v libx265 -an -x265-params lossless=1 -preset:v ultrafast -g 600 -y "2022 Place Timelapse.mkv"

Now I've got a 4.6gb video that's 1:23:29 long and 2000x2000 pixels. Since this is pixel art, I can upscale it using the nearest-neighbor scaling method and keep those crispy edges. With ffmpeg that's just ``-sws_flags neighbor -vf scale=iw*2:-1``. This 4000x4000 version is what made it to YouTube. Whether or not YouTube ever decides to offer the 4000p version is up to them!

To make the fast version of the upscale, just rencode with ``-vf setpts=PTS*.01``. Each step of the way I use -x265-params lossless=1 so no quality is ever lost.

# Closing

Overall this was a fun little python exercise for me. I'm not that great at it, so if I missed an obvious way to do this more easily I would love an email about it. My day-to-day is mostly sysadmin stuff with PowerShell but I always find python and ffmpeg to be pretty fun.
