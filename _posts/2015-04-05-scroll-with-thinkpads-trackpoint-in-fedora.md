---
layout: post
title: "Scroll with ThinkPad's trackpoint in Fedora"
excerpt: "Change the behavior of ThinkPad's middle touchpad button in Fedora to
facilitate scrolling."
tags: [Fedora, ThinkPad, T450, Linux, laptop, scroll, trackpoint]
---

I [installed a T450 touchpad in my
T440]({% post_url 2015-03-22-t450-touchpad-on-t440-upgrade %}), and it works
great in [Fedora with Kernel
4.0]({% post_url 2015-03-24-get-the-t450-touchpad-to-work-on-fedora %}).

However, [I
found](http://www.reddit.com/r/thinkpad/comments/3064vb/is_it_possible_to_scroll_using_only_the/)
that it is possible to change so holding down the middle touchpad button while
pushing the trackpoint facilitates scrolling. By default the middle touchpad
button behaves just as a regular mouse's scroll wheel button, which is not as
functional.

Achieving the former behavior on Fedora in X is [explained on
Thinkwiki](http://www.thinkwiki.org/wiki/How_to_configure_the_TrackPoint#xorg.conf.d).
Basically you only have to create the file
`/etc/X11/xorg.conf.d/20-thinkpad.conf` with the following content:

    Section "InputClass"
      Identifier	"Trackpoint Wheel Emulation"
      MatchProduct	"TPPS/2 IBM TrackPoint|DualPoint Stick|Synaptics Inc. Composite TouchPad / TrackPoint|ThinkPad USB Keyboard with TrackPoint|USB Trackpoint pointing device|Composite TouchPad / TrackPoint"
      MatchDevicePath	"/dev/input/event*"
      Option		"EmulateWheel"		"true"
      Option		"EmulateWheelButton"	"2"
      Option		"Emulate3Buttons"	"false"
      Option		"XAxisMapping"		"6 7"
      Option		"YAxisMapping"		"4 5"
    EndSection

What is especially great with this solution is that pasting from the [X window
selection clipboard](http://en.wikipedia.org/wiki/X_Window_selection) still
works by clicking the middle touchpad button; while holding it down instead
triggers the scrolling behavior.

The problem though is that resizing windows in Gnome Shell is, in one way, done
by holding down the super key, *the scroll button* and moving the cursor at the
same time. This is shown in the following picture:

<figure>
  <a href="/images/resize/resize-window.gif"><img alt="Resizing window in Gnome Shell" src="/images/resize/resize-window.gif"></a>
</figure>

This obviously collides with the edited middle touchpad button behavior. I
explained on
[ask.fedoraproject.org](https://ask.fedoraproject.org/en/question/66163/resize-windows-with-super-right-click-instead-of-super-middle-click/)
how one can change the resizing from using the middle mouse button to the right
mouse button instead, which then works great on a ThinkPad. To summarize the
steps you have to do:

1. Install Gnome Tweak Tool: `$ sudo dnf install gnome-tweak-tool`
2. Open Tweak Tool and go to the page *Windows*.
3. Toggle on *Resize with Secondary-click*.
