title: Hardening Firefox to Protect Privacy
date: 2015-08-11 17:40:39 -0400
tags: firefox, privacy, security
summary: Your web browser is your gateway to the Internet. Unfortunately, sometimes the gate works both ways. In this guide I will cover some tricks to help protect yourself online. I have been using Firefox configured like this for quite a while and wanted to share this with you. I'll admit this configuration could probably go further (eg. disabling JavaScript, employing NoScript, disabling remote fonts, etc.) but I feel like this setup provides a good balance between protecting privacy/security and keeping the browser usable.

Your web browser is your gateway to the Internet. Unfortunately, sometimes the gate works both ways. In this guide I will cover some tricks to help protect yourself online. I have been using Firefox configured like this for quite a while and wanted to share this with you. I'll admit this configuration could probably go further (eg. disabling JavaScript, employing NoScript, disabling remote fonts, etc.) but I feel like this setup provides a good balance between protecting privacy/security and keeping the browser usable.

# Disable Third-Party Cookies

Normally, a cookie's domain name will match the domain name that is shown in the web browser's address bar. This is called a **first-party cookie**. **Third-party cookies**, however, belong to domains *different* from the one shown in the address bar. These sorts of cookies typically appear when web pages feature content, such as banner advertisements, from external websites. This opens up the potential for tracking the user's browsing history, and is often used by advertisers in an effort to serve relevant advertisements to each user. You can [read more about cookies on Wikipedia](https://en.wikipedia.org/wiki/HTTP_cookie). 


Third-party cookie settings are available in the Options window's Privacy panel: 

1. Click the menu button and choose **Options**.
2. Select the Privacy panel.
3. Set **Firefox will:** to **Use custom settings for history**.
4. Set **Accept third-party cookies** to **Never**.
5. Close the *about:preferences* page. Any changes you've made will automatically be saved.

You can [read more about disabling third-party cookies at the Firefox Help website](https://support.mozilla.org/en-US/kb/disable-third-party-cookies).

![Disable Third-Party Cookies]({filename}/images/Disable%20Third-party%20Cookies.gif)

# Enable Tracking Protection

Firefox has a built-in tracking protection feature which actively blocks domains which are known to track users. You can read more about Tracking Protection at the [Firefox Help website](https://support.mozilla.org/en-US/kb/tracking-protection-firefox).

How to turn on Tracking Protection:

1. In the Location bar, type **about:config** and press Enter.
2. The about:config *"This might void your warranty!"* warning page may appear. Click **I'll be careful, I promise!** to continue to the about:config page. 
3. Search for **privacy.trackingprotection.enabled**.
4. Double-click **privacy.trackingprotection.enabled** to toggle its value to *true*.

![Enable Tracking Protection]({filename}/images/Enable%20Tracking%20Protection.gif)

## Troubleshooting Tracking Protection

Sometimes Tracking Protection can cause issues with websites. Personally I've seen it interfere with third-party login systems and shopping carts. You may choose to disable Tracking Protection for a particular site by clicking on the shield icon and selecting "Disable protection for this site." Once Tracking Protection is disabled for a site, you will see a shield with a red strike-through. You may choose to re-enable Tracking Protection for the site by clicking the shield icon again and selecting "Enable protection". 

# Install uBlock Origin to Block Advertising

You may have heard of AdBlock or it's kin (AdBlock Edge and AdBlock Plus), but uBlock Origin is currently the best advertising blocker out there. It is designed with performance in mind so that blocking advertising does not make your web browser run slower. In fact, [on average uBlock actually makes your browser run better](https://github.com/gorhill/uBlock#performance)! You can [install uBlock Origin from the Firefox Add-ons website](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/).

## Enable Additional uBlock Filters

By default uBlock uses a fairly minimal filtering list which is focused on blocking advertisements. In the uBlock Origin settings you can enable some extra filters to resist tracking.

1. Click the uBlock Origin icon in Firefox window.
2. Click the uBlock Origin banner in the menu that appears.
3. Go to the **3rd-party filters** tab.
4. Enable (check) the additional filter lists, provided below.
5. Once you are done, click **Apply changes**.

![uBlock Origin Settings]({filename}/images/uBlock%20Origin%20Settings.gif)

### Ads

The filters listed here are primarily about blocking banners nagging you to disable your advertising blocker.

* Adblock Warning Removal List
* Anti-Adblock Killer

### Privacy

These filters help you to evade tracking across websites.

* Basic tracking list by Disconnect
* Fanboy's Enhanced Tracking List

### Social

The social filters listed below block social buttons and scripts which are frequently used to track you across websites.

* Anti-ThirdpartySocial
* Fanboy's Annoyance List
* Fanboy's Social Blocking List

## Troubleshooting uBlock Origin

Sometimes uBlock will break sites which depend heavily on third-party content. I've seen several "log on with Facebook" type services broken by uBlock. When you suspect uBlock may be causing issues you can click the uBlock icon and then click the blue power button to disable uBlock on the site you're visiting. A reload button will appear that allows you to quickly refresh the page with uBlock disabled.

# Install the HTTPS Everywhere Add-on

HTTPS Everywhere is an extension that encrypts your communications with many major websites, making your browsing more secure. Encryption prevents third-parties from listening to your web traffic. You can [install the HTTPS Everywhere extension from the Electronic Frontier Foundation's website](https://www.eff.org/https-everywhere). After installation you'll be prompted to restart Firefox.

When Firefox restarts, HTTPS Everywhere will ask you if you want to use the SSL Observatory. Personally, I respond *Yes* to this prompt as I don't mind helping the EFF to monitor SSL certificates used on the web. It's your choice.

# Enforce Click-to-Play and Disable Unnecessary Plug-ins

These days it seems like just about every software package out there tries to install a browser plug-in. From a security standpoint, browser plug-ins are the biggest window for malicious software to gain entry to your system. That is why it is a good idea to make sure that only pages which you explictly allow can run plug-ins. This is accomplished by telling Firefox to ask you before activating plug-ins.

In going through plug-ins, I usually set all of them to *Never Activate*, except the following:

* **Shockwave Flash**: Ask to Activate
* **OpenH264 Video Codec provided by Cisco**: Always Activate
* **Primetime Content Decryption Module provided by Adobe**: Always Activate

Whenever you visit a page which requires a plugin, Firefox will display a notification along the top prompting you to allow the plug-in to run. If you trust the site, and want to run plugins all the time, click *Allow...*. From there you can choose to allow the plug-in this one time or allow it always. In most cases I'd recommend allowing the plug-in only once, however for some sites I'll tell it to *Allow and remember* (such as YouTube).

![Disable Plugins]({filename}/images/Disable%20Plugins.gif)