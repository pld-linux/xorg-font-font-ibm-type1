# $Rev: 3208 $, $Date: 2005-08-27 17:42:48 $
#
Summary:	font-ibm-type1
Summary(pl):	font-ibm-type1
Name:		xorg-font-font-ibm-type1
Version:	0.99.0
Release:	0.01
License:	MIT
Group:		X11
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/font/font-ibm-type1-%{version}.tar.bz2
# Source0-md5:	c8232bd729fde5a3245e249acbfba444
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-font-font-util
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/font-ibm-type1-%{version}-root-%(id -u -n)

%description
font-ibm-type1

%description -l pl
font-ibm-type1


%prep
%setup -q -n font-ibm-type1-%{version}


%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%{_libdir}/X11/fonts/Type1/*
