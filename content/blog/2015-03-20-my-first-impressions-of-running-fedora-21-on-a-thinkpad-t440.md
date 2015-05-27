Title: My first impressions of running Fedora 21 on a ThinkPad T440
Summary: I have gotten myself a new laptop, a ThinkPad T440, on which I have given Fedora a spin.
Tags: Fedora, ThinkPad, T440, Linux, Gnome, laptop

After 3.5 years of using a Toshiba Satellite R830 for my laptop needs, I have
now gotten myself a new laptop: a Lenovo ThinkPad T440. One of the first things
I did was to install the Linux distribution Fedora 21 Workstation unto it,
replacing Windows 8 that it was delivered with. In this post I will share my
first impressions of the laptop, how Fedora works on it and what I customized
with regards to Gnome to feel at home.

## The laptop

The ThinkPad T440 belongs to the previous generation of the T series—T450 was
just released. I got myself a used one on Ebay that looks almost new. It cost
me $600 (including shipping and import charges to Sweden), so I am very pleased
with the purchase. The specifications of the laptop are as follow:

* 14" 1600x900 non-touch screen
* Intel i5-4300U CPU
* 8 GB RAM
* 160 GB SSD
* Backlit US ANSI keyboard
* Intel HD Graphics 4400
* Intel Dual Band Wireless AC 7260

## Why a ThinkPad T440

ThinkPad has good reputation among Linux users for working well with various
Linux distributions. Most notable is Red Hat, which is the world's largest
vendor in the Linux space, who [heavily depends on ThinkPad
laptops](http://arstechnica.com/civis/viewtopic.php?f=16&t=1223953) for their
employees. Therefore ThinkPad felt like a fairly safe option since I want as a
hassle-free Linux experience as possible.

When I did my laptop research, I found several things that were compelling with
the ThinkPads and the T440 model. To start with, many people seem to enjoy
ThinkPad's TrackPoint. The build quality of the laptops in the T series is also
often brought up as a selling point, along with the quality of the keyboards.
Upgrading and replacing parts feels encouraged with the T series laptops, as
opposed to other laptops such as Apple's where the opposite seems true.
Furthermore, since the T440 is a laptop for professional usage, it has
accessories such as a docking station that I would like to try out in the
future. Finally, I think ThinkPad has a better brand reputation and emits a
more professional feeling compared to something like a Toshiba or Acer laptop.

Why I opted for a previous generation and used ThinkPad was a matter of cost.
Brand new ThinkPads are very expensive, especially here in Sweden, and cost
they cost far more than I am willing to pay for a laptop.

## Installing Fedora

Replacing Windows with Fedora was quite a straightforward process. In Windows,
the only thing I did before wiping it was to update the BIOS. Then to enter the
BIOS settings, to update the boot sequence, I had to do that using Microsoft's
[new weird way of doing it](http://support.lenovo.com/en/documents/ht076906).
Other than that I did not interact with Windows.

For creating a bootable USB stick I would recommend the tool Disks
(`gnome-disks`), part of the package
[`gnome-disk-utility`](https://apps.fedoraproject.org/packages/gnome-disk-utility),
which comes pre-installed on Fedora, at least on the Gnome spin. On Ubuntu I
have in the past had good experience with the app [Startup Disk
Creator](https://apps.ubuntu.com/cat/applications/usb-creator-gtk/), which I
think comes pre-installed. However, I have no recommendations for how one would
create a bootable USB on Windows; a tool that I have used in the past is
[UNetbootin](http://unetbootin.sourceforge.net/), but it has been a little
hit-or-miss in my experience.

Installing Fedora is a very smooth process thanks to their [Anaconda
installer](https://en.wikipedia.org/wiki/Anaconda_(installer\)). It is even
able to automatically create a BTRFS partition scheme, which I very much
appreciate.

## How well Fedora works on the T440

After the installation and I had booted up Fedora from the SSD for the first
time, I noticed a couple of things that did not work as expected. The first
thing was the TrackPoint which did not work; strange since it worked in the
live USB environment of Fedora. The other thing that neither worked as expected
was the Wi-Fi, which was horrendously slow. However, both of these things were
easily solved by simply updating Fedora; I did that by disabling the Wi-Fi,
plugged in an Ethernet cable, enabled the Ethernet, updated the system by
running `sudo dnf upgrade` and finally I rebooted the computer.

As far as I can tell, everything on the laptop now work as expected. The
brightness buttons work out of the box. The Wi-Fi and TrackPoint work after an
update. Sleep mode works. The touchpad works. Audio works. However, since this
is only my first impressions, I have not had time to see how it works for
extended usage or what battery life I can get out of the machine. But so far it
feels solid.

## Initial configuration

I quite enjoy Gnome's default settings, which is one part of why I like Gnome.
However, there are a few things that I change. The first is to change the
keyboard layout from QWERTY to Colemak, which is possible to do in the Anaconda
installer. The next thing is to enable *natural scrolling* and *tap to click*
for the touchpad. Then I also add a keyboard shortcut (Ctrl+Alt+T) for starting
`gnome-terminal` and lower the delay for *repeat keys* in the keyboard
settings. Finally, using `gnome-tweak-tool`, under *Typing* I set *Ctrl key
position* to *Caps Lock as Ctrl*.

Then there are of course a lot of other things that I configure and install on
a fresh Linux installation, such as ownCloud, tmux, Vim and zsh. But that is
perhaps something I could write about another time.

## Conclusion

The ThinkPad T440 feels like a solid laptop and writing this blog post on it
has been pleasant. In my experience there are often a few things that do not
work on a fresh Linux install, such as the brightness keys. However, the T440
seems to be an exception to that rule and has so far (one day) worked very
well.

I am going to replace the touchpad though, to one of the same model found in
the new T450 with the physical mouse keys brought back. I am also thinking
about replacing the screen with one with full HD resolution.
