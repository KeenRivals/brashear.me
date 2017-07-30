Title: Adventures in XFS Defragmentation
Date: 2017-07-30T12:10-04:00
Tags: Linux

I've got a server at home I use to store personal media and stream it to my TV with Plex. I was having issues with lagging during streaming. After some inspection, it didn't seem to be a constraint on CPU resources causing the problem, but IO. After disabling other IO tasks on the server, performance didn't improve very much. I thought I might be having an upcoming disk failure, but the smart data on all of the drives was good and ``hdparm`` gave me about what I expected the raw read speed to be. On a whim, I checked the filesystem fragmentation with ``xfs_db`` and found it was 98% fragmented. Holy cow!

	~> sudo xfs_db -r /dev/mapper/vg1-raid
	xfs_db> frag
	actual 2645859, ideal 32191, fragmentation factor 98.78%
	Note, this number is largely meaningless.
	Files on this filesystem average 82.19 extents per file

I ran ``xfs_fsr`` based on recommendations I found online and waited.

	~> sudo xfs_fsr
	xfs_fsr -m /proc/mounts -t 7200 -f /var/tmp/.fsrlast_xfs ...
	/ start inode=0
	/usr start inode=0
	/tmp start inode=0
	/var start inode=0
	/raid start inode=0
	xfs_fsr startpass 0, endpass 0, time 7306 seconds

Roughly two hours later, fragmentation had only decreased slightly.

	~> sudo xfs_db -r /dev/mapper/vg1-raid
	xfs_db> frag
	actual 2343029, ideal 32191, fragmentation factor 98.63%
	Note, this number is largely meaningless.
	Files on this filesystem average 72.79 extents per file

Reading the [manpage for ``xfs_fsr``](http://man7.org/linux/man-pages/man8/xfs_fsr.8.html) I found that the default invocation defrags all xfs filesystems for a maximum of two hours. When you run it with a device, it will run ten passes by default. I next ran ``xfs_fsr /dev/mapper/vg1-raid`` and waited a *very* long time—roughly twelve hours. When ``xfs_fsr`` completed, the drive was down to 1.03% fragmentation. Sweet!

	~> sudo xfs_db -r /dev/mapper/vg1-raid
	xfs_db> frag
	actual 32526, ideal 32192, fragmentation factor 1.03%
	Note, this number is largely meaningless.
	Files on this filesystem average 1.01 extents per file

## Three Months Later

Three months later, the filesystem is quite fragmented again!

	~> sudo xfs_db -r /dev/mapper/vg1-raid
	xfs_db> frag
	actual 197628, ideal 26411, fragmentation factor 86.64%
	Note, this number is largely meaningless.
	Files on this filesystem average 7.48 extents per file


# But why was it so fragmented?

I've long heard praises of how great Linux filesystems (such as ext4 and xfs) are at avoiding fragmentation. I can't think of how this filesystem could have got so fragmented. If you have any hypotheses, I'd really appreciate an email!