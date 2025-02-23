---
title: Sharing web apps in a chat 
author: holga, rosano, r10s
image: ../assets/logos/webxdc.png
com_id: 108487984933980780
---

<img src="../assets/logos/webxdc2.png" style="width:160px; float:right; clear:both; margin-left:.5em; margin-bottom:.2em;" alt="Webxdc Logo" />
Delta Chat 1.30 introduces support for [webxdc apps](https://webxdc.org): which makes it possible to share HTML5 apps (packaged as <code>.xdc</code> files) inside your chats, so that any participant can run the app by clicking "Start" in the message.  It transforms Delta Chat into an *extensible* messenging app where third parties can easily program custom interactive chat extensions, called "webxdc apps".

## Sharing webxdc apps is safe and easy 

**Webxdc apps run in a sandboxed browser on your device,** which restricts interaction with external servers or entities outside the chat; this is why <code>.xdc</code> files need to be self-contained zip-files with all necessary resources.

Once running, webxdc apps can **send and receive data with any chat participant** who also runs the apps; the Delta Chat app takes care of routing updates to the right place.

All webxdc apps get end-to-end encryption for free, and user data cannot be accessed by Delta Chat or webxdc app developers. No privacy policy or consent is needed for webxdc apps because all data is stored on-device or between invited chat participants.

## Writing your own webxdc apps with HTML5

<video controls style="width:560px; max-width: 100%;"><source src="https://webxdc.org/assets/just-web-apps.mp4" type="video/mp4"><a href="https://www.youtube.com/watch?v=I1K4pBvb2pI">watch "just web apps" on youtube</a></video>

**Webxdc apps are simpler to develop and deploy than traditional web apps:** you can get started with a simple understanding of HTML, CSS, and JavaScript, without implementing logins, user discovery, or a platform, let alone the legal and operational issues that come with that. 

Just package your web app as an <code>.xdc</code> file (a zip archive, renamed), and then drop it in a chat, or offer it for download on a web page so others can share it in their chats. There are many examples from simple to complex on [webxdc.org](https://webxdc.org).

## Where do we go from here? 

**Webxdc is based on [specifications](https://docs.webxdc.org/spec.html) and is not exclusive to Delta Chat.** We would love to see other messaging projects support webxdc apps. There is nothing in webxdc apps that fundamentally ties it to Delta Chat. Then again, it is maybe not a co-incidence that the webxdc "web over chat" idea grew and evolved in Delta's "chat over e-mail" development communities. After all, webxdc and Delta Chat apps share a unique characteristic: app developers or distributors get no access to user data whatsoever, not even in encrypted form. The best data is no data :) 
