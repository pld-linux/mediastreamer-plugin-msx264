Summary:	H264 video codec for mediastreamer
Summary(pl.UTF-8):	Kodek obrazu H264 dla mediastreamera
Name:		mediastreamer-plugin-msx264
Version:	1.5.4
Release:	3
License:	GPL v2+
Group:		Libraries
#Source0Download: https://gitlab.linphone.org/BC/public/msx264/-/tags
Source0:	https://gitlab.linphone.org/BC/public/msx264/-/archive/%{version}/msx264-%{version}.tar.bz2
# Source0-md5:	3829813876f33bd30c50519d66b07c18
Patch0:		msx264-ms2-update.patch
URL:		https://gitlab.linphone.org/BC/public/msx264
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	mediastreamer-devel >= 2.7.0
# ABI 67
BuildRequires:	libx264-devel >= 0.1.3-1.20091001
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(x264) >= 0.67.0
Requires:	libx264 >= 0.1.3-1.20091001
Requires:	mediastreamer >= 2.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package supplies the mediastreamer plugin for the H264 video
codec.

%description -l pl.UTF-8
Ten pakiet udostępnia wtyczkę mediastreamera do kodeka obrazu H264.

%prep
%setup -q -n msx264-%{version}
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-strict

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/mediastreamer/plugins/libmsx264.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/mediastreamer/plugins/libmsx264.so*
