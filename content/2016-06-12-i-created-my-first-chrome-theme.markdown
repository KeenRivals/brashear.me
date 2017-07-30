title: I created my first Chrome theme!
date: 2016-06-12 09:44:33 -0400
tags: chrome
summary: I recently switched to Chrome from Firefox. I really missed Firefox's awesome dark [Developer Edition Theme](https://wiki.mozilla.org/DevTools/Developer_Edition_Theme). The Chrome web store was lacking an equivalent, so I made one! You can find it on the Chrome Web Store under the name, [Developer Edition Dark](https://chrome.google.com/webstore/detail/developer-edition-dark/lglfmldlfmbbehalkgiglehhjblbfcjo). It's [open source on GitHub](https://github.com/KeenRivals/chrome-developer-edition-dark) too! 

I recently switched to Chrome from Firefox. I'm not sure how long I'll stay but I really missed Firefox's awesome dark [Developer Edition Theme](https://wiki.mozilla.org/DevTools/Developer_Edition_Theme). The Chrome web store was lacking an equivalent, so I made one! You can find it on the Chrome Web Store under the name, [Developer Edition Dark](https://chrome.google.com/webstore/detail/developer-edition-dark/lglfmldlfmbbehalkgiglehhjblbfcjo). It's [open source on GitHub](https://github.com/KeenRivals/chrome-developer-edition-dark) too!

In the rest of this post, I'll provide some notes on Chrome theme creation. Documentation online was quite sparse, so if this helps someone else I'll be happy.

# Chrome Theme Documentation

You'll want to start by reading [Chrome's theme documentation](https://developer.chrome.com/extensions/themes). It's pretty sparse, but it provides a good template for building your own theme. When I was creating my theme, I was surprised to learn there is no way to specify a flat color to use for certain parts of the UI, such as the tabs, tab frame, and toolbar! If you're spending a lot of time Googling that, it's time to give up. You'll have to use an image.

Next, look over this [Google Chrome Theme Tutorial](https://sites.google.com/site/gsugsa/google-apps/google-chrome/how-to-create-a-theme), which goes into more detail about what bits of JSON do what in the Chrome UI. You can use the tool linked on that page to create a basic theme and tweak from there. I'd even encourage you to look at [my theme's source](https://github.com/KeenRivals/chrome-developer-edition-dark) if it helps at all. I didn't mess with any of the new tab page stuff, so my theme should serve as a simple example to learn from.

