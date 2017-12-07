Title: How to Deploy Firefox with Bookmarks and Addons
Date: 2017-12-07T09:27-05:00
Tags: Firefox, Deployment, Sysadmin, Windows

Unlike Chrome, managing Firefox is a bit of a pain. However, I can't bring myself to pull it from our system images. I like Firefox! Documentation floating around the web is a mix of old, wrong, or doesn't fit my goals. I want to:

* Bundle company bookmarks
* Set some settings
* Bundle uBlock Origin by default.
* Allow users to override all settings.

The mozilla.cfg method tickles some of these requirements, but not all. Building an extension to apply settings is more work than it needs to be, and in a weird state since the WebExtension migration. I've found that using [distribution.ini](https://wiki.mozilla.org/Distribution_INI_File) I can deploy Firefox happily. I have published a [basic Firefox deployment example on GitHub](https://github.com/KeenRivals/Firefox-Deployment-Example/).

# Using Distribution.ini to deploy bookmarks and settings

Distribution.ini lives in ``<Firefox installation directory>\distribution\distribution.ini``. You can check out my [sample distribution.ini](https://github.com/KeenRivals/Firefox-Deployment-Example/blob/master/Mozilla%20Firefox/distribution/distribution.ini). When a new Firefox profile is created, the settings in distribution.ini are applied to it. This is almost perfect for my use case, since I generally deploy Firefox and don't touch it later.

# Bundling Extensions

Similar to distribution.ini, if you put extensions (in XPI form) into ``<Firefox installation directory>\distribution\extensions``, they will be installed on first-run. In my deployment example repository, uBlock Origin is deployed. Note that you have to rename the extension's xpi file to the extension's ID. You can find the extension ID by extracting the XPI (it's a zip file) and finding "id" in manifest.json. In the case of uBlock, the id is ``uBlock0@raymondhill.net``.