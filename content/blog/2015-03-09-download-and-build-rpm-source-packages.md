Title: Download and build RPM source packages
Summary: Learn how to build, install and uninstall RPMs on Fedora.
Tags: RPM, SRPM, Linux, Fedora, Red Hat, CentOS
Date: 2015-03-09T17:30:00+01:00

In this post I will show you how to download a source RPM, build it, install it
and then finally uninstall it.

RPM is the package format that is being utilized on Linux distributions such as
Fedora, Red Hat and CentOS.

I am myself running Fedora 21, and this tutorial will therefore be given from
that perspective.

## Download a source RPM package

To download a source RPM (SRPM) package you first need to install the package
[`yum-utils`](http://linux.die.net/man/1/yum-utils) which contains the tool
`yumdownloader`. That is achieved by executing the following command:

    :::bash
    $ sudo yum install yum-utils

The source package we will download in this post is
[`verne-backgrounds`](https://apps.fedoraproject.org/packages/verne-backgrounds/overview/),
which contains the default wallpapers for Fedora 16. Do that with:

    :::bash
    $ yumdownloader --source verne-backgrounds

Which results in the following file being downloaded:

    :::bash
    $ ls
    verne-backgrounds-15.92.1-8.fc21.src.rpm

## Build the RPM package

To build RPM(s) from the SRPM we need the tool
[`rpm-build`](http://www.rpm.org/max-rpm-snapshot/rpmbuild.8.html). Install it
with:

    :::bash
    $ sudo yum install rpm-build

Then build the package:

    :::bash
    $ rpmbuild --rebuild verne-backgrounds-15.92.1-8.fc21.src.rpm

In this case, it results in nine RPMs being built, which can be found in the
directory `~/rpmbuild/RPMS/noarch`:

    :::bash
    $ cd ~/rpmbuild/RPMS/noarch
    $ ls
    verne-backgrounds-15.92.1-8.fc21.noarch.rpm
    verne-backgrounds-extras-gnome-15.92.1-8.fc21.noarch.rpm
    verne-backgrounds-extras-kde-15.92.1-8.fc21.noarch.rpm
    verne-backgrounds-extras-single-15.92.1-8.fc21.noarch.rpm
    verne-backgrounds-extras-xfce-15.92.1-8.fc21.noarch.rpm
    verne-backgrounds-gnome-15.92.1-8.fc21.noarch.rpm
    verne-backgrounds-kde-15.92.1-8.fc21.noarch.rpm
    verne-backgrounds-single-15.92.1-8.fc21.noarch.rpm
    verne-backgrounds-xfce-15.92.1-8.fc21.noarch.rpm

## Install the RPM(s)

Since I am running Gnome Shell, I will only install the RPMs
`verne-backgrounds-gnome` and `verne-backgrounds-single`:

{% highlight bash %}
$ sudo rpm -i verne-backgrounds-gnome-15.92.1-8.fc21.noarch.rpm verne-backgrounds-single-15.92.1-8.fc21.noarch.rpm
{% endhighlight %}

The wallpaper does now apper in the background selection tool in Gnome:

![Gnome Shell wallpapers]({filename}/images/rpm/img1.jpg){.center-block}

## Uninstall the RPMs

Below are two ways to see if the two packages from the previous section are
installed:

    :::bash
    $ rpm -qa | grep verne
    verne-backgrounds-single-15.92.1-8.fc21.noarch
    verne-backgrounds-gnome-15.92.1-8.fc21.noarch
    $ yum list installed | grep verne
    verne-backgrounds-gnome.noarch         15.92.1-8.fc21                  installed
    verne-backgrounds-single.noarch        15.92.1-8.fc21                  installed

We will now proceed to uninstall them:

    :::bash
    $ sudo rpm -e `rpm -qa | grep verne`

That's it. We have now successfully built an RPM, installed it and uninstalled
it.
