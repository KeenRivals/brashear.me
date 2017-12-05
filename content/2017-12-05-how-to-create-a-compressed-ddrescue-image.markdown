Title: How to create a Compressed DDRescue Image
Date: 2017-11-14T12:04-05:00
Tags: Linux, Data Recovery

As disk sizes explode, I've found myself having to mirror disks which I don't have enough storage for. My tool of choice is [ddrescue](https://www.gnu.org/software/ddrescue/ddrescue.html). However, it doesn't support compression because it needs to be able to seek through the output as it rescues data. A solution I've found is to create a sparse file, format it btrfs, and mount it with the ``compression=lzo`` option. This allows ddrescue to operate normally, while giving me fast + decent compression.

1. Create a sparse file which is larger than your source disk: ``dd if=/dev/zero bs=1 count=0 seek=4T of=image-repository.img``
2. Mount the file as a loop device: ``sudo losetup /dev/loop0 image-repository.img``
3. Partition the loop device: ``sudo gdisk /dev/loop0``
2. Create new GPT: ``o`` then ``y``
3. Create new partition, enter a few times to accept defaults: ``n`` 
4. Write the table, hit ``w`` then ``y``
4. Reread paritions from the loop device: ``sudo partprobe /dev/loop0``
5. Format the loop0p1 partition: ``sudo mkfs.btrfs /dev/loop0p1``
6. Mount the filesystem with compression enabled: ``sudo mount -o compress=lzo /dev/loop0p1 /mnt/img-repository``
7. Set the c attr on the mount directory: ``sudo chattr +c /mnt/img-repository``

Now, when you create a ddrescue image inside of /mnt/img-repository, it will be transparently compressed!
