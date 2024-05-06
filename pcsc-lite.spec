#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0x78A1B4DFE8F9C57E (rousseau@debian.org)
#
Name     : pcsc-lite
Version  : 2.2.0
Release  : 21
URL      : https://pcsclite.apdu.fr/files/pcsc-lite-2.2.0.tar.xz
Source0  : https://pcsclite.apdu.fr/files/pcsc-lite-2.2.0.tar.xz
Source1  : https://pcsclite.apdu.fr/files/pcsc-lite-2.2.0.tar.xz.asc
Source2  : 78A1B4DFE8F9C57E.pkey
Summary  : PC/SC smart card interface
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pcsc-lite-autostart = %{version}-%{release}
Requires: pcsc-lite-bin = %{version}-%{release}
Requires: pcsc-lite-data = %{version}-%{release}
Requires: pcsc-lite-lib = %{version}-%{release}
Requires: pcsc-lite-license = %{version}-%{release}
Requires: pcsc-lite-man = %{version}-%{release}
Requires: pcsc-lite-services = %{version}-%{release}
Requires: ccid
BuildRequires : buildreq-meson
BuildRequires : flex
BuildRequires : gnupg
BuildRequires : pkgconfig(libudev)
BuildRequires : polkit-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The purpose of PCSC Lite is to provide a Windows(R) SCard interface in a very
small form factor for communicating to smart cards and readers. PCSC Lite can
be compiled directly to a desired reader driver or can be used to dynamically
allocate/deallocate reader drivers at runtime (default).

%package autostart
Summary: autostart components for the pcsc-lite package.
Group: Default

%description autostart
autostart components for the pcsc-lite package.


%package bin
Summary: bin components for the pcsc-lite package.
Group: Binaries
Requires: pcsc-lite-data = %{version}-%{release}
Requires: pcsc-lite-license = %{version}-%{release}
Requires: pcsc-lite-services = %{version}-%{release}

%description bin
bin components for the pcsc-lite package.


%package data
Summary: data components for the pcsc-lite package.
Group: Data

%description data
data components for the pcsc-lite package.


%package dev
Summary: dev components for the pcsc-lite package.
Group: Development
Requires: pcsc-lite-lib = %{version}-%{release}
Requires: pcsc-lite-bin = %{version}-%{release}
Requires: pcsc-lite-data = %{version}-%{release}
Provides: pcsc-lite-devel = %{version}-%{release}
Requires: pcsc-lite = %{version}-%{release}

%description dev
dev components for the pcsc-lite package.


%package doc
Summary: doc components for the pcsc-lite package.
Group: Documentation
Requires: pcsc-lite-man = %{version}-%{release}

%description doc
doc components for the pcsc-lite package.


%package extras
Summary: extras components for the pcsc-lite package.
Group: Default

%description extras
extras components for the pcsc-lite package.


%package lib
Summary: lib components for the pcsc-lite package.
Group: Libraries
Requires: pcsc-lite-data = %{version}-%{release}
Requires: pcsc-lite-license = %{version}-%{release}

%description lib
lib components for the pcsc-lite package.


%package license
Summary: license components for the pcsc-lite package.
Group: Default

%description license
license components for the pcsc-lite package.


%package man
Summary: man components for the pcsc-lite package.
Group: Default

%description man
man components for the pcsc-lite package.


%package services
Summary: services components for the pcsc-lite package.
Group: Systemd services
Requires: systemd

%description services
services components for the pcsc-lite package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 78A1B4DFE8F9C57E' gpg.status
%setup -q -n pcsc-lite-2.2.0
cd %{_builddir}/pcsc-lite-2.2.0
pushd ..
cp -a pcsc-lite-2.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1715013721
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/pcsc-lite
cp %{_builddir}/pcsc-lite-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pcsc-lite/12f0c48a0be5fb271ccd2f1de671e747c511166f || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/sockets.target.wants
ln -s ../pcscd.socket %{buildroot}/usr/lib/systemd/system/sockets.target.wants/pcscd.socket
mkdir -p %{buildroot}/usr/bin
mv %{buildroot}/sbin %{buildroot}/usr/bin

## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/sockets.target.wants/pcscd.socket

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/pcscd
/usr/bin/sbin/pcscd

%files data
%defattr(-,root,root,-)
/usr/share/polkit-1/actions/org.debian.pcsc-lite.policy

%files dev
%defattr(-,root,root,-)
/usr/include/PCSC/debuglog.h
/usr/include/PCSC/ifdhandler.h
/usr/include/PCSC/pcsclite.h
/usr/include/PCSC/reader.h
/usr/include/PCSC/winscard.h
/usr/include/PCSC/wintypes.h
/usr/lib64/libpcsclite.so
/usr/lib64/libpcsclite_real.so
/usr/lib64/pkgconfig/libpcsclite.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/pcsc\-lite/*

%files extras
%defattr(-,root,root,-)
/V3/usr/lib64/libpcscspy.so.0
/usr/bin/pcsc-spy
/usr/lib64/libpcscspy.so
/usr/lib64/libpcscspy.so.0
/usr/share/man/man1/pcsc-spy.1

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libpcsclite.so.1
/V3/usr/lib64/libpcsclite_real.so.1
/usr/lib64/libpcsclite.so.1
/usr/lib64/libpcsclite_real.so.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pcsc-lite/12f0c48a0be5fb271ccd2f1de671e747c511166f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/pcscd.8

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/sockets.target.wants/pcscd.socket
/usr/lib/systemd/user/pcscd.service
/usr/lib/systemd/user/pcscd.socket
