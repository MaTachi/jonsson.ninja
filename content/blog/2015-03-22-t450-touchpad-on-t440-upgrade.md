Title: T450 touchpad on T440 upgrade
Summary: Upgrade the touchpad on your ThinkPad T440 with a touchpad for T450.
Tags: Fedora, ThinkPad, T440, Linux, Gnome, laptop

The previous generation of ThinkPad, with models such as X240, T440 and T540,
introduced a new touchpad without any physical buttons, also known as a
[clickpad](http://www.freedesktop.org/wiki/Software/libinput/clickpad-softbuttons/).
By reading reviews and comments, it is clear that this change was by and large
met with dissatisfaction. The reason being that it was hard to use the
trackpoint without the physical buttons at the top of the touchpad.

I only used the clickpad on my T440 for a few days, but long enough to
understand why people were complaining. The first problem was the lack of
tactile feeling of where the left, middle and right buttons where, therefore I
often did a middle click when my intention was to do a left click. The second
problem was that I would often move the cursor slightly when pressing down the
clickpad. Thirdly, it was also quite hard to select text using the trackpoint
with the software buttons.

Luckily Lenovo realized their mistake and brought back the physical buttons to
the top of the touchpad in the latest iteration of the ThinkPads. Even better,
the touchpad for the T450 has the very same size as the one in T440, and I
believe the same is true for X250 and its predecessor X240. People soon found
out that it is fully compatible, and only requires you to order a touchpad and
replace your current one with it. I was compelled and wanted to do the same
upgrade on my T440.

As I wrote in my [previous
post]({filename}/blog/2015-03-20-my-first-impressions-of-running-fedora-21-on-a-thinkpad-t440.md)
about my T440 purchase, it feels like disassembling your T series ThinkPad is
encouraged, which certainly shows when performing this modification. Lenovo has
a great [hardware maintenance
manual](http://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/t440_hmm_en_sp40a26000_01.pdf)
that, among other things, exactly explains how to remove the keyboard and
system board, which is required to replace the touchpad. Note though that the
manual might not be 100% the same as the ones for T440s and T440p.

A T450 touchpad can be purchased from Ebay or Aliexpress. I got mine from
[Aliexpress](http://www.aliexpress.com/store/product/TOUCHPAD-FOR-THINKPAD-T440P-T440S-T440-T431S-T450P-T450S-W540-L440-L540-Touchpad-Clickpad-With-Left/737935_32286821621.html)
for about $75. I assume it will go down in price over time, so if you want one
but think it is too expensive you might want to wait.

To my help performing the touchpad change I had the Lenovo manual. But I also
found value in [this
thread](http://forum.notebookreview.com/threads/t450-t550-touchpad-on-t440-t540-mod.769254/),
especially the first post, even though it was a little hard to read. Even
better, there is a [guide with
pictures](http://www.51nb.com/viewnews-97681.html) illustrating each step to
replace the touchpad, however, it is in Chinese, but the pictures are still
great.

<figure>
  <a href="{filename}/images/touchpad/img1.jpg"><img src="/images/touchpad/img1.jpg"></a>
  <figcaption>My ThinkPad T440 with the back cover, SSD and internal battery removed.</figcaption>
</figure>

<figure>
  <a href="{filename}/images/touchpad/img2.jpg"><img src="/images/touchpad/img2.jpg"></a>
  <figcaption>Without the keyboard, after the touchpad change.</figcaption>
</figure>

All in all, I believe it took me about one to two hours to perform the whole
process. There are quite a few screws, cables and components that need to be
removed and unplugged, which did put some pressure and stress on my mind. I
would only recommend doing this if you are able to stay cool. It is not *hard*
to do it, but I became quite nervous towards the end that I might had screwed
something up and that it would not turn on again.

The new ThinkPads' touchpads do not work correctly on Linux just yet though.
[Work is being
done](http://who-t.blogspot.se/2015/01/lenovos-x1-carbon-3rd-touchpad-woes.html)
and fixes have been committed to the kernel. However, it will take some time
for them to trickle down to your distribution of choice. In the meantime, there
is a [quite easy
workaround](https://bugs.freedesktop.org/show_bug.cgi?id=88609#c10) that will
make the T450 touchpad buttons work on Linux, with the downside that gestures,
such as two-finger scroll, will not work. I am myself running Fedora 21 and it
works great with that workaround; touchpad scrolling is not super important for
me, since I usually scroll with the keyboard, so I can happily wait until the
patch eventually trickles down.

A last resource I want to mention is the [subreddit
thinkpad](http://www.reddit.com/r/thinkpad/). It is a great source of
information and news. It is also a great place to ask fellow ThinkPad geeks
question about anything that might pop up.

<figure>
  <a href="{filename}/images/touchpad/img3.jpg"><img src="/images/touchpad/img3.jpg"></a>
  <figcaption>Everything back in place with the new touchpad installed.</figcaption>
</figure>

