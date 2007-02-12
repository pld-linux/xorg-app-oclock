Summary:	oclock application
Summary(pl.UTF-8):	Aplikacja oclock
Name:		xorg-app-oclock
Version:	1.0.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/oclock-%{version}.tar.bz2
# Source0-md5:	91f49547f9ed3cd0137c8b7c3183e360
Source1:	oclock.desktop
Source2:	oclock.png
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
oclock applications.

%description -l pl.UTF-8
Aplikacja oclock.

%prep
%setup -q -n oclock-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/oclock.desktop
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/oclock.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/oclock
%{_datadir}/X11/app-defaults/Clock-color
%{_desktopdir}/oclock.desktop
%{_pixmapsdir}/oclock.png
%{_mandir}/man1/oclock.1x*
