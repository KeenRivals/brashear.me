Title: Hide a Partition from Windows Using Linux
Date: 2017-10-26T08:10-04:00
Tags: Linux, Windows

I  use [CloneZilla](http://clonezilla.org/) to create Windows recovery images for users. The general idea is they boot the USB and with very few steps can restore their PC to a "factory" state. The drive consists of two partitions—the CloneZilla boot partition, and a data partition. I have had problems with users messing with the data on the drive, which makes it unbootable. On top of that, newer Windows 10 versions show both partitions on the removable media. This gives them two drives to mess up! 
Poking around, I found that there are some GPT attributes which can help me here. Using ``parted``, I set the hidden attribute. It seemed to have no effect. Some research suggested that my version of parted (on Ubuntu 16.04) may not be handling GPT attributes properly. The fix ended up being to use ``gdisk`` instead.

# Using gdisk

Assuming you already have partitions, you only need to use gdisk to set the attributes.

1. Open the disk with ``gdisk disk.img``
2. List partitions with ``p``
3. Enter expert mode with ``x``
4. Use ``a`` to set attributes.
5. Enter the partition number. gdisk will show what the current fields are and a list of known attributes.
6. Type ``62`` and hit enter to set the hidden attribute. Hit enter again if you’re done setting attributes.
7. Use ``w`` to write the partition table.

You’re done!
