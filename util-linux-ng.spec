### Header
Summary: A collection of basic system utilities
Name: util-linux-ng
Version: 2.17.2
Release: 12.28%{?dist}.1
License: GPLv1+ and GPLv2 and GPLv2+ and LGPLv2+ and MIT and BSD with advertising and Public Domain
Group: System Environment/Base
URL: ftp://ftp.kernel.org/pub/linux/utils/util-linux-ng

### Features
%if 0%{?rhel}
%define include_raw 1
%else
%define include_raw 0
%endif

### Macros
%define floppyver 0.16
%define cytune_archs %{ix86} alpha armv4l

### Paths
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

### Dependences
BuildRequires: audit-libs-devel >= 1.0.6
BuildRequires: gettext-devel
BuildRequires: libselinux-devel
BuildRequires: ncurses-devel
BuildRequires: pam-devel
BuildRequires: texinfo
BuildRequires: zlib-devel
BuildRequires: popt-devel
BuildRequires: libutempter-devel
BuildRequires: autoconf
BuildRequires: automake

### Sources
Source0: ftp://ftp.kernel.org/pub/linux/utils/util-linux-ng/v2.17/util-linux-ng-%{version}.tar.bz2
Source1: util-linux-ng-login.pamd
Source2: util-linux-ng-remote.pamd
Source3: util-linux-ng-chsh-chfn.pamd
Source4: util-linux-ng-60-raw.rules
Source5: mount.tmpfs
Source8: nologin.c
Source9: nologin.8
Source10: uuidd.init

Source11: http://dl.sourceforge.net/floppyutil/floppy-%{floppyver}.tar.bz2

### Obsoletes & Conflicts & Provides
%ifarch alpha
Conflicts: initscripts <= 4.58
%endif
Conflicts: kernel < 2.2.12-7
# old versions of e2fsprogs contain fsck, uuidgen
Conflicts: e2fsprogs < 1.41.8-5

# old versions of util-linux have been splited to more sub-packages
Obsoletes: mount < 2.11, losetup < 2.11
Provides: mount = %{version}-%{release}, losetup = %{version}-%{release}
# Robert Love's schedutils have been merged to util-linux-2.13-pre1
Obsoletes: schedutils < 1.5
Provides: schedutils = %{version}-%{release}
# fork and rename from util-linux to util-linux-ng
Obsoletes: util-linux < 2.13.1
Provides: util-linux = %{version}-%{release}

# setarch merge in util-linux-ng-2.13
%ifarch sparc sparcv9 sparc64
Obsoletes: sparc32
%endif
Obsoletes: setarch < 2.1
Provides: setarch = %{version}-%{release}

Requires(preun): /sbin/install-info
Requires(post): /sbin/install-info
Requires(post): coreutils
Requires: pam >= 1.0.90, /etc/pam.d/system-auth
Requires: audit-libs >= 1.0.6
Requires: libuuid = %{version}-%{release}
Requires: libblkid = %{version}-%{release}
%if %{include_raw}
Requires: udev
%endif

### Floppy patches (Fedora/RHEL specific)
###
# add a missing header
Patch0: util-linux-ng-2.13-floppy-locale.patch
# add note about ATAPI IDE floppy to fdformat.8
Patch1: util-linux-ng-2.13-fdformat-man-ide.patch
# 169628 - /usr/bin/floppy doesn't work with /dev/fd0
Patch2: util-linux-ng-2.13-floppy-generic.patch


# lib/ and include/ rebase (last for RHEL6.4, based on upstrem 2.22.2)
Patch3: util-linux-ng-2.17-lib-rebase.patch


### Fedora/RHEL specific patches -- need to die!
###
# 199745 - Non-existant simpleinit(8) mentioned in ctrlaltdel(8)
Patch4: util-linux-ng-2.13-ctrlaltdel-man.patch
# /etc/blkid.tab --> /etc/blkid/blkid.tab
Patch5: util-linux-ng-2.16-blkid-cachefile.patch

### Ready for upstream?
###
# 151635 - makeing /var/log/lastlog
Patch7: util-linux-ng-2.13-login-lastlog.patch
# 231192 - ipcs is not printing correct values on pLinux
Patch8: util-linux-ng-2.15-ipcs-32bit.patch


### Upstream patches (backports)
# 533874 - RFE: libblkid should allow the developer to ask for scanning of slow devices (eg. cdroms)
Patch9: util-linux-ng-2.17-blkid-removable.patch
# 572937 - RHEL6: use microsecond resolution for blkid cache entries
Patch10: util-linux-ng-2.17-blkid-usec.patch
# 588248 - RHEL6: don't probe for RAIDs on CD-ROMs
Patch11: util-linux-ng-2.17-blkid-cdrom.patch
# 586368 - RHEL6: mdraid assembles incorrectly
# 592958 - whole disk raid members to not be identified
Patch12: util-linux-ng-2.17-blkid-raid.patch
# 586942 - Add utempter support to "script"
Patch13: util-linux-ng-2.17-script-utempter.patch
# 588298 - improve fdisk(8) move command
Patch14: util-linux-ng-2.17-fdisk-move.patch
# 594689 - partx infinite loop
Patch15: util-linux-ng-2.17-partx.patch
# 589955 - add command-line interface for libblkid topology support
Patch16: util-linux-ng-2.17-blkid-i.patch
# 604875 - memory usage in wipefs(8)
Patch17: util-linux-ng-2.17-wipefs-leak.patch
# 591133 - udev /dev/disk/by-uuid not populated
Patch18: util-linux-ng-2.17-blkid-zfs.patch
# 602657 - fdisk -l does not show correctly partitions names for FCoE volumes 
Patch19: util-linux-ng-2.17-fdisk-dm.patch

# lscpu rebase (last for RHEL6.4, based on upstrem 2.22.2)
# 591617 - lscpu does not use cpu masks properly 
# 623012 - lscpu return error after offline cpu
# 670770 - lscpu does not identify 32bit capability on AMD
# 736245 - lscpu segfault on non-uniform cpu configuration           [rhel-6.4]
# 823008 - update to the latest upstream lscpu and chcpu             [rhel-6.4]
# 837935 - lscpu coredumps on a system with 158 active processors    [rhel-6.4]
Patch20: util-linux-ng-2.17-lscpu-rebase.patch

# 612668 - [RFE] backport fsfreeze (backport from 2.18)
Patch21: util-linux-ng-2.17-fsfreeze.patch
# 598631 - shutdown, reboot, halt and C-A-D don't work
Patch22: util-linux-ng-2.17-agetty-clocal.patch
# 644503 - support for _rnetdev mount option missing in RHEL6
Patch23: util-linux-ng-2.17-rnetdev.patch


## RHEL6.1
# 619139 - fsck returns zero instead of error code 
Patch24: util-linux-ng-2.17-fsck-rc.patch
# 621312 - losetup --help returns 1 (fail) for successful command execution
Patch25: util-linux-ng-2.17-losetup-rc.patch
# 651035 - misleading reference to samba-client in mount man page, cifs options
Patch26: util-linux-ng-2.17-mount-man-cifs.patch
# 612325 - RHEL6.0 Beta-1: Add mkfs.ext4 to mkfs man page
Patch27: util-linux-ng-2.17-mkfs-man.patch
# 650879 - RHEL6: /usr/bin/column segmentation fault
Patch28: util-linux-ng-2.17-column-segfaul.patch
# 626374 - fdisk incorrectly checks alignment for non-512-byte *logical* sectors
Patch29: util-linux-ng-2.17-fdisk-512.patch
# 663731 - sfdisk -d and fdisk -l print /dev/dm-<N>
Patch30: util-linux-ng-2.17-fdisk-canonicalize.patch
# 650953 - wipefs(8) does not erase LUKS
Patch31: util-linux-ng-2.17-blkid-sbmagic.patch
# 656453 - libblkid incorrectly revalidated cache entries
Patch32: util-linux-ng-2.17-blkid-filter.patch
# 561111 - remount of tmpfs fails on RHEL6 alpha
Patch33: util-linux-ng-2.17-mount-selinux-remount.patch
# 624521 - fsck seems to run quasi-serially
Patch34: util-linux-ng-2.17-fsck-parallel.patch

# 657082 - Add lsblk (list block devices) utility
# 677569 - lsblk: SIZE integer overflow on large values
# 684037 - improperly used readlink() in util-linux-ng-2.17-lsblk.patch
# 723638 - Backport upstream extensions for lsblk                          [rhel-6.2]
# 818621 - lsblk should not open device it prints info about               [rhel-6.4]
# 809449 - Backport inverse tree (-s) option for lsblk and related patches [rhel-6.4]
# 809139 - lsblk option -D missing in manpage                              [rhel-6.4]
Patch35: util-linux-ng-2.17-lsblk.patch

# 625064 - fuse-sshfs mounts cannot be unmounted as user
Patch36: util-linux-ng-2.17-mount-subtype.patch
# 615389 - Output of "mount" is missing mapping displays for loop-mounts
Patch37: util-linux-ng-2.17-mount-autoclear.patch
# 616325 - Include findmnt in util-linux-ng package
Patch38: util-linux-ng-2.17-findmnt.patch
# 665376 - incorrectly documented the mount "atime" option
Patch39: util-linux-ng-2.17-mount-man-atime.patch
# 671357 - mount.8 man page update for ext{3,4} options
Patch40: util-linux-ng-2.17-mount-man-ext.patch
# CVE-2010-3879 fuse: unprivileged user can unmount arbitrary locations
Patch41: util-linux-ng-2.17-umount-fake.patch
# 678306 - introduce safe variant of uuid_generate_time(), fix locking of counter file
Patch42: util-linux-ng-2.17-libuuid-rebase.patch
# 678378 - util-linux-ng code review
Patch43: util-linux-ng-2.17-fsck-getopt.patch
Patch44: util-linux-ng-2.17-login-setgid.patch
Patch45: util-linux-ng-2.17-readlink.patch
Patch46: util-linux-ng-2.17-wholedisk.patch


## RHEL6.2
# 723546 - Defects revealed by Coverity scan
Patch47: util-linux-ng-2.17-coverity-e62.patch
# 723352 - cfdisk cannot read default installer partitioning
Patch48: util-linux-ng-2.17-cfdisk-size.patch
# 712158 - uid/gid overflow in ipcs
Patch49: util-linux-ng-2.17-ipcs-uid.patch
# 696959 - wipefs(8) reject partitioned devices
Patch50: util-linux-ng-2.17-wipefs-pt.patch
# 694648 - document blank line at head of fstab
Patch51: util-linux-ng-2.17-fstab-man-blank.patch
# 684203 - umount fails on inconsistent fstab
Patch52: util-linux-ng-2.17-mount-fstab-broken.patch
# 679831 --lines does not work
Patch53: util-linux-ng-2.17-tailf-man-lines.patch
# 679741 - canonicalize swap device
Patch54: util-linux-ng-2.17-swapon-dm.patch
# 692119 - include fstrim tool to enable user-space using discard/UNMAP/WRITE_SAME for enterprise arrays
Patch55: util-linux-ng-2.17-fstrim.patch
# 675999 - blkid crashes on a server with more than 128 storage devices
Patch56: util-linux-ng-2.17-blkid-128-devices.patch
# 696731 - display failed login attempts
Patch57: util-linux-ng-2.17-login-hush.patch
# 726092 - Pass host name from agetty to login
Patch58: util-linux-ng-2.17-agetty-remote.patch
# CVE-2011-1675 - mount fails to anticipate RLIMIT_FSIZE [#738789]
Patch59: util-linux-ng-2.17-mount-mtab.patch
# CVE-2011-1677 - umount may fail to remove /etc/mtab~ lock file [#738789]
Patch60: util-linux-ng-2.17-umount-mtab.patch


## RHEL6.3
# 588419 - [RFE] Changing the console login timeout
Patch61: util-linux-ng-2.17-login-timeout.patch
# 740163 - 'fdisk -l' returns confusing output
Patch62: util-linux-ng-2.17-fdisk-nopt.patch
Patch63: util-linux-ng-2.17-sfdisk-nopt.patch
# 797888 - script does not play well with csh when invoked from within /etc/csh.login
Patch64: util-linux-ng-2.17-script-csh.patch


## RHEL6.4
# 839281 - inode_readahead for ext4 should be inode_readahead_blks
# 820183 - mount(8) man page should include relatime in defaults definition
# 783514 - default barrier setting for EXT3 filesystems in mount manpage is wrong
Patch65: util-linux-ng-2.17-mount-man.patch
# 679833 - [RFE] tailf should support `-n 0`
Patch66: util-linux-ng-2.17-tailf-n0.patch
# 730891 - document cfdisk and sfdisk incompatibility with 4096-bytes sectors
Patch67: util-linux-ng-2.17-fdisk-man-iolimits.patch
# 730272 - losetup does not warn if backing file is < 512 bytes
Patch68: util-linux-ng-2.17-losetup-warnsize.patch
# 790728 - blkid ignores swap UUIDs if the first byte is a zero byte
Patch69: util-linux-ng-2.17-blkid-swap.patch
# 719927 - [RFE] add adjtimex --compare functionality to hwclock
Patch70: util-linux-ng-2.17-hwclock-compare.patch
# 819945 - hwclock --systz causes a system time jump
Patch71: util-linux-ng-2.17-hwclock-systz.patch
# 845971 - while reading /etc/fstab, mount command returns a device before a directory.
Patch72: util-linux-ng-2.17-mount-getfs.patch
# 858009 - login doesn't update /var/run/utmp properly
Patch73: util-linux-ng-2.17-login-utmp.patch
# 845477 - Duplicate SElinux mount options cause mounting from the commandline to fail
# [overwrites util-linux-ng-2.17-mount-selinux-remount.patch from RHEL6.1]
Patch74: util-linux-ng-2.17-mount-selinux-dedup.patch
# 823008 - update to the latest upstream lscpu and chcpu
Patch75: util-linux-ng-2.17-chcpu.patch
# 892471 - CVE-2013-0157 mount folder existence information disclosure
Patch76: util-linux-ng-2.17-mount-canonicalize.patch

## RHEL6.5
# 911756 - Make silicon medley signature recognition more robust
Patch77: util-linux-ng-2.17-blkid-silraid.patch
# 917678 - mount in RHEL 6.4 ignores user option
Patch78: util-linux-ng-2.17-mount-fstab-symlinks.patch
# 816342 - agetty: improve CLOCAL flag management
Patch79: util-linux-ng-2.17-agetty-clocal-mode.patch
# 846790 - missing information about threads in kill(2) man page
Patch80: util-linux-ng-2.17-kill-man-threads.patch
# 864585 - "mount -av" displays "nothing was mounted" when a /sbin/mount.<fs> successed
Patch81: util-linux-ng-2.17-mount-all.patch
# 868850 - sfdisk man pages should refer block devices as "block devices" rather than disks.
Patch82: util-linux-ng-2.17-sfdisk-man-disk.patch
# 870128 - improve blkid documentation
Patch83: util-linux-ng-2.17-blkid-man-removable.patch
# 870854 - Cannot use user@domain format for console logins
Patch84: util-linux-ng-2.17-agetty-chars.patch
# 872291 - "man hwclock" says to run non-existent "adjtimex" utility
Patch85: util-linux-ng-2.17-hwclock-man-adjtimex.patch
# 885313 - hexdump segfault
Patch86: util-linux-ng-2.17-hexdump-segfault.patch
# 915844 - mount man page incorrectly describes behaviour of "relatime" mount option
Patch87: util-linux-ng-2.17-mount-man-relatime.patch
# 947062 - blkdiscard command support
Patch88:  util-linux-ng-2.17-blkdiscard.patch
# 966735 - CPU add/delete util-linux-ng patch
Patch89: util-linux-ng-2.17-lscpu-hotplug.patch
# 859523 - fallocate: add punch hole support
Patch90: util-linux-ng-2.17-fallocate-holes.patch

## RHEL-6.6
# 1072583 - hwclock --systohc can hang on busy or virtual machine
Patch91: util-linux-ng-2.17-hwclock-systohc.patch
# 1033309 - man rename references mmv command which is not available
Patch92: util-linux-ng-2.17-rename-man.patch
# 1039187 - taskset man page PERMISSIONS section is incorrect
Patch93: util-linux-ng-2.17-taskset-man.patch
# 999625 - mount does not appear to be correctly documented for default mount options
Patch94: util-linux-ng-2.17-mount-man-defaults.patch
# 1004021 - document blkid -w behaviour
Patch95: util-linux-ng-2.17-blkid-man-w.patch
# 1011590 - fdisk: Floating point exception on multipath mapped device
Patch96: util-linux-ng-2.17-fdisk-SIGFPE.patch
# 1031641 - findmnt should handle better trailing "/" in /proc/mounts entries
Patch97: util-linux-ng-2.17-libmount-slash.patch
# 1104575 - kill(1) doesn't check errno after calling strtol()
Patch98: util-linux-ng-2.17-kill-strtol.patch
# 1049055 - backport PID ns support to unshare(1) in util-linux-ng
Patch99: util-linux-ng-2.17-unshare.patch
# 957906 - backport 'nsenter' utility to util-linux
Patch100: util-linux-ng-2.17-nsenter.patch
# 619521 - requesting to add logins(1m) command to distribution of Red Hat
Patch101: util-linux-ng-2.17-lslogins.patch
# 1097715 - flock nfs file fails on nfsv4
Patch102: util-linux-ng-2.17-flock-nfs.patch
# 1016470 - Document that blockdev --setbsz call has never worked
Patch103: util-linux-ng-2.17-blockdev-setbsz.patch

## RHEL6.8
# 1191236 - 'umount -f' calls readlink on dead NFS mounts and hangs
Patch104: util-linux-ng-2.17-umount-canonicalize.patch
# 1172297 - umount --fake fails to edit mtab for NFS mounts which are already gone
Patch105: util-linux-ng-2.17-umount-fake-helpers.patch
# 961148 - RHEL6: swapon: add "discard" support
Patch106: util-linux-ng-2.17-swapon-discard.patch
# 1168390 - lscpu doesn't show all nodes on a discontinuous NUMA setup
Patch107: util-linux-ng-2.17-lscpu-numa.patch
# 1023655 - 'pppd' hangs (uninterruptable) when run on tty
Patch108: util-linux-ng-2.17-login-vhangup.patch
# 1215840 - slogins segfault and failure to allocate memory
Patch109: util-linux-ng-2.17-lslogins-lg.patch
# 1088411 - RHEL6: lsblk does not list dm-multipath and partitioned devices
Patch110: util-linux-ng-2.17-lsblk-mpath.patch
# 1150302 - ionice support class names
Patch111: util-linux-ng-2.17-ionice-str.patch
# 1085062 - fdisk -l fails to fully process /proc/partitions when multipath device
Patch112: util-linux-ng-2.17-fdisk-wholedisk.patch
Patch113: util-linux-ng-2.17-fdisk-tryonly.patch
# 1122839 - fallocate and findmnt have wrong options according to man pages
Patch114: util-linux-ng-2.17-opts-typos.patch
# 1089663 - Not all xfs mount options are described in mount(8)
Patch115: util-linux-ng-2.17-mount-man-xfs.patch
# 1295737 - man page for hwclock doesn't include --compare option
Patch116: util-linux-ng-2.17-hwclock-man-compare.patch
# 1140594 - mount --move badly documented
Patch117: util-linux-ng-2.17-mount-man-move.patch
# 1296894 - RHEL6: update audit event in hwclock
Patch118: util-linux-ng-2.17-hwclock-audit.patch
# 1266191 - fdisk does not handle >2TB disks correctly
Patch119: util-linux-ng-2.17-fdisk-longlong.patch
# 1299687 - Partition size is not updated by fdisk "f" subcommand
Patch120: util-linux-ng-2.17-fdisk-reorder.patch
# 1316864 ipcmk fails with "Invalid argument" while creating a shared memory of size 2 GiB
Patch121: util-linux-ng-2.17-ipcmk-size.patch

#
# RHEL6.9
#
# 1320360 - lscpu shows wrong "Virtualization type" on Xen paravirtualization guest (PV)
Patch122: 0122-lscpu-correct-the-Virtualization-type-on-Xen-DomU-PV.patch
# 1319642 - [util-linux-ng] lscpu: Fix model and model name on Power Systems
Patch123: 0123-lscpu-Fix-model-and-model-name-on-Power-Systems.patch
# 1319642 - [util-linux-ng] lscpu: Fix model and model name on Power Systems
Patch124: 0124-sfdisk-remove-useless-CDROM-detection-for-s.patch
# 1310035 - Hostname not being displayed besides the telnet login prompt
Patch125: 0125-login-display-hostname-on-login-prompt.patch
# 1310317 - fdisk -l fdisk double open fd
Patch126: 0126-fdisk-l-double-open-fd.patch
# 1337478 - wrong error handler and/or error message on fdisk call as not root user
Patch127: 0127-fdisk-follow-errno-on-error-message.patch
# 1349192 - RHEL6.8 util-linux-ng requires 642 kernel, but does not specify it as a dependency
Patch128: 0128-lib-linux_version-add-code-to-get-kernel-release.patch
# 1023655 - 'pppd' hangs (uninterruptable) when run on tty
Patch129: 0129-login-check-kernel-version-for-proper-vhangup.patch

#
# RHEL6.9.Z
#
# 1448225 - Please add the -H option to login
Patch130: 0130-login-add-H-option.patch

%description
The util-linux-ng package contains a large variety of low-level system
utilities that are necessary for a Linux system to function. Among
others, Util-linux contains the fdisk configuration tool and the login
program.


%package -n libblkid
Summary: Block device ID library
Group: Development/Libraries
License: LGPLv2+
Requires: libuuid = %{version}-%{release}

%description -n libblkid
This is block device identification library, part of util-linux-ng.


%package -n libblkid-devel
Summary: Block device ID library
Group: Development/Libraries
License: LGPLv2+
Provides: libblkid-static = %{version}-%{release}
Requires: libblkid = %{version}-%{release}
Requires: pkgconfig

%description -n libblkid-devel
This is the block device identification development library and headers,
part of util-linux-ng.


%package -n libuuid
Summary: Universally unique ID library
Group: Development/Libraries
License: BSD

%description -n libuuid
This is the universally unique ID library, part of util-linux-ng.

The libuuid library generates and parses 128-bit universally unique
id's (UUID's).  A UUID is an identifier that is unique across both
space and time, with respect to the space of all UUIDs.  A UUID can
be used for multiple purposes, from tagging objects with an extremely
short lifetime, to reliably identifying very persistent objects
across a network.

See also the "uuid" package, which is a separate implementation.

%package -n libuuid-devel
Summary: Universally unique ID library
Group: Development/Libraries
License: BSD
Provides: libuuid-static = %{version}-%{release}
Requires: libuuid = %{version}-%{release}
Requires: pkgconfig

%description -n libuuid-devel
This is the universally unique ID development library and headers,
part of util-linux-ng.

The libuuid library generates and parses 128-bit universally unique
id's (UUID's).  A UUID is an identifier that is unique across both
space and time, with respect to the space of all UUIDs.  A UUID can
be used for multiple purposes, from tagging objects with an extremely
short lifetime, to reliably identifying very persistent objects
across a network.

See also the "uuid-devel" package, which is a separate implementation.


%package -n uuidd
Summary: Helper daemon to guarantee uniqueness of time-based UUIDs
Group: System Environment/Daemons
Requires: libuuid = %{version}-%{release}
License: GPLv2
Requires(pre): shadow-utils
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/service
Requires(preun): /sbin/chkconfig

%description -n uuidd
The uuidd package contains a userspace daemon (uuidd) which guarantees
uniqueness of time-based UUID generation even at very high rates on
SMP systems.


%prep
%setup -q -a 11
cp %{SOURCE8} %{SOURCE9} .

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch98 -p1
%patch99 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch119 -p1
%patch120 -p1
%patch121 -p1
%patch122 -p1
%patch123 -p1
%patch124 -p1
%patch125 -p1
%patch126 -p1
%patch127 -p1
%patch128 -p1
%patch129 -p1
%patch130 -p1

%build
unset LINGUAS || :

# unfortunately, we did changes to build-system
./autogen.sh

export CFLAGS="-D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64 $RPM_OPT_FLAGS"
export SUID_CFLAGS="-fpie"
export SUID_LDFLAGS="-pie"
%configure \
	--bindir=/bin \
	--sbindir=/sbin \
	--libdir=/%{_lib} \
	--disable-silent-rules \
	--disable-wall \
	--enable-partx \
	--enable-login-utils \
	--enable-kill \
	--enable-write \
%if %{include_raw}
	--enable-raw \
%endif
	--with-selinux \
	--with-audit \
	--with-utempter \
	--disable-makeinstall-chown

# build util-linux-ng
make %{?_smp_mflags}

# build floppy stuff
pushd floppy-%{floppyver}
%configure --disable-gtk2
make %{?_smp_mflags}
popd

# build nologin
gcc $CFLAGS -o nologin nologin.c

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/{bin,sbin}
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_infodir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man{1,6,8,5}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/{pam.d,security/console.apps,blkid}
mkdir -p ${RPM_BUILD_ROOT}/var/log
touch ${RPM_BUILD_ROOT}/var/log/lastlog
chmod 0644 ${RPM_BUILD_ROOT}/var/log/lastlog

# install util-linux-ng
make install DESTDIR=${RPM_BUILD_ROOT}

# inslall floppy stuff
pushd floppy-%{floppyver}
make install DESTDIR=${RPM_BUILD_ROOT}
popd

# install nologin
install -m 755 nologin ${RPM_BUILD_ROOT}/sbin
install -m 644 nologin.8 ${RPM_BUILD_ROOT}%{_mandir}/man8

%if %{include_raw}
echo '.so man8/raw.8' > $RPM_BUILD_ROOT%{_mandir}/man8/rawdevices.8
{
	# see RH bugzilla #216664
	mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/udev/rules.d
	pushd ${RPM_BUILD_ROOT}%{_sysconfdir}/udev/rules.d
	install -m 644 %{SOURCE4} ./60-raw.rules
	popd
}
%endif

# Our own initscript for uuidd
install -D -m 755 %{SOURCE10} ${RPM_BUILD_ROOT}/etc/rc.d/init.d/uuidd
# And a dirs uuidd needs that the makefiles don't create
install -d ${RPM_BUILD_ROOT}/var/run/uuidd
install -d ${RPM_BUILD_ROOT}/var/lib/libuuid

# libtool junk
rm -rf ${RPM_BUILD_ROOT}%{_libdir}/*.la

%ifarch sparc sparc64 sparcv9
rm -rf ${RPM_BUILD_ROOT}%{_bindir}/sunhostid
cat << E-O-F > ${RPM_BUILD_ROOT}%{_bindir}/sunhostid
#!/bin/sh
# this should be %{_bindir}/sunhostid or somesuch.
# Copyright 1999 Peter Jones, <pjones@redhat.com> .
# GPL and all that good stuff apply.
(
idprom=\`cat /proc/openprom/idprom\`
echo \$idprom|dd bs=1 skip=2 count=2
echo \$idprom|dd bs=1 skip=27 count=6
echo
) 2>/dev/null
E-O-F
chmod 755 ${RPM_BUILD_ROOT}%{_bindir}/sunhostid
%endif

# PAM settings
{
	pushd ${RPM_BUILD_ROOT}%{_sysconfdir}/pam.d
	install -m 644 %{SOURCE1} ./login
	install -m 644 %{SOURCE2} ./remote
	install -m 644 %{SOURCE3} ./chsh
	install -m 644 %{SOURCE3} ./chfn
	popd
}

ln -sf ../../sbin/hwclock ${RPM_BUILD_ROOT}/usr/sbin/hwclock
ln -sf hwclock ${RPM_BUILD_ROOT}/sbin/clock
echo ".so man8/hwclock.8" > ${RPM_BUILD_ROOT}%{_mandir}/man8/clock.8

# remove libtool junk  (TODO)
#rm -f ${RPM_BUILD_ROOT}/%{_lib}/libblkid.la

# install tmpfs mount helper
pushd ${RPM_BUILD_ROOT}/sbin
install -m 755 %{SOURCE5} ./mount.tmpfs
popd

# unsupported on %{ix86} alpha armv4l
%ifnarch %cytune_archs
rm -f $RPM_BUILD_ROOT%{_bindir}/cytune $RPM_BUILD_ROOT%{_mandir}/man8/cytune.8*
%endif

# unsupported on s390
%ifarch s390 s390x
for I in /usr/{bin,sbin}/{fdformat,tunelp,floppy} \
	%{_mandir}/man8/{fdformat,tunelp,floppy}.8* \
	/sbin/{hwclock,clock} \
	/usr/sbin/hwclock \
	%{_mandir}/man8/{hwclock,clock}.8*; do
	
	rm -f $RPM_BUILD_ROOT$I
done
%endif

# unsupported on SPARCs
%ifarch sparc sparcv9 sparc64
for I in /sbin/sfdisk \
	%{_mandir}/man8/sfdisk.8* \
	%doc fdisk/sfdisk.examples \
	/sbin/cfdisk \
	%{_mandir}/man8/cfdisk.8*; do
	
	rm -f $RPM_BUILD_ROOT$I
done
%endif

# deprecated commands
for I in /sbin/fsck.minix /sbin/mkfs.{bfs,minix} /sbin/sln \
	/usr/bin/chkdupexe %{_bindir}/line %{_bindir}/pg %{_bindir}/newgrp \
	/sbin/shutdown /usr/sbin/vipw /usr/sbin/vigr; do
	rm -f $RPM_BUILD_ROOT$I
done

# deprecated man pages
for I in man1/chkdupexe.1 man1/line.1 man1/pg.1 man1/newgrp.1 \
	man8/fsck.minix.8 man8/mkfs.minix.8 man8/mkfs.bfs.8 \
	man8/vipw.8 man8/vigr; do
	rm -rf $RPM_BUILD_ROOT%{_mandir}/${I}*
done

# deprecated docs
for I in text-utils/README.pg misc-utils/README.reset floppy-%{floppyver}/README.html; do
	rm -rf $I
done

# rename docs
mv floppy-%{floppyver}/README floppy-%{floppyver}/README.floppy

# we install getopt/getopt-*.{bash,tcsh} as doc files
chmod 644 getopt/getopt-*.{bash,tcsh}
rm -f ${RPM_BUILD_ROOT}%{_datadir}/getopt/*
rmdir ${RPM_BUILD_ROOT}%{_datadir}/getopt

ln -sf ../../bin/kill $RPM_BUILD_ROOT%{_bindir}/kill

# /usr/sbin -> /sbin
for I in addpart delpart partx; do
	if [ -e $RPM_BUILD_ROOT/usr/sbin/$I ]; then
		mv $RPM_BUILD_ROOT/usr/sbin/$I $RPM_BUILD_ROOT/sbin/$I
	fi
done

# /usr/bin -> /bin
for I in logger taskset; do
	if [ -e $RPM_BUILD_ROOT/usr/bin/$I ]; then
		mv $RPM_BUILD_ROOT/usr/bin/$I $RPM_BUILD_ROOT/bin/$I
	fi
done

# /sbin -> /bin
for I in raw; do
	if [ -e $RPM_BUILD_ROOT/sbin/$I ]; then
		mv $RPM_BUILD_ROOT/sbin/$I $RPM_BUILD_ROOT/bin/$I
	fi
done

ln -sf ../../bin/logger $RPM_BUILD_ROOT%{_bindir}/logger

# omit info/dir file
rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

# unnecessary devel library
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libmount.so
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libmount.a

# find MO files
%find_lang %name

# the files section supports only one -f option...
mv %{name}.lang %{name}.files

# create list of setarch(8) symlinks
find  $RPM_BUILD_ROOT%{_bindir}/ -regextype posix-egrep -type l \
	-regex ".*(linux32|linux64|s390|s390x|i386|ppc|ppc64|ppc32|sparc|sparc64|sparc32|sparc32bash|mips|mips64|mips32|ia64|x86_64)$" \
	-printf "%{_bindir}/%f\n" >> %{name}.files

find  $RPM_BUILD_ROOT%{_mandir}/man8 -regextype posix-egrep  \
	-regex ".*(linux32|linux64|s390|s390x|i386|ppc|ppc64|ppc32|sparc|sparc64|sparc32|sparc32bash|mips|mips64|mips32|ia64|x86_64)\.8.*" \
	-printf "%{_mandir}/man8/%f*\n" >> %{name}.files

%clean
[ "${RPM_BUILD_ROOT}" != "/" ] && rm -rf ${RPM_BUILD_ROOT}

%post
/sbin/install-info %{_infodir}/ipc.info %{_infodir}/dir || :
# only for minimal buildroots without /var/log
[ -d /var/log ] || /bin/mkdir -p /var/log
/bin/touch /var/log/lastlog
/bin/chown root:root /var/log/lastlog
/bin/chmod 0644 /var/log/lastlog
# Fix the file context, do not use restorecon
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
	SECXT=$( /usr/sbin/matchpathcon -n /var/log/lastlog 2> /dev/null )
	if [ -n "$SECXT" ]; then
		# Selinux enabled, but without policy? It's true for buildroots
		# without selinux stuff on host machine with enabled selinux.
		# We don't want to use any RPM dependence on selinux policy for
		# matchpathcon(2). SELinux policy should be optional.
		/usr/bin/chcon "$SECXT"  /var/log/lastlog >/dev/null 2>&1 || :
	fi
fi
/sbin/ldconfig

%postun
/sbin/ldconfig

%preun
if [ "$1" = 0 ]; then
	/sbin/install-info --del %{_infodir}/ipc.info %{_infodir}/dir || :
fi
exit 0


%post -n libblkid
/sbin/ldconfig
[ -e /etc/blkid.tab ] && mv /etc/blkid.tab /etc/blkid/blkid.tab || :
[ -e /etc/blkid.tab.old ] && mv /etc/blkid.tab.old /etc/blkid/blkid.tab.old || :

%postun -n libblkid -p /sbin/ldconfig

%post -n libuuid -p /sbin/ldconfig
%postun -n libuuid -p /sbin/ldconfig

%pre -n uuidd
getent group uuidd >/dev/null || groupadd -r uuidd
getent passwd uuidd >/dev/null || \
useradd -r -g uuidd -d /var/lib/libuuid -s /sbin/nologin \
    -c "UUID generator helper daemon" uuidd
exit 0

%post -n uuidd
/sbin/chkconfig --del uuidd 2>&1 || :
/sbin/chkconfig --add uuidd

%preun -n uuidd
if [ "$1" = 0 ]; then
	/sbin/service uuidd stop > /dev/null 2>&1 || :
	/sbin/chkconfig --del uuidd
fi

%files -f %{name}.files
%defattr(-,root,root)
%doc */README.* NEWS AUTHORS licenses/* README*
%doc getopt/getopt-*.{bash,tcsh}

%config(noreplace)	%{_sysconfdir}/pam.d/chfn
%config(noreplace)	%{_sysconfdir}/pam.d/chsh
%config(noreplace)	%{_sysconfdir}/pam.d/login
%config(noreplace)	%{_sysconfdir}/pam.d/remote

%attr(4755,root,root)	/bin/mount
%attr(4755,root,root)	/bin/umount
%attr(755,root,root)	/sbin/mount.tmpfs
%attr(755,root,root)	/bin/login
%attr(4711,root,root)	%{_bindir}/chfn
%attr(4711,root,root)	%{_bindir}/chsh
%attr(2755,root,tty)	%{_bindir}/write

%ghost %attr(0644,root,root)	%verify(not md5 size mtime)	/var/log/lastlog

# this private package library
/%{_lib}/libmount.so.*

/bin/dmesg
/bin/kill
/bin/more
/bin/taskset
/bin/lsblk
/bin/findmnt
/bin/logger
/sbin/addpart
/sbin/agetty
/sbin/blkid
/sbin/blockdev
/sbin/ctrlaltdel
/sbin/delpart
/sbin/blkdiscard
/sbin/fdisk
/sbin/findfs
/sbin/fsck
/sbin/fsck.cramfs
/sbin/fsfreeze
/sbin/losetup
/sbin/mkfs
/sbin/mkfs.cramfs
/sbin/mkswap
/sbin/nologin
/sbin/partx
/sbin/pivot_root
/sbin/swapoff
/sbin/swapon
/sbin/switch_root
/sbin/wipefs
/sbin/fstrim
/sbin/chcpu

%{_bindir}/cal
%{_bindir}/chrt
%{_bindir}/col
%{_bindir}/colcrt
%{_bindir}/colrm
%{_bindir}/column
%{_bindir}/ddate
%{_bindir}/fallocate
%{_bindir}/flock
%{_bindir}/getopt
%{_bindir}/hexdump
%{_bindir}/ionice
%{_bindir}/ipcmk
%{_bindir}/ipcrm
%{_bindir}/ipcs
%{_bindir}/isosize
%{_bindir}/kill
%{_bindir}/logger
%{_bindir}/look
%{_bindir}/lscpu
%{_bindir}/lslogins
%{_bindir}/mcookie
%{_bindir}/namei
%{_bindir}/nsenter
%{_bindir}/rename
%{_bindir}/renice
%{_bindir}/rev
%{_bindir}/script
%{_bindir}/scriptreplay
%{_bindir}/setarch
%{_bindir}/setsid
%{_bindir}/setterm
%{_bindir}/tailf
%{_bindir}/ul
%{_bindir}/unshare
%{_bindir}/uuidgen
%{_bindir}/whereis

%{_sbindir}/ldattach
%{_sbindir}/readprofile
%{_sbindir}/rtcwake

%{_infodir}/ipc.info*

%{_mandir}/man1/cal.1*
%{_mandir}/man1/chfn.1*
%{_mandir}/man1/chrt.1*
%{_mandir}/man1/chsh.1*
%{_mandir}/man1/col.1*
%{_mandir}/man1/colcrt.1*
%{_mandir}/man1/colrm.1*
%{_mandir}/man1/column.1*
%{_mandir}/man1/ddate.1*
%{_mandir}/man1/dmesg.1*
%{_mandir}/man1/fallocate.1*
%{_mandir}/man1/flock.1*
%{_mandir}/man1/getopt.1*
%{_mandir}/man1/hexdump.1*
%{_mandir}/man1/ionice.1*
%{_mandir}/man1/ipcmk.1*
%{_mandir}/man1/ipcrm.1*
%{_mandir}/man1/ipcs.1*
%{_mandir}/man1/kill.1*
%{_mandir}/man1/logger.1*
%{_mandir}/man1/login.1*
%{_mandir}/man1/look.1*
%{_mandir}/man1/lscpu.1*
%{_mandir}/man1/lslogins.1*
%{_mandir}/man1/mcookie.1*
%{_mandir}/man1/more.1*
%{_mandir}/man1/namei.1*
%{_mandir}/man1/nsenter.1*
%{_mandir}/man1/readprofile.1*
%{_mandir}/man1/rename.1*
%{_mandir}/man1/renice.1*
%{_mandir}/man1/rev.1*
%{_mandir}/man1/script.1*
%{_mandir}/man1/scriptreplay.1*
%{_mandir}/man1/setsid.1*
%{_mandir}/man1/setterm.1*
%{_mandir}/man1/tailf.1*
%{_mandir}/man1/taskset.1*
%{_mandir}/man1/ul.1*
%{_mandir}/man1/unshare.1*
%{_mandir}/man1/uuidgen.1*
%{_mandir}/man1/whereis.1*
%{_mandir}/man1/write.1*

%{_mandir}/man5/fstab.5*

%{_mandir}/man8/addpart.8*
%{_mandir}/man8/agetty.8*
%{_mandir}/man8/blkid.8*
%{_mandir}/man8/blockdev.8*
%{_mandir}/man8/ctrlaltdel.8*
%{_mandir}/man8/delpart.8*
%{_mandir}/man8/fdisk.8*
%{_mandir}/man8/findfs.8*
%{_mandir}/man8/findmnt.8*
%{_mandir}/man8/fsck.8*
%{_mandir}/man8/fsfreeze.8*
%{_mandir}/man8/isosize.8*
%{_mandir}/man8/ldattach.8*
%{_mandir}/man8/losetup.8*
%{_mandir}/man8/lsblk.8*
%{_mandir}/man8/mkfs.8*
%{_mandir}/man8/mkswap.8*
%{_mandir}/man8/mount.8*
%{_mandir}/man8/nologin.8*
%{_mandir}/man8/partx.8*
%{_mandir}/man8/pivot_root.8*
%{_mandir}/man8/rtcwake.8*
%{_mandir}/man8/setarch.8*
%{_mandir}/man8/swapoff.8*
%{_mandir}/man8/swapon.8*
%{_mandir}/man8/switch_root.8*
%{_mandir}/man8/umount.8*
%{_mandir}/man8/wipefs.8*
%{_mandir}/man8/fstrim.8*
%{_mandir}/man8/chcpu.8*
%{_mandir}/man8/blkdiscard.8*

%if %{include_raw}
/bin/raw
%config(noreplace)	%{_sysconfdir}/udev/rules.d/60-raw.rules
%{_mandir}/man8/raw.8*
%{_mandir}/man8/rawdevices.8*
%endif

%ifnarch s390 s390x
/sbin/clock
/sbin/hwclock
%{_bindir}/floppy
%{_sbindir}/fdformat
%{_sbindir}/hwclock
%{_sbindir}/tunelp
%{_mandir}/man8/fdformat.8*
%{_mandir}/man8/floppy.8*
%{_mandir}/man8/hwclock.8*
%{_mandir}/man8/clock.8*
%{_mandir}/man8/tunelp.8*
%endif

%ifnarch sparc sparcv9 sparc64
%doc fdisk/sfdisk.examples
/sbin/cfdisk
/sbin/sfdisk
%{_mandir}/man8/cfdisk.8*
%{_mandir}/man8/sfdisk.8*
%endif

%ifarch sparc sparc64 sparcv9
%{_bindir}/sunhostid
%endif

%ifarch %cytune_archs
%{_bindir}/cytune
%{_mandir}/man8/cytune.8*
%endif


%files -n uuidd
%defattr(-,root,root)
/etc/rc.d/init.d/uuidd
%{_mandir}/man8/uuidd.8*
%attr(-, uuidd, uuidd) %{_sbindir}/uuidd
%dir %attr(2775, uuidd, uuidd) /var/lib/libuuid
%dir %attr(2775, uuidd, uuidd) /var/run/uuidd


%files -n libblkid
%defattr(-,root,root)
%dir /etc/blkid
/%{_lib}/libblkid.so.*


%files -n libblkid-devel
%defattr(-,root,root)
%{_libdir}/libblkid.a
%{_libdir}/libblkid.so
%{_includedir}/blkid
%{_mandir}/man3/libblkid.3*
%{_libdir}/pkgconfig/blkid.pc


%files -n libuuid
%defattr(-,root,root)
/%{_lib}/libuuid.so.*

%files -n libuuid-devel
%defattr(-,root,root)
%{_libdir}/libuuid.a
%{_libdir}/libuuid.so
%{_includedir}/uuid
%{_mandir}/man3/uuid.3*
%{_mandir}/man3/uuid_clear.3*
%{_mandir}/man3/uuid_compare.3*
%{_mandir}/man3/uuid_copy.3*
%{_mandir}/man3/uuid_generate.3*
%{_mandir}/man3/uuid_generate_random.3*
%{_mandir}/man3/uuid_generate_time.3*
%{_mandir}/man3/uuid_is_null.3*
%{_mandir}/man3/uuid_parse.3*
%{_mandir}/man3/uuid_time.3*
%{_mandir}/man3/uuid_unparse.3*
%{_libdir}/pkgconfig/uuid.pc


%changelog
* Tue Oct 31 2017 Karel Zak <kzak@redhat.com> 2.17.2-12.28.el6_9.1
- fix #1448225 - Please add the -H option to login

* Tue Jan 03 2017 Karel Zak <kzak@redhat.com> 2.17.2-12.28
- remove dependence on kernel (#1349192)

* Mon Jan 02 2017 Karel Zak <kzak@redhat.com> 2.17.2-12.27
- fix #1349192 - RHEL6.8 util-linux-ng requires 642 kernel, but does not specify it as a dependency
- fix #1023655 - 'pppd' hangs (uninterruptable) when run on tty

* Mon Oct 31 2016 Karel Zak <kzak@redhat.com> 2.17.2-12.26
- fix #1320360 - lscpu shows wrong "Virtualization type" on Xen paravirtualization guest (PV)
- fix #1319642 - [util-linux-ng] lscpu: Fix model and model name on Power Systems
- fix #1319642 - [util-linux-ng] lscpu: Fix model and model name on Power Systems
- fix #1310035 - Hostname not being displayed besides the telnet login prompt
- fix #1310317 - fdisk -l fdisk double open fd
- fix #1337478 - wrong error handler and/or error message on fdisk call as not root user

* Wed Oct 12 2016 Karel Zak <kzak@redhat.com> 2.17.2-12.25
- fix #1349192 - RHEL6.8 util-linux-ng requires 642 kernel, but does not specify it as a dependency

* Tue Mar 15 2016 Karel Zak <kzak@redhat.com> 2.17.2-12.24
- fix #1316864 - ipcmk fails with "Invalid argument" while creating a shared memory of size 2 GiB

* Tue Mar  8 2016 Karel Zak <kzak@redhat.com> 2.17.2-12.23
- improve patch for #1122839
- improve patch for #1085062

* Fri Feb 12 2016 Karel Zak <kzak@redhat.com> 2.17.2-12.22
- fix #1023655 - improve the patch to avoid signals by TCSAFLUSH

* Mon Jan 25 2016 Karel Zak <kzak@redhat.com> 2.17.2-12.21
- fix #1299687 - Partition size is not updated by fdisk "f" subcommand

* Mon Jan 11 2016 Karel Zak <kzak@redhat.com> 2.17.2-12.20
- add missing function declaration for #1168390 bugfix

* Mon Jan 11 2016 Karel Zak <kzak@redhat.com> 2.17.2-12.19
- fix #1088411 - lsblk does not list dm-multipath and partitioned devices
- fix #1215840 - slogins segfault and failure to allocate memory
- fix #1023655 - 'pppd' hangs (uninterruptable) when run on tty
- fix #1168390 - lscpu doesn't show all nodes on a discontinuous NUMA setup
- fix #1191236 - 'umount -f' calls readlink on dead NFS mounts and hangs
- fix #1172297 - umount --fake fails to edit mtab for NFS mounts which are already gone
- fix #961148  - RHEL6: swapon: add "discard" support
- fix #1150302 - ionice support class names
- fix #1085062 - fdisk -l fails to fully process /proc/partitions when multipath device
- fix #1122839 - fallocate and findmnt have wrong options according to man pages
- fix #1089663 - Not all xfs mount options are described in mount(8)
- fix #1295737 - man page for hwclock doesn't include --compare option
- fix #1140594 - mount --move badly documented
- fix #1296894 - RHEL6: update audit event in hwclock
- fix #1266191 - fdisk does not handle >2TB disks correctly

* Mon Aug 11 2014 Karel Zak <kzak@redhat.com> 2.17.2-12.18
- fix #1016470 - Document that blockdev --setbsz call has never worked

* Tue Jun 24 2014 Karel Zak <kzak@redhat.com> 2.17.2-12.17
- fix #1097715 - flock nfs file fails on nfsv4

* Fri Jun 13 2014 Karel Zak <kzak@redhat.com> 2.17.2-12.16
- fix #1033309 - man rename references mmv command which is not available
- fix #1039187 - taskset man page PERMISSIONS section is incorrect
- fix #999625 - mount does not appear to be correctly documented for default mount options
- fix #1004021 - document blkid -w behaviour
- fix #1011590 - fdisk: Floating point exception on multipath mapped device
- fix #1031641 - findmnt should handle better trailing "/" in /proc/mounts entries
- fix #1104575 - kill(1) doesn't check errno after calling strtol()
- fix #1049055 - backport PID ns support to unshare(1) in util-linux-ng
- fix #957906 - backport 'nsenter' utility to util-linux
- fix #619521 - requesting to add logins(1m) command to distribution of Red Hat

* Wed Apr  9 2014 Karel Zak <kzak@redhat.com> 2.17.2-12.15
- fix #1072583 - hwclock --systohc can hang on busy or virtual machine

* Tue Aug  6 2013 Karel Zak <kzak@redhat.com> 2.17.2-12.14
- improve agetty patches for #816342 and #870854

* Tue Jul 30 2013 Karel Zak <kzak@redhat.com> 2.17.2-12.13
- fix #816342 - agetty: improve CLOCAL flag management
- fix #846790 - missing information about threads in kill(2) man page
- fix #864585 - "mount -av" displays "nothing was mounted" when a /sbin/mount.<fs> successed
- fix #868850 - sfdisk man pages should refer block devices as "block devices" rather than disks.
- fix #870128 - improve blkid documentation
- fix #870854 - Cannot use user@domain format for console logins
- fix #872291 - "man hwclock" says to run non-existent "adjtimex" utility
- fix #958313 - Add /bin/logger symlink
- fix #885313 - hexdump segfault
- fix #915844 - mount man page incorrectly describes behaviour of "relatime" mount option
- fix #947062 - blkdiscard command support
- fix #966735 - CPU add/delete util-linux-ng patch
- fix #859523 - fallocate: add punch hole support

* Tue Apr 23 2013 Karel Zak <kzak@redhat.com> 2.17.2-12.12
- fix #917678 - mount in RHEL 6.4 ignores user option

* Wed Apr 17 2013 Karel Zak <kzak@redhat.com> 2.17.2-12.11
- improve patch for #911756 to be robust on big-endian machines

* Wed Apr 10 2013 Karel Zak <kzak@redhat.com> 2.17.2-12.10
- fix #911756 - Make silicon medley signature recognition more robust

* Wed Jan  9 2013 Karel Zak <kzak@redhat.com> 2.17.2-12.9
- fix #892471 - CVE-2013-0157 mount folder existence information disclosure

* Tue Oct  2 2012 Karel Zak <kzak@redhat.com> 2.17.2-12.8
- fix #679833 - [RFE] tailf should support `-n 0`
- fix #719927 - [RFE] add adjtimex --compare functionality to hwclock
- fix #730272 - losetup does not warn if backing file is < 512 bytes
- fix #730891 - document cfdisk and sfdisk incompatibility with 4096-bytes sectors
- fix #736245 - lscpu segfault on non-uniform cpu configuration
- fix #783514 - default barrier setting for EXT3 filesystems in mount manpage is wrong
- fix #790728 - blkid ignores swap UUIDs if the first byte is a zero byte
- fix #818621 - lsblk should not open device it prints info about
- fix #819945 - hwclock --systz causes a system time jump
- fix #820183 - mount(8) man page should include relatime in defaults definition
- fix #823008 - update to the latest upstream lscpu and chcpu
- fix #837935 - lscpu coredumps on a system with 158 active processors
- fix #839281 - inode_readahead for ext4 should be inode_readahead_blks
- fix #845477 - Duplicate SElinux mount options cause mounting from the commandline to fail
- fix #845971 - while reading /etc/fstab, mount command returns a device before a directory
- fix #858009 - login doesn't update /var/run/utmp properly
- fix #809449 - Backport inverse tree (-s) option for lsblk and related patches
- fix #809139 - lsblk option -D missing in manpage

* Fri Apr  6 2012 Karel Zak <kzak@redhat.com> 2.17.2-12.7
- fix #740163 - 'fdisk -l' returns confusing output (sfdisk)

* Wed Mar 28 2012 Karel Zak <kzak@redhat.com> 2.17.2-12.6
- fix #785142 - uuidd service not active by default

* Mon Mar  5 2012 Karel Zak <kzak@redhat.com> 2.17.2-12.5
- fix #588419 - Changing the console login timeout
- fix #740163 - 'fdisk -l' returns confusing output
- fix #785142 - uuidd service not active by defaul
- fix #797888 - script does not play well with csh when invoked from within /etc/csh.login

* Thu Sep 15 2011 Karel Zak <kzak@redhat.com> 2.17.2-12.4
- fix CVE-2011-1675 - mount fails to anticipate RLIMIT_FSIZE
- fix CVE-2011-1677 - umount may fail to remove /etc/mtab~ lock file

* Tue Aug 30 2011 Karel Zak <kzak@redhat.com> 2.17.2-12.3
- fix fatal typos in patch for #723546

* Fri Aug 26 2011 Karel Zak <kzak@redhat.com> 2.17.2-12.2
- rename /etc/hushlogin to /etc/hushlogins (#696731)

* Thu Aug 11 2011 Karel Zak <kzak@redhat.com> 2.17.2-12.1
- fix #723546 - Defects revealed by Coverity scan
- fix #723352 - cfdisk cannot read default installer partitioning
- fix #712158 - uid/gid overflow in ipcs
- fix #696959 - wipefs(8) reject partitioned devices
- fix #694648 - document blank line at head of fstab
- fix #684203 - umount fails on inconsistent fstab
- fix #679831 --lines does not work
- fix #679741 - canonicalize swap device
- fix #692119 - include fstrim tool
- fix #675999 - blkid crashes on a server with more than 128 storage devices
- fix #696731 - display failed login attempts
- fix #726092 - Pass host name from agetty to login
- fix #716995 - Remove Deprecation Statement in /etc/udev/rules.d/60-raw.rules
- fix #712808 - uuidd should depend on chkconfig
- fix #723638 - Backport upstream extensions for lsblk (RHEL6.2)

* Fri Mar 11 2011 Karel Zak <kzak@redhat.com> 2.17.2-12
- fix #684037 - improperly used readlink() in util-linux-ng-2.17-lsblk.patch

* Tue Feb 22 2011 Karel Zak <kzak@redhat.com> 2.17.2-11
- fix #678306 - introduce safe variant of uuid_generate_time(), fix locking of counter file
- fix #678378 - util-linux-ng code review

* Tue Feb 15 2011 Karel Zak <kzak@redhat.com> 2.17.2-10
- fix #677569 - lsblk: SIZE integer overflow on large values

* Fri Jan 28 2011 Karel Zak <kzak@redhat.com> 2.17.2-9
- fix CVE-2010-3879 fuse: unprivileged user can unmount arbitrary locations

* Thu Jan 27 2011 Karel Zak <kzak@redhat.com> 2.17.2-8
- fix #619139 - fsck returns zero instead of error code 
- fix #621312 - losetup --help returns 1 (fail) for successful command execution
- fix #651035 - misleading reference to samba-client in mount man page, cifs options
- fix #612325 - RHEL6.0 Beta-1: Add mkfs.ext4 to mkfs man page
- fix #650879 - RHEL6: /usr/bin/column segmentation fault
- fix #626374 - fdisk incorrectly checks alignment for non-512-byte *logical* sectors
- fix #663731 - sfdisk -d and fdisk -l print /dev/dm-<N>
- fix #650953 - wipefs(8) does not erase LUKS
- fix #656453 - libblkid incorrectly revalidated cache entries
- fix #623012 - lscpu return error after offline cpu
- fix #616393 - tmpfs mount fails with 'user' option
- fix #561111 - remount of tmpfs fails on RHEL6 alpha
- fix #624521 - fsck seems to run quasi-serially
- fix #657082 - Add lsblk (list block devices) utility
- fix #625064 - fuse-sshfs mounts cannot be unmounted as user
- fix #615389 - Output of "mount" is missing mapping displays for loop-mounts
- fix #616325 - Include findmnt in util-linux-ng package
- fix #665376 - incorrectly documented the mount "atime" option
- fix #670770 - lscpu does not identify 32bit capability on AMD
- fic #671357 - mount.8 man page update for ext{3,4} options

* Thu Dec  2 2010 Karel Zak <kzak@redhat.com> 2.17.2-7
- fix #644503 - support for _rnetdev mount option missing in RHEL6

* Fri Aug 13 2010 Karel Zak <kzak@redhat.com> 2.17.2-6
- fix #592958 - whole disk raid members to not be identified

* Mon Jul 12 2010 Karel Zak <kzak@redhat.com> 2.17.2-5
- fix #561111 - remount of tmpfs fails on RHEL6 alpha
- fix #612668 - backport fsfreeze from util-linux-ng 2.18
- fix #598631 - shutdown, reboot, halt and C-A-D don't work

* Mon Jun 28 2010 Karel Zak <kzak@redhat.com> 2.17.2-4
- fix #604875 - memory usage in wipefs(8)
- fix #591133 - udev /dev/disk/by-uuid not populated
- fix #602657 - fdisk -l does not show correctly partitions names for FCoE volumes
- fix #591617 - lscpu does not use cpu masks properly

* Fri May 21 2010 Karel Zak <kzak@redhat.com> 2.17.2-3
- fix #592958 - whole disk raid members to not be identified
- fix #594689 - partx infinite loop
- fix #589955 - add command-line interface for libblkid topology support

* Mon May  3 2010 Karel Zak <kzak@redhat.com> 2.17.2-2
- fix #588248 - RHEL6: don't probe for RAIDs on CD-ROMs
- fix #586368 - RHEL6: mdraid assembles incorrectly
- fix #586942 - Add utempter support to "script"
- fix #588298 - RHEL6: improve fdisk(8) move command. 

* Mon Mar 22 2010 Karel Zak <kzak@redhat.com> 2.17.2-1
- upgrade to the bugfix release 2.17.2 (#575722)
  ftp://ftp.kernel.org/pub/linux/utils/util-linux-ng/v2.17/v2.17.2-ReleaseNotes
  ftp://ftp.kernel.org/pub/linux/utils/util-linux-ng/v2.17/v2.17.2-ChangeLog
- remove: util-linux-ng-2.17-blkid-alignment-offset.patch
          util-linux-ng-2.17-blkid-minix.patch
          util-linux-ng-2.17-blkid-tinyflag.patch
- fix #572937 - RHEL6: use microsecond resolution for blkid cache entries

* Wed Mar 10 2010 Karel Zak <kzak@redhat.com> 2.17.1-3
- fix #572121 - RHEL6: reset tiny flag in libblkid
- fix #572122 - RHEL6: blkid (and related) should be a bit more robust

* Wed Mar  3 2010 Karel Zak <kzak@redhat.com> 2.17.1-2
- fix #570135 - RHEL6: libblkid: support alignment_offset=-1

* Tue Feb 23 2010 Karel Zak <kzak@redhat.com> 2.17.1-1
- upgrade to 2.17.1 (bugfix release, #567555)
  ftp://ftp.kernel.org/pub/linux/utils/util-linux-ng/v2.17/v2.17.1-ReleaseNotes
  ftp://ftp.kernel.org/pub/linux/utils/util-linux-ng/v2.17/v2.17.1-ChangeLog
- spec file fixes:
  fix floppyutil URL in specfile
  add missing liceces to License field
  fix mixed-use-of-spaces-and-tabs
- fix #565888 - uuidd initscript lsb compliance
- remove util-linux-ng-2.17-mount-mtabfake.patch (merged upstream)

* Fri Feb  5 2010 Karel Zak <kzak@redhat.com> 2.17-4
- fix #559305 - spurious mount warning when /bin/mount not setuid root

* Mon Feb  1 2010 Karel Zak <kzak@redhat.com> 2.17-3
- fix #533874 - RFE: libblkid should allow the developer to ask for 
  scanning of slow devices (eg. cdroms)

* Wed Jan 13 2010 Steve Grubb <sgrubb@redhat.com> 2.17-2
- Rebuild for new libaudit

* Thu Jan  8 2010 Karel Zak <kzak@redhat.com> 2.17-1
- rebase to the final 2.17
  ftp://ftp.kernel.org/pub/linux/utils/util-linux-ng/v2.17/v2.17-ReleaseNotes
  ftp://ftp.kernel.org/pub/linux/utils/util-linux-ng/v2.17/v2.17-ChangeLog

* Wed Dec 16 2009 Karel Zak <kzak@redhat.com> 2.17-0.7
- fix #427183 - in repair mode, mount gives false information (port from RHEL5)

* Mon Dec 14 2009 Karel Zak <kzak@redhat.com> 2.17-0.6
- minor fixes in spec file (fix URL, add Requires, add LGPLv2+)

* Wed Dec  9 2009 Karel Zak <kzak@redhat.com> 2.17-0.5
- upgrade to 2.17-rc2
  ftp://ftp.kernel.org/pub/linux/utils/util-linux-ng/v2.17/v2.17-rc2-ChangeLog

* Mon Dec  7 2009 Karel Zak <kzak@redhat.com> 2.17-0.4
- add clock.8 man page (manlink to hwclock)
- add --help to mount.tmpfs

* Mon Nov 23 2009 Karel Zak <kzak@redhat.com> 2.17-0.3
- upgrade to 2.17-rc1
  ftp://ftp.kernel.org/pub/linux/utils/util-linux-ng/v2.17/v2.17-rc1-ChangeLog

* Tue Nov 10 2009 Karel Zak <kzak@redhat.com> 2.17-0.2.git10dfc39
- upgrade to pre-release snapshot (official changelog not available yet, see
  http://git.kernel.org/?p=utils/util-linux-ng/util-linux-ng.git for now)

* Mon Oct 19 2009 Karel Zak <kzak@redhat.com> 2.17-0.1.git5e51568
- upgrade to pre-release snapshot (official changelog not available yet, see
  http://git.kernel.org/?p=utils/util-linux-ng/util-linux-ng.git for now)  
- new commands: fallocate, unshare, wipefs
- libblkid supports topology and partitions probing
- remove support for --rmpart[s] from blockdev(8) (util-linux-ng-2.14-blockdev-rmpart.patch)
- merged upstream:
  util-linux-ng-2.14-sfdisk-dump.patch
  util-linux-ng-2.16-blkid-swsuspend.patch
  util-linux-ng-2.16-libblkid-compression.patch
  util-linux-ng-2.16-libblkid-ext2.patch
  util-linux-ng-2.16-switchroot-tty.patch

* Mon Oct  5 2009 Karel Zak <kzak@redhat.com> 2.16-13
- fix spec file

* Fri Oct  2 2009 Karel Zak <kzak@redhat.com> 2.16-12
- release++

* Thu Oct  1 2009 Karel Zak <kzak@redhat.com> 2.16-11
- fix #519237 - bash: cannot set terminal process group (-1): Inappropriate ioctl for device

* Wed Sep 16 2009 Tomas Mraz <tmraz@redhat.com> - 2.16-10
- use password-auth common PAM configuration instead of system-auth and
  drop pam_console.so call from the remote PAM config file

* Mon Sep 14 2009 Karel Zak <kzak@redhat.com> 2.16-9
- fix #522718 - sfdisk -d /dev/xxx | sfdisk --force /dev/yyy fails when LANG is set
- fix typo in swsuspend detection

* Wed Aug 26 2009 Tomas Mraz <tmraz@redhat.com> - 2.16-8
- rebuilt with new audit

* Sun Aug 23 2009 Karel Zak <kzak@redhat.com> 2.16-7
- fix #518572 - blkid requires ext2.ko to be decompressed on installation media

* Thu Aug 13 2009 Karel Zak <kzak@redhat.com> 2.16-5
- fix #513104 - blkid returns no fstype for ext2 device when ext2 module not loaded

* Wed Aug  5 2009 Stepan Kasal <skasal@redhat.com> 2.16-4
- set conflict with versions of e2fsprogs containing fsck

* Thu Jul 30 2009 Karel Zak <kzak@redhat.com> 2.16-3
- remove the mount.conf support (see #214891)

* Mon Jul 27 2009 Karel Zak <kzak@redhat.com> 2.16-2
- fix #214891 - add mount.conf and MTAB_LOCK_DIR= option

* Sat Jul 25 2009 Karel Zak <kzak@redhat.com> 2.16-1
- upgrade to 2.16
  ftp://ftp.kernel.org/pub/linux/utils/util-linux-ng/v2.16/v2.16-ReleaseNotes
- enable built-in libuuid (replacement for the old uuid stuff from e2fsprogs)
- new commands switch_root, uuidgen and uuidd (subpackage)

* Wed Jun 10 2009 Karel Zak <kzak@redhat.com> 2.15.1-1
- upgrade to 2.15.1

* Mon Jun  8 2009 Karel Zak <kzak@redhat.com> 2.15.1-0.2
- set BuildRequires: e2fsprogs-devel
- add Requires: e2fsprogs-devel to libblkid-devel

* Thu Jun  4 2009 Karel Zak <kzak@redhat.com> 2.15.1-0.1
- upgrade to 2.15.1-rc1
  ftp://ftp.kernel.org/pub/linux/utils/util-linux-ng/v2.15/v2.15-ReleaseNotes
  ftp://ftp.kernel.org/pub/linux/utils/util-linux-ng/v2.15/v2.15.1-rc1-ChangeLog 
- merged patches:
  util-linux-ng-2.14-login-remote.patch
  util-linux-ng-2.14-fdisk-4k-I.patch
  util-linux-ng-2.14-fdisk-4k-II.patch
  util-linux-ng-2.14-fdisk-4k-III.patch
  util-linux-ng-2.14-dmesg-r.patch
  util-linux-ng-2.14-flock-segfaults.patch
  util-linux-ng-2.14-renice-n.patch
- new commands: lscpu, ipcmk
- remove support for "managed" and "kudzu" mount options
- cleanup spec file
- enable built-in libblkid (replacement for the old blkid from e2fsprogs)

* Thu Apr  2 2009 Karel Zak <kzak@redhat.com> 2.14.2-8
- fix #490769 - post scriptlet failed (thanks to Dan Horak)
 
* Fri Mar 20 2009 Karel Zak <kzak@redhat.com> 2.14.2-7
- fix some nits in mount.tmpfs

* Fri Mar 20 2009 Karel Zak <kzak@redhat.com> 2.14.2-6
- fix #491175 - mount of tmpfs FSs fail at boot

* Thu Mar 19 2009 Karel Zak <kzak@redhat.com> 2.14.2-5
- fix #489672 - flock segfaults when file name is not given (upstream)
- fix #476964 - Mount /var/tmp with tmpfs creates denials
- fix #487227 - fdisk 4KiB hw sectors support (upstream)
- fix #477303 - renice doesn't support -n option (upstream)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Karel Zak <kzak@redhat.com> 2.14.2-3
- add -r option to dmesg(1)

* Mon Feb  9 2009 Karel Zak <kzak@redhat.com> 2.14.2-2
- fix typo in spec file

* Mon Feb  9 2009 Karel Zak <kzak@redhat.com> 2.14.2-1
- upgrade to stable 2.14.2
  ftp://ftp.kernel.org/pub/linux/utils/util-linux-ng/v2.14/v2.14.2-ReleaseNotes

* Thu Jan 22 2009 Karel Zak <kzak@redhat.com> 2.14.2-0.2
- fix #480413 - util-linux-ng doesn't include scriptreplay
- fix #479002 - remove dependency on ConsoleKit-libs
- upgrade to 2.14.2-rc2

* Mon Dec 22 2008 Karel Zak <kzak@redhat.com> 2.14.2-0.1
- upgrade to 2.14.2-rc1
- refresh old patches

* Fri Nov 21 2008 Karel Zak <kzak@redhat.com> 2.14.1-5
- fix #472502 - problem with fdisk and use +sectors for the end of partition

* Mon Oct  6 2008 Karel Zak <kzak@redhat.com> 2.14.1-3
- fix #465761 -  mount manpage is missing uid/gid mount options for tmpfs
- refresh util-linux-ng-2.14-mount-file_t.patch (fuzz=0)

* Wed Sep 10 2008 Karel Zak <kzak@redhat.com> 2.14.1-2
- remove obsolete pam-console support

* Wed Sep 10 2008 Karel Zak <kzak@redhat.com> 2.14.1-1
- upgrade to stable 2.14.1

* Thu Aug 14 2008 Karel Zak <kzak@redhat.com> 2.14.1-0.1
- upgrade to 2.14.1-rc1
- refresh old patches

* Thu Jul 24 2008 Karel Zak <kzak@redhat.com> 2.14-3
- update util-linux-ng-2.14-mount-file_t.patch to make
  the SELinux warning optional (verbose mode is required)

* Tue Jul  1 2008 Karel Zak <kzak@redhat.com> 2.14-2
- fix #390691 - mount should check selinux context on mount, and warn on file_t

* Mon Jun  9 2008 Karel Zak <kzak@redhat.com> 2.14-1
- upgrade to stable util-linux-ng release

* Mon May 19 2008 Karel Zak <kzak@redhat.com> 2.14-0.1
- upgrade to 2.14-rc3
- remove arch(8) (deprecated in favor of uname(1) or arch(1) from coreutils)
- add a new command ldattach(8)
- cfdisk(8) linked with libncursesw

* Tue Apr 22 2008 Karel Zak <kzak@redhat.com> 2.13.1-9
- fix audit log injection attack via login

* Thu Apr 17 2008 Karel Zak <kzak@redhat.com> 2.13.1-8
- fix location of the command raw(8)

* Tue Apr 15 2008 Karel Zak <kzak@redhat.com> 2.13.1-7
- fix 244383 - libblkid uses TYPE="swsuspend" for S1SUSPEND/S2SUSPEND

* Wed Apr  2 2008 Karel Zak <kzak@redhat.com> 2.13.1-6
- fix 439984 - backport mkswap -U

* Wed Mar 26 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.13.1-5
- clean up sparc conditionals

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.13.1-4
- Autorebuild for GCC 4.3

* Mon Jan 28 2008 Karel Zak <kzak@redhat.com> 2.13.1-3
- upgrade to new upstream release
- fix #427874 - util-linux-ng gets "excess command line argument" on update

* Wed Jan  2 2008 Karel Zak <kzak@redhat.com> 2.13.1-2
- update to upstream 2.13.1-rc2

* Wed Dec 12 2007 Dan Walsh <dwalsh@redhat.com> 2.13.1-1
- Fix pam files so that pam_keyinit happens after pam_selinux.so

* Wed Dec 12 2007 Karel Zak <kzak@redhat.com> 2.13.1-0.2
- remove viwp and vigr (in favour of shadow-utils)

* Sun Dec  9 2007 Karel Zak <kzak@redhat.com> 2.13.1-0.1
- update to the latest upstream stable branch
  (commit: fda9d11739ee88c3b2f22a73f12ec019bd3b8335)

* Wed Oct 31 2007 Karel Zak <kzak@redhat.com> 2.13-4
- fix #354791 - blockdev command calls the blkpg ioctl with a wrong data structure

* Tue Oct 16 2007 Karel Zak <kzak@redhat.com> 2.13-3
- fix mount -L | -U segfault
- fix script die on SIGWINCH

* Thu Oct  4 2007 Karel Zak <kzak@redhat.com> 2.13-2
- update to the latest upstream stable branch

* Tue Aug 28 2007 Karel Zak <kzak@redhat.com> 2.13-1
- upgrade to stable util-linux-ng release

* Fri Aug 24 2007 Karel Zak <kzak@redhat.com> 2.13-0.59
- add release number to util-linux Provides and increment setarch Obsoletes
- fix #254114 - spec typo
- upgrade to floppy-0.16
- add BuildRequires: popt-devel

* Wed Aug 22 2007 Jesse Keating <jkeating@redhat.com>  2.13-0.58
- Obsolete a sufficiently high enough version of setarch

* Mon Aug 20 2007 Karel Zak <kzak@redhat.com>  2.13-0.57
- fix #253664 - util-linux-ng fails to build on sparc (patch by Dennis Gilmore)
- rebase to new GIT snapshot

* Mon Aug 20 2007 Karel Zak <kzak@redhat.com> 2.13-0.56
- fix obsoletes field

* Mon Aug 20 2007 Karel Zak <kzak@redhat.com> 2.13-0.55
- util-linux-ng includes setarch(1), define relevat Obsoletes+Provides

* Mon Aug 20 2007 Karel Zak <kzak@redhat.com> 2.13-0.54
- port "blockdev --rmpart" patch from util-linux
- use same Provides/Obsoletes setting like in util-linux

* Wed Aug 15 2007 Karel Zak <kzak@redhat.com> 2.13-0.53
- fix #252046 - review Request: util-linux-ng (util-linux replacement)

* Mon Aug 13 2007 Karel Zak <kzak@redhat.com> 2.13-0.52
- rebase to util-linux-ng (new util-linux upstream fork,
		based on util-linux 2.13-pre7)
- more than 70 Fedora/RHEL patches have been merged to upstream code

* Fri Apr  6 2007 Karel Zak <kzak@redhat.com> 2.13-0.51
- fix #150493 - hwclock --systohc sets clock 0.5 seconds slow
- fix #220873 - starting RPC idmapd: Error: RPC MTAB does not exist.
		(added rpc_pipefs to util-linux-2.13-umount-sysfs.patch)
- fix #227903 - mount -f does not work with NFS-mounted

* Sat Mar  3 2007 David Zeuthen <davidz@redhat.com> 2.13-0.50
- include ConsoleKit session module by default (#229172)

* Thu Jan 11 2007 Karel Zak <kzak@redhat.com> 2.13-0.49
- fix #222293 - undocumented partx,addpart, delpart

* Sun Dec 17 2006 Karel Zak <kzak@redhat.com> 2.13-0.48
- fix paths in po/Makefile.in.in

* Fri Dec 15 2006 Karel Zak <kzak@redhat.com> 2.13-0.47
- fix #217240 - namei ignores non-directory components instead of saying "Not a directory"
- fix #217241 - namei enforces symlink limits inconsistently

* Wed Dec 14 2006 Karel Zak <kzak@redhat.com> 2.13-0.46
- fix leaking file descriptor in the more command (patch by Steve Grubb)

* Wed Dec 13 2006 Karel Zak <kzak@redhat.com> 2.13-0.45
- use ncurses only
- fix #218915 - fdisk -b 4K
- upgrade to -pre7 release
- fix building problem with raw0 patch
- fix #217186 - /bin/sh: @MKINSTALLDIRS@: No such file or directory 
  (port po/Makefile.in.in from gettext-0.16)
- sync with FC6 and RHEL5:
- fix #216489 - SCHED_BATCH option missing in chrt
- fix #216712 - issues with raw device support ("raw0" is wrong device name)
- fix #216760 - mount with context or fscontext option fails
  (temporarily disabled the support for additional contexts -- not supported by kernel yet)
- fix #211827 - Can't mount with additional contexts
- fix #213127 - mount --make-unbindable does not work
- fix #211749 - add -r option to losetup to create a read-only loop

* Thu Oct 12 2006 Karel Zak <kzak@redhat.com> 2.13-0.44
- fix #209911 - losetup.8 updated (use dm-crypt rather than deprecated cryptoloop)
- fix #210338 - spurious error from '/bin/login -h $PHONENUMBER' (bug in IPv6 patch)
- fix #208634 - mkswap "works" without warning on a mounted device

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 2.13-0.43
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Wed Sep 20 2006 Karel Zak <kzak@redhat.com> 2.13-0.42
- remove obsolete NFS code and patches (we use /sbin/mount.nfs
  and /sbin/umount.nfs from nfs-utils now)
- move nfs.5 to nfs-utils

* Fri Sep 15 2006 Karel Zak <kzak@redhat.com> 2.13-0.41
- fix #205038 - mount not allowing sloppy option (exports "-s"
  to external /sbin/mount.nfs(4) calls) 
- fix minor bug in util-linux-2.13-mount-twiceloop.patch
- fix #188193- util-linux should provide plugin infrastructure for HAL

* Mon Aug 21 2006 Karel Zak <kzak@redhat.com> 2.13-0.40
- fix Makefile.am in util-linux-2.13-mount-context.patch
- fix #201343 - pam_securetty requires known user to work
		(split PAM login configuration to two files)
- fix #203358 - change location of taskset binary to allow for early affinity work

* Fri Aug 11 2006 Karel Zak <kzak@redhat.com> 2.13-0.39
- fix #199745 - non-existant simpleinit(8) mentioned in ctrlaltdel(8)

* Thu Aug 10 2006 Dan Walsh <dwalsh@redhat.com> 2.13-0.38
- Change keycreate line to happen after pam_selinux open call so it gets correct context

* Thu Aug 10 2006 Karel Zak <kzak@redhat.com> 2.13-0.37
- fix #176494 - last -i returns strange IP addresses (patch by Bill Nottingham)

* Thu Jul 27 2006 Karel Zak <kzak@redhat.com> 2.13-0.36
- fix #198300, #199557 - util-linux "post" scriptlet failure

* Thu Jul 27 2006 Steve Dickson <steved@redhat.com> 2.13-0.35
- Added the -o fsc flag to nfsmount.

* Wed Jul 26 2006 Karel Zak <kzak@redhat.com> 2.13-0.34
- rebuild

* Tue Jul 18 2006 Karel Zak <kzak@redhat.com> 2.13-0.33
- add Requires(post): libselinux

* Mon Jul 17 2006 Karel Zak <kzak@redhat.com> 2.13-0.32
- add IPv6 support to the login command (patch by Milan Zazrivec)
- fix #198626 - add keyinit instructions to the login PAM script 
  (patch by David Howells) 

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.13-0.31.1
- rebuild

* Tue Jul 11 2006 Karel Zak <kzak@redhat.com> 2.13-0.31
- cleanup dependences for post and preun scriptlets

* Mon Jul 10 2006 Karsten Hopp <karsten@redhat.de> 2.13-0.30
- silence install in minimal buildroot without /var/log

* Fri Jul  7 2006 Karel Zak <kzak@redhat.com> 2.13-0.29 
- include the raw command for RHELs

* Mon Jun 26 2006 Florian La Roche <laroche@redhat.com> 2.13-0.28
- move install-info parts from postun to preun

* Wed Jun 21 2006 Dan Walsh <dwalsh@RedHat.com> 2.13-0.27
- Only execute chcon on machines with selinux enabled

* Wed Jun 14 2006 Steve Dickson <steved@redhat.com> 2.13-0.26
- Remove unneeded header files from nfsmount.c

* Mon Jun 12 2006 Karel Zak <kzak@redhat.com> 2.13-0.25
- fix #187014 - umount segfaults for normal user
- fix #183446 - cal not UTF-8-aware
- fix #186915 - mount does not translate SELIinux context options though libselinux
- fix #185500 - Need man page entry for -o context= mount option
- fix #152579 - missing info about /etc/mtab and /proc/mounts mismatch
- fix #183890 - missing info about possible ioctl() and fcntl() problems on NFS filesystem
- fix #191230 - using mount --move results in wrong data in /etc/mtab
- added mount subtrees support
- fdisk: wrong number of sectors for large disks (suse#160822)
- merge fdisk-xvd (#182553) with new fdisk-isfull (#188981) patch 
- fix #181549 - raw(8) manpage has old information about dd
- remove asm/page.h usage

* Wed May 24 2006 Dan Walsh <dwalsh@RedHat.com> 2.13-0.24
- Remove requirement on restorecon, since we can do the same thing
- with chcon/matchpathcon, and not add requirement on policycoreutils

* Wed May 24 2006 Steve Dickson <steved@redhat.com> 2.13-0.23
- Fixed bug in patch for bz183713 which cause nfs4 mounts to fail.

* Tue May  2 2006 Steve Dickson <steved@redhat.com> 2.13-0.22
- Added syslog logging to background mounts as suggested
  by a customer.

* Mon May  1 2006 Steve Dickson <steved@redhat.com> 2.13-0.21
- fix #183713 - foreground mounts are not retrying as advertised
- fix #151549 - Added 'noacl' mount flag
- fix #169042 - Changed nfsmount to try udp before using tcp when rpc-ing
		the remote rpc.mountd (iff -o tcp is not specified).
		This drastically increases the total number of tcp mounts
		that can happen at once (ala autofs).

* Wed Mar  9 2006 Jesse Keating <jkeating@redhat.com> 2.13-0.20
- Better calling of restorecon as suggested by Bill Nottingham
- prereq restorecon to avoid ordering issues

* Wed Mar  9 2006 Jesse Keating <jkeating@redhat.com> 2.13-0.19
- restorecon /var/log/lastlog

* Wed Mar  8 2006 Karel Zak <kzak@redhat.com> 2.13-0.17
- fix #181782 - mkswap selinux relabeling (fix util-linux-2.13-mkswap-selinux.patch)

* Wed Feb 22 2006 Karel Zak <kzak@redhat.com> 2.13-0.16
- fix #181782 - mkswap should automatically add selinux label to swapfile
- fix #180730 - col is exiting with 1 (fix util-linux-2.12p-col-EILSEQ.patch)
- fix #181896 - broken example in schedutils man pages
- fix #177331 - login omits pam_acct_mgmt & pam_chauthtok when authentication is skipped.
- fix #177523 - umount -a should not unmount sysfs
- fix #182553 - fdisk -l inside xen guest shows no disks

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.13-0.15.1
- bump again for double-long bug on ppc(64)

* Wed Feb  8 2006 Peter Jones <pjones@redhat.com> 2.13-0.15
- add "blockdev --rmpart N <device>" and "blockdev --rmparts <device>"

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.13-0.14.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Thu Jan 19 2006 Steve Dickson <steved@redhat.com> 2.13-0.14
- Updated the gssd_check() and idmapd_check(), used with
  nfsv4 mounts, to looked for the correct file in /var/lock/subsys
  which stops bogus warnings. 

* Tue Jan  3 2006 Karel Zak <kzak@redhat.com> 2.13-0.13
- fix #174676 - hwclock audit return code mismatch
- fix #176441: col truncates data
- fix #174111 - mount allows loopback devices to be mounted more than once to the same mount point
- better wide chars usage in the cal command (based on the old 'moremisc' patch)

* Mon Dec 12 2005 Karel Zak <kzak@redhat.com> 2.13-0.12
- rebuilt

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 25 2005 Karel Zak <kzak@redhat.com> 2.13-0.11.pre6
- update to upstream version 2.13-pre6
- fix #172203 - mount man page in RHEL4 lacks any info on cifs mount options

* Mon Nov  7 2005 Karel Zak <kzak@redhat.com> 2.13-0.10.pre5
- fix #171337 - mkfs.cramfs doesn't work correctly with empty files

* Fri Oct 28 2005 Karel Zak <kzak@redhat.com> 2.13-0.9.pre5
- rebuild

* Wed Oct 26 2005 Karel Zak <kzak@redhat.com> 2.13-0.8.pre5
- updated version of the patch for hwclock audit

* Thu Oct 20 2005 Karel Zak <kzak@redhat.com> 2.13-0.7.pre5
- fix #171337 - mkfs.cramfs dies creating installer image

* Thu Oct 20 2005 Karel Zak <kzak@redhat.com> 2.13-0.6.pre5
- update to upstream 2.13pre5
- remove separated cramfs1.1 (already in upstream package)
- remove odd symlink /usr/bin/mkcramfs -> ../../sbin/mkfs.cramfs
- fix #170171 - ipcs -lm always report "max total shared memory (kbytes) = 0"

* Mon Oct 17 2005 Karel Zak <kzak@redhat.com> 2.13-0.5.pre4
* fix #170564 - add audit message to login

* Fri Oct  7 2005 Karel Zak <kzak@redhat.com> 2.13-0.4.pre4
- fix #169628 - /usr/bin/floppy doesn't work with /dev/fd0
- fix #168436 - login will attempt to run if it has no read/write access to its terminal
- fix #168434 - login's timeout can fail - needs to call siginterrupt(SIGALRM,1)
- fix #165253 - losetup missing option -a [new feature]
- update PAM files (replace pam_stack with new "include" PAM directive)
- remove kbdrate from src.rpm
- update to 2.13pre4

* Fri Oct  7 2005 Steve Dickson <steved@redhat.com> 2.13-0.3.pre3
- fix #170110 - Documentation for 'rsize' and 'wsize' NFS mount options
		is misleading

* Fri Sep  2 2005 Karel Zak <kzak@redhat.com> 2.13-0.3.pre2
- fix #166923 - hwclock will not run on a non audit-enabled kernel
- fix #159410 - mkswap(8) claims max swap area size is 2 GB
- fix #165863 - swsusp swaps should be reinitialized
- change /var/log/lastlog perms to 0644

* Tue Aug 16 2005 Karel Zak <kzak@redhat.com> 2.13-0.2.pre2
- /usr/share/misc/getopt/* -move-> /usr/share/doc/util-linux-2.13/getopt-*
- the arch command marked as deprecated
- removed: elvtune, rescuept and setfdprm
- removed: man8/sln.8 (moved to man-pages, see #10601)
- removed REDAME.pg and README.reset
- .spec file cleanup
- added schedutils (commands: chrt, ionice and taskset)

* Tue Jul 12 2005 Karel Zak <kzak@redhat.com> 2.12p-9.7
- fix #159339 - util-linux updates for new audit system
- fix #158737 - sfdisk warning for large partitions, gpt
- fix #150912 - Add ocfs2 support
- NULL is better than zero at end of execl()

* Thu Jun 16 2005 Karel Zak <kzak@redhat.com> 2.12p-9.5
- fix #157656 - CRM 546998: Possible bug in vipw, changes permissions of /etc/shadow and /etc/gshadow
- fix #159339 - util-linux updates for new audit system (pam_loginuid.so added to util-linux-selinux.pamd)
- fix #159418 - sfdisk unusable - crashes immediately on invocation
- fix #157674 - sync option on VFAT mount destroys flash drives
- fix .spec file /usr/sbin/{hwclock,clock} symlinks

* Wed May  4 2005 Jeremy Katz <katzj@redhat.com> - 2.12p-9.3
- rebuild against new libe2fsprogs (and libblkid) to fix cramfs auto-detection

* Mon May  2 2005 Karel Zak <kzak@redhat.com> 2.12p-9.2
- rebuild

* Mon May  2 2005 Karel Zak <kzak@redhat.com> 2.12p-9
- fix #156597 - look - doesn't work with separators

* Mon Apr 25 2005 Karel Zak <kzak@redhat.com> 2.12p-8
- fix #154498 - util-linux login & pam session
- fix #155293 - man 5 nfs should include vers as a mount option
- fix #76467 - At boot time, fsck chokes on LVs listed by label in fstab
- new Source URL
- added note about ATAPI IDE floppy to fdformat.8
- fix #145355 - Man pages for fstab and fstab-sync in conflict

* Tue Apr  5 2005 Karel Zak <kzak@redhat.com> 2.12p-7
- enable build with libblkid from e2fsprogs-devel
- remove workaround for duplicated labels

* Thu Mar 31 2005 Steve Dickson <SteveD@RedHat.com> 2.12p-5
- Fixed nfs mount to rollback correctly.

* Fri Mar 25 2005 Karel Zak <kzak@redhat.com> 2.12p-4
- added /var/log/lastlog to util-linux (#151635)
- disabled 'newgrp' in util-linux (enabled in shadow-utils) (#149997, #151613)
- improved mtab lock (#143118)
- fixed ipcs typo (#151156)
- implemented mount workaround for duplicated labels (#116300)

* Wed Mar 16 2005 Elliot Lee <sopwith@redhat.com> 2.12p-3
- rebuilt

* Fri Feb 25 2005 Steve Dickson <SteveD@RedHat.com> 2.12p-2
- Changed nfsmount to only use reserve ports when necessary
  (bz# 141773) 

* Thu Dec 23 2004 Elliot Lee <sopwith@redhat.com> 2.12p-1
- Update to util-linux-2.12p. This changes swap header format
  from - you may need to rerun mkswap if you did a clean install of
  FC3.

* Fri Dec 10 2004 Elliot Lee <sopwith@redhat.com> 2.12j-1
- Update to util-linux-2.12j

* Tue Dec  7 2004 Steve Dickson <SteveD@RedHat.com> 2.12a-20
- Corrected a buffer overflow problem with nfs mounts.
  (bz# 141733) 

* Wed Dec 01 2004 Elliot Lee <sopwith@redhat.com> 2.12a-19
- Patches for various bugs.

* Mon Nov 29 2004 Steve Dickson <SteveD@RedHat.com> 2.12a-18
- Made NFS mounts adhere to the IP protocol if specified on
  command line as well as made NFS umounts adhere to the
  current IP protocol. Fix #140016

* Thu Oct 14 2004 Elliot Lee <sopwith@redhat.com> 2.12a-16
- Add include_raw macro, build with it off for Fedora

* Wed Oct 13 2004 Stephen C. Tweedie <sct@redhat.com> - 2.12a-15
- Add raw patch to allow binding of devices not yet in /dev

* Wed Oct 13 2004 John (J5) Palmieri <johnp@redhat.com> 2.12a-14
- Add David Zeuthen's patch to enable the pamconsole flag #133941

* Wed Oct 13 2004 Stephen C. Tweedie <sct@redhat.com> 2.12a-13
- Restore raw utils (bugzilla #130016)

* Mon Oct 11 2004 Phil Knirsch <pknirsch@redhat.com> 2.12a-12
- Add the missing remote entry in pam.d

* Wed Oct  6 2004 Steve Dickson <SteveD@RedHat.com>
- Rechecked in some missing NFS mounting code.

* Wed Sep 29 2004 Elliot Lee <sopwith@redhat.com> 2.12a-10
- Make swaplabel support work with swapon -a -e

* Tue Sep 28 2004 Steve Dickson <SteveD@RedHat.com>
- Updated the NFS and NFS4 code to the latest CITI patch set
  (in which they incorporate a number of our local patches).

* Wed Sep 15 2004 Nalin Dahybhai <nalin@redhat.com> 2.12a-8
- Fix #132196 - turn on SELinux support at build-time.

* Wed Sep 15 2004 Phil Knirsch <pknirsch@redhat.com> 2.12a-7
- Fix #91174 with pamstart.patch

* Tue Aug 31 2004 Elliot Lee <sopwith@redhat.com> 2.12a-6
- Fix #16415, #70616 with rdevman.patch
- Fix #102566 with loginman.patch
- Fix #104321 with rescuept.patch (just use plain lseek - we're in _FILE_OFFSET_BITS=64 land now)
- Fix #130016 - remove raw.
- Re-add agetty (replacing it with mgetty is too much pain, and mgetty is much larger)

* Thu Aug 26 2004 Steve Dickson <SteveD@RedHat.com>
- Made the NFS security checks more explicit to avoid confusion
  (an upstream fix)
- Also removed a compilation warning

* Wed Aug 11 2004 Alasdair Kergon <agk@redhat.com>
- Remove unused mount libdevmapper inclusion.

* Wed Aug 11 2004 Alasdair Kergon <agk@redhat.com>
- Add device-mapper mount-by-label support
- Fix segfault in mount-by-label when a device without a label is present.

* Wed Aug 11 2004 Steve Dickson <SteveD@RedHat.com>
- Updated nfs man page to show that intr are on by
  default for nfs4

* Thu Aug 05 2004 Jindrich Novy <jnovy@redhat.com>
- modified warning causing heart attack for >16 partitions, #107824

* Fri Jul 09 2004 Elliot Lee <sopwith@redhat.com> 2.12a-3
- Fix #126623, #126572
- Patch cleanup
- Remove agetty (use mgetty, agetty is broken)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jun 03 2004 Elliot Lee <sopwith@redhat.com> 2.12a-1
- Update to 2.12a
- Fix #122448

* Thu May 13 2004 Dan Walsh <dwalsh@RedHat.com> 2.12-19
- Change pam_selinux to run last

* Tue May 04 2004 Elliot Lee <sopwith@redhat.com> 2.12-18
- Fix #122448 (autofs issues)

* Fri Apr 23 2004 Elliot Lee <sopwith@redhat.com> 2.12-17
- Fix #119157 by editing the patch
- Add patch145 to fix #119986

* Fri Apr 16 2004 Elliot Lee <sopwith@redhat.com> 2.12-16
- Fix #118803

* Tue Mar 23 2004 Jeremy Katz <katzj@redhat.com> 2.12-15
- mkcramfs: use PAGE_SIZE for default blocksize (#118681)

* Sat Mar 20 2004 <SteveD@RedHat.com>
- Updated the nfs-mount.patch to correctly 
  handle the mounthost option and to ignore 
  servers that do not set auth flavors

* Tue Mar 16 2004 Dan Walsh <dwalsh@RedHat.com> 2.12-13
- Fix selinux ordering or pam for login

* Tue Mar 16 2004 <SteveD@RedHat.com>
- Make RPC error messages displayed with -v argument
- Added two checks to the nfs4 path what will print warnings
  when rpc.idmapd and rpc.gssd are not running
- Ping NFS v4 servers before diving into kernel
- Make v4 mount interruptible which also make the intr option on by default 

* Sun Mar 13 2004  <SteveD@RedHat.com>
- Reworked how the rpc.idmapd and rpc.gssd checks were
  done due to review comments from upstream.
- Added rpc_strerror() so the '-v' flag will show RPC errors.

* Sat Mar 13 2004  <SteveD@RedHat.com>
- Added two checks to the nfs4 path what will print warnings
  when rpc.idmapd and rpc.gssd are not running.

* Thu Mar 11 2004 <SteveD@RedHat.com>
- Reworked and updated the nfsv4 patches.

* Wed Mar 10 2004 Dan Walsh <dwalsh@RedHat.com>
- Bump version

* Wed Mar 10 2004 Steve Dickson <SteveD@RedHat.com>
- Tried to make nfs error message a bit more meaninful
- Cleaned up some warnings

* Sun Mar  7 2004 Steve Dickson <SteveD@RedHat.com> 
- Added pesudo flavors for nfsv4 mounts.
- Added BuildRequires: libselinux-devel and Requires: libselinux
  when WITH_SELINUX is set. 

* Fri Feb 27 2004 Dan Walsh <dwalsh@redhat.com> 2.12-5
- check for 2.6.3 kernel in mount options

* Mon Feb 23 2004 Elliot Lee <sopwith@redhat.com> 2.12-4
- Remove /bin/kill for #116100

* Fri Feb 20 2004 Dan Walsh <dwalsh@redhat.com> 2.12-3
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 12 2004 Elliot Lee <sopwith@redhat.com> 2.12-1
- Final 2.12 has been out for ages - might as well use it.

* Wed Jan 28 2004 Steve Dickson <SteveD@RedHat.com> 2.12pre-4
- Added mount patches that have NFS version 4 support

* Mon Jan 26 2004 Elliot Lee <sopwith@redhat.com> 2.12pre-3
- Provides: mount losetup

* Mon Jan 26 2004 Dan Walsh <dwalsh@redhat.com> 2.12pre-2
- Add multiple to /etc/pam.d/login for SELinux

* Thu Jan 15 2004 Elliot Lee <sopwith@redhat.com> 2.12pre-1
- 2.12pre-1
- Merge mount/losetup packages into the main package (#112324)
- Lose separate 

* Mon Nov 3 2003 Dan Walsh <dwalsh@redhat.com> 2.11y-35.sel
- remove selinux code from login and use pam_selinux

* Thu Oct 30 2003 Dan Walsh <dwalsh@redhat.com> 2.11y-34.sel
- turn on selinux

* Fri Oct 24 2003 Elliot Lee <sopwith@redhat.com> 2.11y-34
- Add BuildRequires: texinfo (from a bug# I don't remember)
- Fix #90588 with mountman patch142.

* Mon Oct 6 2003 Dan Walsh <dwalsh@redhat.com> 2.11y-33
- turn off selinux

* Thu Sep 25 2003 Dan Walsh <dwalsh@redhat.com> 2.11y-32.sel
- turn on selinux
- remove context selection

* Fri Sep 19 2003 Elliot Lee <sopwith@redhat.com> 2.11y-31
- Add patch140 (alldevs) to fix #101772. Printing the total size of
  all devices was deemed a lower priority than having all devices
  (e.g. /dev/ida/c0d9) displayed.

* Fri Sep 12 2003 Dan Walsh <dwalsh@redhat.com> 2.11y-31
- turn off selinux

* Fri Sep 12 2003 Dan Walsh <dwalsh@redhat.com> 2.11y-30.sel
- turn on selinux

* Fri Sep 5 2003 Elliot Lee <sopwith@redhat.com> 2.11y-28
- Fix #103004, #103954

* Fri Sep 5 2003 Dan Walsh <dwalsh@redhat.com> 2.11y-27
- turn off selinux

* Thu Sep 4 2003 Dan Walsh <dwalsh@redhat.com> 2.11y-26.sel
- build with selinux

* Mon Aug 11 2003 Elliot Lee <sopwith@redhat.com> 2.11y-25
- Use urandom instead for mkcramfs

* Tue Jul 29 2003 Dan Walsh <dwalsh@redhat.com> 2.11y-24
- add SELINUX 2.5 support

* Wed Jul 23 2003 Elliot Lee <sopwith@redhat.com> 2.11y-22
- #100433 patch

* Mon Jun 14 2003 Elliot Lee <sopwith@redhat.com> 2.11y-20
- #97381 patch

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Apr 21 2003 Elliot Lee <sopwith@redhat.com> 2.11y-17
- Change patch128 to improve ipcs -l

* Fri Apr 11 2003 Elliot Lee <sopwith@redhat.com> 2.11y-16
- Fix #85407

* Fri Apr 11 2003 Elliot Lee <sopwith@redhat.com> 2.11y-15
- Change patch128 to util-linux-2.11f-ipcs-84243-86285.patch to get all
ipcs fixes

* Thu Apr 10 2003 Matt Wilson <msw@redhat.com> 2.11y-14
- fix last login date display on AMD64 (#88574)

* Mon Apr  7 2003 Jeremy Katz <katzj@redhat.com> 2.11y-13
- include sfdisk on ppc

* Fri Mar 28 2003 Jeremy Katz <katzj@redhat.com> 2.11y-12
- add patch from msw to change mkcramfs blocksize with a command line option

* Tue Mar 25 2003 Phil Knirsch <pknirsch@redhat.com> 2.11y-11
- Fix segfault on s390x due to wrong usage of BLKGETSIZE.

* Thu Mar 13 2003 Elliot Lee <sopwith@redhat.com> 2.11y-10
- Really apply the ipcs patch. Doh.

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 19 2003 Elliot Lee <sopwith@redhat.com> 2.11y-8
- ipcs-84243.patch to fix #84243

* Thu Feb 13 2003 Yukihiro Nakai <ynakai@redhat.com> 2.11y-7
- Update moremisc patch to fix swprintf()'s minimum field (bug #83361).

* Mon Feb 03 2003 Elliot Lee <sopwith@redhat.com> 2.11y-6
- Fix mcookie segfault on many 64-bit architectures (bug #83345).

* Mon Feb 03 2003 Tim Waugh <twaugh@redhat.com> 2.11y-5
- Fix underlined multibyte characters (bug #83376).

* Sun Feb 02 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- rebuild to have again a s390 rpm
- disable some more apps for mainframe

* Wed Jan 29 2003 Elliot Lee <sopwith@redhat.com> 2.11y-4
- util-linux-2.11y-umask-82552.patch

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Jan 13 2003 Elliot Lee <sopwith@redhat.com> 2.11y-2
- Fix #81069, #75421

* Mon Jan 13 2003 Elliot Lee <sopwith@redhat.com> 2.11y-1
- Update to 2.11y
- Fix #80953
- Update patch0, patch107, patch117, patch120 for 2.11y
- Remove patch60, patch61, patch207, patch211, patch212, patch119, patch121
- Remove patch122, patch200

* Wed Oct 30 2002 Elliot Lee <sopwith@redhat.com> 2.11w-2
- Remove some crack/unnecessary patches while submitting stuff upstream.
- Build with -D_FILE_OFFSET_BITS=64

* Tue Oct 29 2002 Elliot Lee <sopwith@redhat.com> 2.11w-1
- Update to 2.11w, resolve patch conflicts

* Tue Oct 08 2002 Phil Knirsch <pknirsch@redhat.com> 2.11r-10hammer.3
- Extended util-linux-2.11b-s390x patch to work again.

* Thu Oct 03 2002 Elliot Lee <sopwith@redhat.com> 2.11r-10hammer.2
- Add patch122 for hwclock on x86_64

* Thu Sep 12 2002 Than Ngo <than@redhat.com> 2.11r-10hammer.1
- Fixed pam config files

* Wed Sep 11 2002 Bernhard Rosenkraenzer <bero@redhat.com> 2.11r-10hammer
- Port to hammer

* Fri Aug 30 2002 Elliot Lee <sopwith@redhat.com> 2.11r-10
- Patch120 (hwclock) to fix #72140
- Include isosize util

* Wed Aug 7 2002  Elliot Lee <sopwith@redhat.com> 2.11r-9
- Patch120 (skipraid2) to fix #70353, because the original patch was 
totally useless.

* Fri Aug 2 2002  Elliot Lee <sopwith@redhat.com> 2.11r-8
- Patch119 (fdisk-add-primary) from #67898

* Wed Jul 24 2002 Elliot Lee <sopwith@redhat.com> 2.11r-7
- Really add the gptsize patch, instead of what I think the patch says.
(+1)

* Tue Jul 23 2002 Elliot Lee <sopwith@redhat.com> 2.11r-6
- Add the sp[n].size part of the patch from #69603

* Mon Jul 22 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- adjust mainframe patches

* Tue Jul  2 2002 Bill Nottingham <notting@redhat.com> 2.11r-4
- only require usermode if we're shipping kbdrate here

* Fri Jun 28 2002 Trond Eivind Glomsrod <teg@redhat.com> 2.11r-3
- Port the large swap patch to new util-linux... the off_t changes 
  now in main aren't sufficient

* Thu Jun 27 2002 Elliot Lee <sopwith@redhat.com> 2.11r-2
- Remove swapondetect (patch301) until it avoids possible false positives.

* Thu Jun 27 2002 Elliot Lee <sopwith@redhat.com> 2.11r-1
- Update to 2.11r, wheeee
- Remove unused patches

* Thu Jun 27 2002 Elliot Lee <sopwith@redhat.com> 2.11n-19
- Make a note here that this package was the source of the single change 
contained in util-linux-2.11f-18 (in 7.2/Alpha), and also contains the 
rawman patch from util-linux-2.11f-17.1 (in 2.1AS).
- Package has no runtime deps on slang, so remove the BuildRequires: 
slang-devel.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jun 20 2002 Elliot Lee <sopwith@redhat.com> 2.11n-17
- Fix teg's swapondetect patch to not print out the usage message when 
'swapon -a -e' is run. (#66690) (edit existing patch)
- Apply hjl's utmp handling patch (#66950) (patch116)
- Fix fdisk man page notes on IDE disk partition limit (#64013) (patch117)
- Fix mount.8 man page notes on vfat shortname option (#65628) (patch117)
- Fix possible cal overflow with widechars (#67090) (patch117)

* Tue Jun 11 2002 Trond Eivind Glomsrod <teg@redhat.com> 2.11n-16
- support large swap partitions
- add '-d' option to autodetect available swap partitions

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed May 15 2002 Elliot Lee <sopwith@redhat.com> 2.11n-14
- Remove kbdrate (again).

* Mon Apr 29 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- adjust mainframe patches to apply to current rpm
- do not include fdisk until it is fixed to work on mainframe

* Mon Apr 01 2002 Elliot Lee <sopwith@redhat.com> 2.11n-12
- Don't strip binaries - rpm does it for us.

* Sun Mar 31 2002 Elliot Lee <sopwith@redhat.com> 2.11n-11
- Apply patch115 from ejb@ql.org for bug #61868

* Wed Mar 27 2002 Elliot Lee <sopwith@redhat.com> 2.11n-10
- Finish fixing #60675 (ipcrm man page), updated the patch.
- Fix #61203 (patch114 - dumboctal.patch).

* Tue Mar 12 2002 Elliot Lee <sopwith@redhat.com> 2.11n-9
- Update ctty3 patch to ignore SIGHUP while dropping controlling terminal

* Fri Mar 08 2002 Elliot Lee <sopwith@redhat.com> 2.11n-8
- Update ctty3 patch to drop controlling terminal before forking.

* Fri Mar 08 2002 Elliot Lee <sopwith@redhat.com> 2.11n-7
  Fix various bugs:
- Add patch110 (skipraid) to properly skip devices that are part of a RAID array.
- Add patch111 (mkfsman) to update the mkfs man page's "SEE ALSO" section.
- remove README.cfdisk
- Include partx
- Fix 54741 and related bugs for good(hah!) with patch113 (ctty3)

* Wed Mar 06 2002 Elliot Lee <sopwith@redhat.com> 2.11n-6
- Put kbdrate in, add usermode dep.

* Tue Feb 26 2002 Elliot Lee <sopwith@redhat.com> 2.11n-5
- Fix #60363 (tweak raw.8 man page, make rawdevices.8 symlink).

* Tue Jan 28 2002 Bill Nottingham <notting@redhat.com> 2.11n-4
- remove kbdrate (fixes kbd conflict)

* Fri Dec 28 2001 Elliot Lee <sopwith@redhat.com> 2.11n-3
- Add util-linux-2.11n-ownerumount.patch (#56593)
- Add patch102 (util-linux-2.11n-colrm.patch) to fix #51887
- Fix #53452 nits.
- Fix #56953 (remove tunelp on s390)
- Fix #56459, and in addition switch to using sed instead of perl.
- Fix #58471
- Fix #57300
- Fix #37436
- Fix #32132

* Wed Dec 26 2001 Elliot Lee <sopwith@redhat.com> 2.11n-1
- Update to 2.11n
- Merge mount/losetup back in.

* Tue Dec 04 2001 Elliot Lee <sopwith@redhat.com> 2.11f-17
- Add patch38 (util-linux-2.11f-ctty2.patch) to ignore SIGINT/SIGTERM/SIGQUIT in the parent, so that ^\ won't break things.

* Fri Nov 09 2001 Elliot Lee <sopwith@redhat.com> 2.11f-16
- Merge patches 36, 75, 76, and 77 into patch #37, to attempt resolve all the remaining issues with #54741.

* Wed Oct 24 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add nologin man-page for s390/s390x

* Wed Oct 24 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.11f-14
- Don't build kbdrate on s390/s390x
- Don't make the pivot_root.8 man page executable(!)

* Tue Oct 23 2001 Elliot Lee <sopwith@redhat.com> 2.11f-13
- Patch/idea #76 from HJL, fixes bug #54741 (race condition in login 
acquisition of controlling terminal).

* Thu Oct 11 2001 Bill Nottingham <notting@redhat.com>
- fix permissions problem with vipw & shadow files, again (doh!)

* Tue Oct 09 2001 Erik Troan <ewt@redhat.com>
- added patch from Olaf Kirch to fix possible pwent structure overwriting

* Fri Sep 28 2001 Elliot Lee <sopwith@redhat.com> 2.11f-10
- fdisk patch from arjan

* Sun Aug 26 2001 Elliot Lee <sopwith@redhat.com> 2.11f-9
- Don't include cfdisk, since it appears to be an even bigger pile of junk than fdisk? :)

* Wed Aug  1 2001 Tim Powers <timp@redhat.com>
- don't require usermode

* Mon Jul 30 2001 Elliot Lee <sopwith@redhat.com> 2.11f-7
- Incorporate kbdrate back in.

* Mon Jul 30 2001 Bill Nottingham <notting@redhat.com>
- revert the patch that calls setsid() in login that we had reverted
  locally but got integrated upstream (#46223)

* Tue Jul 24 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- correct s390x patch

* Mon Jul 23 2001 Elliot Lee <sopwith@redhat.com>
- Add my megapatch (various bugs)
- Include pivot_root (#44828)

* Thu Jul 12 2001 Bill Nottingham <notting@redhat.com>
- make shadow files 0400, not 0600

* Wed Jul 11 2001 Bill Nottingham <notting@redhat.com>
- fix permissions problem with vipw & shadow files

* Mon Jun 18 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 2.11f, remove any merged patches
- add s390x patches for somewhat larger swap

* Thu Jun 14 2001 Erik Troan <ewt@redhat.com>
- added --verbose patch to mkcramfs; it's much quieter by default now

* Tue May 22 2001 Erik Troan <ewt@redhat.com>
- removed warning about starting partitions on cylinder 0 -- swap version2
  makes it unnecessary

* Wed May  9 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.11b-2
- Fix up s390x support

* Mon May  7 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.11b-1
- Fix up login for real (a console session should be the controlling tty)
  by reverting to 2.10s code (#36839, #36840, #39237)
- Add man page for agetty (#39287)
- 2.11b, while at it

* Fri Apr 27 2001 Preston Brown <pbrown@redhat.com> 2.11a-4
- /sbin/nologin from OpenBSD added.

* Fri Apr 20 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.11a-3
- Fix up login - exiting immediately even if the password is correct
  is not exactly a nice feature.
- Make definite plans to kill people who update login without checking
  if the new version works ;)

* Tue Apr 17 2001 Erik Troan <ewt@redhat.com>
- upgraded to 2.11a (kbdrate moved to kbd, among other things)
- turned off ALLOW_VCS_USE
- modified mkcramfs to not use a large number of file descriptors
- include mkfs.bfs

* Sun Apr  8 2001 Matt Wilson <msw@redhat.com>
- changed Requires: kernel >= 2.2.12-7 to Conflicts: kernel < 2.2.12-7
  (fixes a initscripts -> util-linux -> kernel -> initscripts prereq loop)

* Tue Mar 20 2001 Matt Wilson <msw@redhat.com>
- patched mkcramfs to use the PAGE_SIZE from asm/page.h instead of hard
  coding 4096 (fixes mkcramfs on alpha...)

* Mon Mar 19 2001 Matt Wilson <msw@redhat.com>
- added mkcramfs (from linux/scripts/mkcramfs)

* Mon Feb 26 2001 Tim Powers <timp@redhat.com>
- fixed bug #29131, where ipc.info didn't have an info dir entry,
  added the dir entry to ipc.texi (Patch58)

* Fri Feb 23 2001 Preston Brown <pbrown@redhat.com>
- use lang finder script
- install info files

* Thu Feb 08 2001 Erik Troan <ewt@redhat.com>
- reverted login patch; seems to cause problems
- added agetty

* Wed Feb 07 2001 Erik Troan <ewt@redhat.com>
- updated kill man page
- added patch to fix vipw race
- updated vipw to edit /etc/shadow and /etc/gshadow, if appropriate
- added patch to disassociate login from tty, session, and pgrp

* Tue Feb 06 2001 Erik Troan <ewt@redhat.com>
- fixed problem w/ empty extended partitions
- added patch to fix the date in the more man page
- set OPT to pass optimization flags to make rather then RPM_OPT_FLAG
- fixed fdisk -l /Proc/partitions parsing
- updated to 2.10s

* Tue Jan 23 2001 Preston Brown <pbrown@redhat.com>
- danish translations added

* Mon Jan 15 2001 Nalin Dahyabhai <nalin@redhat.com>
- fix segfault in login in btmp patch (#24025)

* Mon Dec 11 2000 Oliver Paukstadt <oliver.paukstadt@millenux.com>
- ported to s390

* Wed Nov 01 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 2.10p
- update patch37 to newer fdisk version

* Mon Oct  9 2000 Jeff Johnson <jbj@redhat.com>
- update to 2.10o
-  fdformat: fixed to work with kernel 2.4.0test6 (Marek Wojtowicz)
-  login: not installed suid
-  getopt: by default install aux files in /usr/share/misc
- update to 2.10n:
-  added blockdev.8
-  change to elvtune (andrea)
-  fixed overrun in agetty (vii@penguinpowered.com)
-  shutdown: prefer umounting by mount point (rgooch)
-  fdisk: added plan9
-  fdisk: remove empty links in chain of extended partitions
-  hwclock: handle both /dev/rtc and /dev/efirtc (Bill Nottingham)
-  script: added -f (flush) option (Ivan Schreter)
-  script: added -q (quiet) option (Per Andreas Buer)
-  getopt: updated to version 1.1.0 (Frodo Looijaard)
-  Czech messages (Jiri Pavlovsky)
- login.1 man page had not /var/spool/mail path (#16998).
- sln.8 man page (but not executable) included (#10601).
- teach fdisk 0xde(Dell), 0xee(EFI GPT), 0xef(EFI FAT) partitions (#17610).

* Wed Aug 30 2000 Matt Wilson <msw@redhat.com>
- rebuild to cope with glibc locale binary incompatibility, again

* Mon Aug 14 2000 Jeff Johnson <jbj@redhat.com>
- setfdprm should open with O_WRONLY, not 3.

* Fri Aug 11 2000 Jeff Johnson <jbj@redhat.com>
- fdformat should open with O_WRONLY, not 3.

* Fri Jul 21 2000 Nalin Dahyabhai <nalin@redhat.com>
- make 'look' look in /usr/share/dict

* Fri Jul 21 2000 Bill Nottingham <notting@redhat.com>
- put /usr/local/sbin:/usr/local/bin in root's path

* Wed Jul 19 2000 Jakub Jelinek <jakub@redhat.com>
- rebuild to cope with glibc locale binary incompatibility

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jul 10 2000 Bill Nottingham <notting@redhat.com>
- enable hwclock to use /dev/efirtc on ia64 (gettext is fun. :( )

* Mon Jul  3 2000 Bill Nottingham <notting@redhat.com>
- move cfdisk to /usr/sbin, it depends on /usr stuff
- add rescuept

* Fri Jun 23 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- point more at the correct path to vi (for "v"), Bug #10882

* Sun Jun  4 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging changes.

* Thu Jun  1 2000 Nalin Dahyabhai <nalin@redhat.com>
- modify PAM setup to use system-auth

* Mon May  1 2000 Bill Nottingham <notting@redhat.com>
- eek, where did login go? (specfile tweaks)

* Mon Apr 17 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.10k
- fix compilation with current glibc

* Tue Mar 21 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.10h

* Tue Mar  7 2000 Jeff Johnson <jbj@redhat.com>
- rebuild for sparc baud rates > 38400.

* Sat Mar  4 2000 Matt Wilson <msw@redhat.com>
- use snprintf - not sprintf - when doing
  sprintf ("%%s\n", _("Some string")) to avoid overflows and
  segfaults.

* Mon Feb 21 2000 Jeff Johnson <jbj@redhat.com>
- raw control file was /dev/raw, now /dev/rawctl.
- raw access files were /dev/raw*, now /dev/raw/raw*.

* Thu Feb 17 2000 Erik Troan <ewt@redhat.com>
- -v argument to mkswap wasn't working

* Thu Feb 10 2000 Jakub Jelinek <jakub@redhat.com>
- Recognize 0xfd on Sun disklabels as RAID

* Tue Feb  8 2000 Bill Nottingham <notting@redhat.com>
- more lives in /bin, and was linked against /usr/lib/libnurses. Bad.

* Thu Feb 03 2000 Jakub Jelinek <jakub@redhat.com>
- update to 2.10f
- fix issues in the new realpath code, avoid leaking memory

* Tue Feb 01 2000 Cristian Gafton <gafton@redhat.com>
- rebuild to fix dependencies
- add NFSv3 patches

* Fri Jan 28 2000 Bill Nottingham <notting@redhat.com>
- don't require csh

* Mon Jan 24 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 2.10e
- add rename

* Thu Jan 20 2000 Jeff Johnson <jbj@redhat.com>
- strip newlines in logger input.

* Mon Jan 10 2000 Jeff Johnson <jbj@redhat.com>
- rebuild with correct ncurses libs.

* Tue Dec  7 1999 Matt Wilson <msw@redhat.com>
- updated to util-linux 2.10c
- deprecated IMAP login mail notification patch17
- deprecated raw patch22
- depricated readprofile patch24

* Tue Dec  7 1999 Bill Nottingham <notting@redhat.com>
- add patch for readprofile

* Thu Nov 18 1999 Michael K. Johnson <johnsonm@redhat.com>
- tunelp should come from util-linux

* Tue Nov  9 1999 Jakub Jelinek <jakub@redhat.com>
- kbdrate cannot use /dev/port on sparc.

* Wed Nov  3 1999 Jakub Jelinek <jakub@redhat.com>
- fix kbdrate on sparc.

* Wed Oct 27 1999 Bill Nottingham <notting@redhat.com>
- ship hwclock on alpha.

* Tue Oct  5 1999 Bill Nottingham <notting@redhat.com>
- don't ship symlinks to rdev if we don't ship rdev.

* Tue Sep 07 1999 Cristian Gafton <gafton@redhat.com>
- add rawIO support from sct

* Mon Aug 30 1999 Preston Brown <pbrown@redhat.com>
- don't display "new mail" message when the only piece of mail is from IMAP

* Fri Aug 27 1999 Michael K. Johnson <johnsonm@redhat.com>
- kbdrate is now a console program

* Thu Aug 26 1999 Jeff Johnson <jbj@redhat.com>
- hostid is now in sh-utils. On sparc, install hostid as sunhostid (#4581).
- update to 2.9w:
-  Updated mount.8 (Yann Droneaud)
-  Improved makefiles
-  Fixed flaw in fdisk

* Tue Aug 10 1999 Jeff Johnson <jbj@redhat.com>
- tsort is now in textutils.

* Wed Aug  4 1999 Bill Nottingham <notting@redhat.com>
- turn off setuid bit on login. Again. :(

* Tue Aug  3 1999 Peter Jones, <pjones@redhat.com>
- hostid script for sparc (#3803).

* Tue Aug 03 1999 Christian 'Dr. Disk' Hechelmann <drdisk@tc-gruppe.de>
- added locale message catalogs to %%file
- added patch for non-root build
- vigr.8 and /usr/lib/getopt  man-page was missing from file list
- /etc/fdprm really is a config file

* Fri Jul 23 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.9v:
- cfdisk no longer believes the kernel's HDGETGEO
	(and may be able to partition a 2 TB disk)

* Fri Jul 16 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.9u:
- Czech more.help and messages (Jiri Pavlovsky)
- Japanese messages (Daisuke Yamashita)
- fdisk fix (Klaus G. Wagner)
- mount fix (Hirokazu Takahashi)
- agetty: enable hardware flow control (Thorsten Kranzkowski)
- minor cfdisk improvements
- fdisk no longer accepts a default device
- Makefile fix

* Tue Jul  6 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.9t:
- national language support for hwclock
- Japanese messages (both by Daisuke Yamashita)
- German messages and some misc i18n fixes (Elrond)
- Czech messages (Jiri Pavlovsky)
- wall fixed for /dev/pts/xx ttys
- make last and wall use getutent() (Sascha Schumann)
	[Maybe this is bad: last reading all of wtmp may be too slow.
	Revert in case people complain.]
- documented UUID= and LABEL= in fstab.5
- added some partition types
- swapon: warn only if verbose

* Fri Jun 25 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.9s.

* Sat May 29 1999 Jeff Johnson <jbj@redhat.com>
- fix mkswap sets incorrect bits on sparc64 (#3140).

* Thu Apr 15 1999 Jeff Johnson <jbj@redhat.com>
- on sparc64 random ioctls on clock interface cause kernel messages.

* Thu Apr 15 1999 Jeff Johnson <jbj@redhat.com>
- improved raid patch (H.J. Lu).

* Wed Apr 14 1999 Michael K. Johnson <johnsonm@redhat.com>
- added patch for smartraid controllers

* Sat Apr 10 1999 Cristian Gafton <gafton@redhat.com>
- fix logging problems caused by setproctitle and PAM interaction
  (#2045)

* Wed Mar 31 1999 Jeff Johnson <jbj@redhat.com>
- include docs and examples for sfdisk (#1164)

* Mon Mar 29 1999 Matt Wilson <msw@redhat.com>
- rtc is not working properly on alpha, we can't use hwclock yet.

* Fri Mar 26 1999 Cristian Gafton <gafton@redhat.com>
- add patch to make mkswap more 64 bit friendly... Patch from
  eranian@hpl.hp.com (ahem!)

* Thu Mar 25 1999 Jeff Johnson <jbj@redhat.com>
- include sfdisk (#1164)
- fix write (#1784)
- use positive logic in spec file (%%ifarch rather than %ifnarch).
- (re)-use 1st matching utmp slot if search by mypid not found.
- update to 2.9o
- lastb wants bad logins in wtmp clone /var/run/btmp (#884)

* Thu Mar 25 1999 Jakub Jelinek <jj@ultra.linux.cz>
- if hwclock is to be compiled on sparc,
  it must actually work. Also, it should obsolete
  clock, otherwise it clashes.
- limit the swap size in mkswap for 2.2.1+ kernels
  by the actual maximum size kernel can handle.
- fix kbdrate on sparc, patch by J. S. Connell
  <ankh@canuck.gen.nz>

* Wed Mar 24 1999 Matt Wilson <msw@redhat.com>
- added pam_console back into pam.d/login

* Tue Mar 23 1999 Matt Wilson <msw@redhat.com>
- updated to 2.9i
- added hwclock for sparcs and alpha

* Mon Mar 22 1999 Erik Troan <ewt@redhat.com>
- added vigr to file list

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 12)

* Thu Mar 18 1999 Cristian Gafton <gafton@redhat.com>
- remove most of the ifnarch arm stuff

* Mon Mar 15 1999 Michael Johnson <johnsonm@redhat.com>
- added pam_console.so to /etc/pam.d/login

* Thu Feb  4 1999 Michael K. Johnson <johnsonm@redhat.com>
- .perms patch to login to make it retain root in parent process
  for pam_close_session to work correctly

* Tue Jan 12 1999 Jeff Johnson <jbj@redhat.com>
- strip fdisk in buildroot correctly (#718)

* Mon Jan 11 1999 Cristian Gafton <gafton@redhat.com>
- have fdisk compiled on sparc and arm

* Mon Jan 11 1999 Erik Troan <ewt@redhat.com>
- added beos partition type to fdisk

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- incorporate fdisk on all arches

* Sat Dec  5 1998 Jeff Johnson <jbj@redhat.com>
- restore PAM functionality at end of login (Bug #201)

* Thu Dec 03 1998 Cristian Gafton <gafton@redhat.com>
- patch top build on the arm without PAM and related utilities, for now.
- build hwclock only on intel

* Wed Nov 18 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to version 2.9

* Thu Oct 29 1998 Bill Nottingham <notting@redhat.com>
- build for Raw Hide (slang-1.2.2)
- patch kbdrate wackiness so it builds with egcs

* Tue Oct 13 1998 Erik Troan <ewt@redhat.com>
- patched more to use termcap

* Mon Oct 12 1998 Erik Troan <ewt@redhat.com>
- added warning about alpha/bsd label starting cylinder

* Mon Sep 21 1998 Erik Troan <ewt@redhat.com>
- use sigsetjmp/siglongjmp in more rather then sig'less versions

* Fri Sep 11 1998 Jeff Johnson <jbj@redhat.com>
- explicit attrs for setuid/setgid programs

* Thu Aug 27 1998 Cristian Gafton <gafton@redhat.com>
- sln is now included in glibc

* Sun Aug 23 1998 Jeff Johnson <jbj@redhat.com>
- add cbm1581 floppy definitions (problem #787)

* Mon Jun 29 1998 Jeff Johnson <jbj@redhat.com>
- remove /etc/nologin at end of shutdown/halt.

* Fri Jun 19 1998 Jeff Johnson <jbj@redhat.com>
- add mount/losetup.

* Thu Jun 18 1998 Jeff Johnson <jbj@redhat.com>
- update to 2.8 with 2.8b clean up. hostid now defunct?

* Mon Jun 01 1998 David S. Miller <davem@dm.cobaltmicro.com>
- "more" now works properly on sparc

* Sat May 02 1998 Jeff Johnson <jbj@redhat.com>
- Fix "fdisk -l" fault on mounted cdrom. (prob #513)

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat Apr 11 1998 Cristian Gafton <gafton@redhat.com>
- manhattan rebuild

* Mon Dec 29 1997 Erik Troan <ewt@redhat.com>
- more didn't suspend properly on glibc
- use proper tc*() calls rather then ioctl's

* Sun Dec 21 1997 Cristian Gafton <gafton@redhat.com>
- fixed a security problem in chfn and chsh accepting too 
  long gecos fields

* Fri Dec 19 1997 Mike Wangsmo <wanger@redhat.com>
- removed "." from default path

* Tue Dec 02 1997 Cristian Gafton <gafton@redhat.com>
- added (again) the vipw patch

* Wed Oct 22 1997 Michael Fulbright <msf@redhat.com>
- minor cleanups for glibc 2.1

* Fri Oct 17 1997 Michael Fulbright <msf@redhat.com>
- added vfat32 filesystem type to list recognized by fdisk

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- don't build clock on the alpha 
- don't install chkdupexe

* Thu Oct 02 1997 Michael K. Johnson <johnsonm@redhat.com>
- Update to new pam standard.
- BuildRoot.

* Thu Sep 25 1997 Cristian Gafton <gafton@redhat.com>
- added rootok and setproctitle patches
- updated pam config files for chfn and chsh

* Tue Sep 02 1997 Erik Troan <ewt@redhat.com>
- updated MCONFIG to automatically determine the architecture
- added glibc header hacks to fdisk code
- rdev is only available on the intel

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- update to util-linux 2.7, fixed login problems

* Wed Jun 25 1997 Erik Troan <ewt@redhat.com>
- Merged Red Hat changes into main util-linux source, updated package to
  development util-linux (nearly 2.7).

* Tue Apr 22 1997 Michael K. Johnson <johnsonm@redhat.com>
- LOG_AUTH --> LOG_AUTHPRIV in login and shutdown

* Mon Mar 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- Moved to new pam and from pam.conf to pam.d

* Tue Feb 25 1997 Michael K. Johnson <johnsonm@redhat.com>
- pam.patch differentiated between different kinds of bad logins.
  In particular, "user does not exist" and "bad password" were treated
  differently.  This was a minor security hole.
