#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x78A1B4DFE8F9C57E (rousseau@debian.org)
#
Name     : pcsc-lite
Version  : 1.9.3
Release  : 12
URL      : https://pcsclite.apdu.fr/files/pcsc-lite-1.9.3.tar.bz2
Source0  : https://pcsclite.apdu.fr/files/pcsc-lite-1.9.3.tar.bz2
Source1  : https://pcsclite.apdu.fr/files/pcsc-lite-1.9.3.tar.bz2.asc
Summary  : PC/SC smart card interface
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pcsc-lite-autostart = %{version}-%{release}
Requires: pcsc-lite-bin = %{version}-%{release}
Requires: pcsc-lite-lib = %{version}-%{release}
Requires: pcsc-lite-license = %{version}-%{release}
Requires: pcsc-lite-man = %{version}-%{release}
Requires: pcsc-lite-services = %{version}-%{release}
Requires: ccid
BuildRequires : ccid
BuildRequires : flex
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libusb-1.0)

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
Requires: pcsc-lite-license = %{version}-%{release}
Requires: pcsc-lite-services = %{version}-%{release}

%description bin
bin components for the pcsc-lite package.


%package dev
Summary: dev components for the pcsc-lite package.
Group: Development
Requires: pcsc-lite-lib = %{version}-%{release}
Requires: pcsc-lite-bin = %{version}-%{release}
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

%description services
services components for the pcsc-lite package.


%prep
%setup -q -n pcsc-lite-1.9.3
cd %{_builddir}/pcsc-lite-1.9.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1628297101
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1628297101
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pcsc-lite
cp %{_builddir}/pcsc-lite-1.9.3/COPYING %{buildroot}/usr/share/package-licenses/pcsc-lite/12f0c48a0be5fb271ccd2f1de671e747c511166f
%make_install
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/sockets.target.wants
ln -s ../pcscd.socket %{buildroot}/usr/lib/systemd/system/sockets.target.wants/pcscd.socket
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/sockets.target.wants/pcscd.socket

%files bin
%defattr(-,root,root,-)
/usr/bin/pcscd

%files dev
%defattr(-,root,root,-)
/usr/include/PCSC/debuglog.h
/usr/include/PCSC/ifdhandler.h
/usr/include/PCSC/pcsclite.h
/usr/include/PCSC/reader.h
/usr/include/PCSC/winscard.h
/usr/include/PCSC/wintypes.h
/usr/lib64/libpcsclite.so
/usr/lib64/pkgconfig/libpcsclite.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/pcsc\-lite/*

%files extras
%defattr(-,root,root,-)
/usr/bin/pcsc-spy
/usr/lib64/libpcscspy.so
/usr/lib64/libpcscspy.so.0
/usr/lib64/libpcscspy.so.0.0.0
/usr/share/man/man1/pcsc-spy.1

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpcsclite.so.1
/usr/lib64/libpcsclite.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pcsc-lite/12f0c48a0be5fb271ccd2f1de671e747c511166f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/reader.conf.5
/usr/share/man/man8/pcscd.8

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/sockets.target.wants/pcscd.socket
/usr/lib/systemd/system/pcscd.service
/usr/lib/systemd/system/pcscd.socket
