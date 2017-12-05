Title: Export-WindowsImage from ESD to WIM can't be mounted
Tags: windows, sysadmin

Today I was converting an ESD to WIM. When mounting the WIM with ``Mount-WindowsImage``, I got an error: *an attempt was made to load a program with an incorrect format*.

It seems like a simple Export-WindowsImage from ESD preserves the ESD format instead of actually converting it to WIM. I found that I can make it convert to WIM by specifying the ``CompressionType`` as maximum.
