title: Migration from Octopress to Pelican
date: 2017-07-30T11:01-04:00
tags: blog, webdev
summary:  Octopress has served me well so far. It was a good introduction to static blog generators when I started using it (early 2014). However, it's got enough cracks that I'm no longer interested in using it. As of this post I've migrated my blog to Pelican with my own custom theme which I'm calling pelican-feather.

Octopress has served me well so far. It was a good introduction to static blog generators when I started using it (early 2014). However, it's got enough cracks that I'm no longer interested in using it. As of this post I've migrated my blog to Pelican with my own custom theme which I'm calling pelican-feather.

# Why I like Pelican more than Octopress

There were a few reasons why I felt transitioning to pelican was a good idea. Most of my problems with Octopress were minor annoyances, which compounded to make using the software annoying. When writing posts, I want to write markdown and call it done. Octopress gets in the way too much for me to keep wanting to use it.

## Ruby is annoying

I'm far from an expert in either ruby or python, but the packaging infrastructure around python is much more workable for me than ruby. I was regularly having to fix my rbenv to be able to manage my blog with octopress. Problems ranged from rbenv disagreeing with fish-shell to broken gem dependencies requiring me to reinstall octopress. This made publishing annoying and discouraged me from doing it.

With pelican, I ``sudo pip install pelican`` and I'm on my way. It helps that the default install is less bloated than Octopress, so deeply customizing it is not a daunting task.

## Pelican Themes are easy to make and use

I'm a sysadmin, not a web developer. Though I can sling some HTML & CSS, it's not my specialty. Creating a custom theme that worked well and looked decent with Pelican was easy.

## Octopress feels like abandonware

Octopress 3.0 has been [on the way for more than two years](http://octopress.org/2015/01/15/octopress-3.0-is-coming/). On top of that, none of the stated goals of 3.0 resolve the aforementioned problems I have with it. At time of writing, the last commit on the [Octopress 3.0 repository](https://github.com/octopress/octopress) was over a year ago. I'm aware that [Jekyll](https://jekyllrb.com/) is still actively developed, but I want to leave the ruby ecosystem.