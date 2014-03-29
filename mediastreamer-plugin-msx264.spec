Summary:	H264 video codec for mediastreamer
Summary(pl.UTF-8):	Kodek obrazu H264 dla mediastreamera
Name:		mediastreamer-plugin-msx264
Version:	1.4.3
Release:	3
License:	GPL v2+
Group:		Libraries
Source0:	http://download-mirror.savannah.gnu.org/releases/linphone/plugins/sources/msx264-%{version}.tar.gz
# Source0-md5:	8e3dad81033631918bb1138548fd9797
URL:		https://github.com/Distrotech/msx264
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	ortp-devel >= 0.16.0
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

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{?with_wb:--enable-wideband}

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
