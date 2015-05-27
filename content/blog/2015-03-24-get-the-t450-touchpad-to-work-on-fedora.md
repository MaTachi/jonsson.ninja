Title: Get the T450 touchpad to work on Fedora
Summary: Get the T450 touchpad working to 100% on Fedora with 3 easy steps.
Tags: Fedora, ThinkPad, T450, Linux, laptop

The other day I replaced the touchpad in my Lenovo ThinkPad T440 laptop with a
touchpad for T450, read more about it
[here]({filename}/blog/2015-03-22-t450-touchpad-on-t440-upgrade.md).

The T450 touchpad's buttons did not work as expected and required a
[workaround](https://bugs.freedesktop.org/show_bug.cgi?id=88609#c10) to
function. However, applying that workaround had the downside with multi-finger
gestures, such as two-finger scroll, not working.

Luckily this has been [fixed in Linux kernel
4.0.0-rc5](http://www.reddit.com/r/thinkpad/comments/301u4r/guide_patch_and_compile_linux_kernel_with_new/cpodf65),
which was just released. *rc* stands for release candidate, so it might not be
such a good idea to run it in a critical environment. With kernel 4.0 you do
not need any workaround anymore, and the touchpad and its buttons work just as
expected.

On
[apps.fedoraproject.org/packages/kernel](https://apps.fedoraproject.org/packages/kernel)
I saw that the latest rc was available in Rawhide, which is Fedora's rolling
testing version. Then I went over to
[ask.fedoraproject.org](https://ask.fedoraproject.org/en/question/65863/is-it-possible-to-install-the-kernel-in-rawhide-on-stable-fedora/)
and got to know that the kernel in Rawhide can be installed on regular stable
Fedora by performing these three steps:

    $ cd /etc/yum.repos.d
    $ sudo wget http://alt.fedoraproject.org/pub/alt/rawhide-kernel-nodebug/fedora-rawhide-kernel-nodebug.repo
    $ sudo dnf upgrade

This will add a repository containing the Rawhide kernel and then upgrade the
system. After a reboot it will be working. However, if you have applied any
workarounds, such as the GRUB parameters, you probably want to remove them.

The current latest kernel version in stable Fedora is 3.19.1, which suffers
from the touchpad problem. So I will continue to run Rawhide's kernel until 4.0
has gone stable and reached stable Fedora, then I will switch back. But this
works great in the meantime.
