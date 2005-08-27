# $Rev: 3357 $, $Date: 2005-08-27 17:42:47 $
#
Summary:	oclock application
Summary(pl):	Aplikacja oclock
Name:		xorg-app-oclock
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/oclock-%{version}.tar.bz2
# Source0-md5:	c6d053a6fc269f47532203975d246f3c
Patch0:		oclock-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/oclock-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
oclock applications.

%description -l pl
Aplikacja oclock.


%prep
%setup -q -n oclock-%{version}
%patch0 -p1


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


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%{_sysconfdir}/X11/app-defaults/*
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*
