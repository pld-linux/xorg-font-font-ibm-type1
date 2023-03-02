Summary:	IBM Courier font in Type1 format
Summary(pl.UTF-8):	Font IBM Courier w formacie Type1
Name:		xorg-font-font-ibm-type1
Version:	1.0.4
Release:	1
License:	distributable (see COPYING)
Group:		Fonts
Source0:	https://xorg.freedesktop.org/releases/individual/font/font-ibm-type1-%{version}.tar.xz
# Source0-md5:	00f64a84b6c9886040241e081347a853
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	fontconfig
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	t1utils
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.2
BuildRequires:	xorg-util-util-macros >= 1.20
BuildRequires:	xz
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/Type1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IBM Courier font in Type1 format.

%description -l pl.UTF-8
Font IBM Courier w formacie Type1.

%prep
%setup -q -n font-ibm-type1-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%if "%{_gnu}" != "-gnux32"
	--build=%{_host} \
	--host=%{_host} \
%endif
	--with-fontdir=%{_fontsdir}/Type1

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# separate *.afm, convert *.pfa to .pfb
cd $RPM_BUILD_ROOT%{_fontsdir}/Type1
install -d afm
%{__mv} *.afm afm
for f in *.pfa ; do
	t1binary $f `basename $f .pfa`.pfb
	rm -f $f
done
sed -e '1d;s/\.pfa /.pfb /' fonts.scale > fonts.scale.ibm
%{__rm} fonts.scale fonts.dir

cat > Fontmap.ibm <<EOF
/Courier                                 (cour.pfb)     ;
/Courier-Bold                            (courb.pfb)    ;
/Courier-BoldItalic                      (courbi.pfb)   ;
/Courier-Italic                          (couri.pfb)    ;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst Type1

%postun
fontpostinst Type1

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%{_fontsdir}/Type1/cour*.pfb
%{_fontsdir}/Type1/afm/cour*.afm
%{_fontsdir}/Type1/fonts.scale.ibm
%{_fontsdir}/Type1/Fontmap.ibm
