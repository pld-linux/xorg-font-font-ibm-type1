Summary:	IBM Courier font in Type1 format
Summary(pl.UTF-8):	Font IBM Courier w formacie Type1
Name:		xorg-font-font-ibm-type1
Version:	1.0.2
Release:	1
License:	distributable (see COPYING)
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-ibm-type1-%{version}.tar.bz2
# Source0-md5:	ad4a8b9443f32c29a4e7001a50af17c0
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	fontconfig
BuildRequires:	t1utils
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.1
BuildRequires:	xorg-util-util-macros >= 1.3
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
	--build=%{_host} \
	--host=%{_host} \
	--with-fontdir=%{_fontsdir}/Type1

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# separate *.afm, convert *.pfa to .pfb
cd $RPM_BUILD_ROOT%{_fontsdir}/Type1
install -d afm
mv -f *.afm afm
for f in *.pfa ; do
	t1binary $f `basename $f .pfa`.pfb
	rm -f $f
done
sed -e '1d;s/\.pfa /.pfb /' fonts.scale > fonts.scale.ibm
rm -f fonts.scale fonts.dir fonts.cache-1

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
%doc COPYING ChangeLog README
%{_fontsdir}/Type1/cour*.pfb
%{_fontsdir}/Type1/afm/cour*.afm
%{_fontsdir}/Type1/fonts.scale.ibm
%{_fontsdir}/Type1/Fontmap.ibm
