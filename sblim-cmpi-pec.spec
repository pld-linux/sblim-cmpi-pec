Summary:	SBLIM CMPI Plugin extension
Summary(pl.UTF-8):	Rozszerzenie wtyczek SBLIM CMPI
Name:		sblim-cmpi-pec
Version:	1.0.1
Release:	1
License:	Eclipse Public License v1.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
# Source0-md5:	6481b32f7a632b9344b8a1bfd07ad056
Patch0:		%{name}-dirs.patch
Patch1:		%{name}-format.patch
URL:		http://sblim.sourceforge.net/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	curl-devel >= 7.16.1
BuildRequires:	libtool
BuildRequires:	sblim-cmpi-base-devel
BuildRequires:	sblim-cmpi-devel
BuildRequires:	sblim-sfcc-devel >= 2.1.0
Requires:	%{name}-libs = %{version}-%{release}
Requires:	sblim-cmpi-base
Requires:	sblim-sfcb >= 1.3.2
Requires:	sblim-sfcb-schema >= 2.15
Requires:	nagios-plugins >= 1.4.11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin Extension for CIM (aka PEC) is an effort to expose Nagios
plug-ins through the Common Information Model (CIM).

%description -l pl.UTF-8
Rozszerzenie wtyczek dla CIM (PEC - Plugin Extension for CIM) to
próba udostępnienia wtyczek Nagiosa poprzez interfejs CIM (Common
Information Model).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CIMSERVER=sfcb \
	PROVIDERDIR=%{_libdir}/cmpi \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# modules
%{__rm} $RPM_BUILD_ROOT%{_libdir}/cmpi/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/pecconfigure
%attr(755,root,root) %{_bindir}/peciterativetest
%attr(755,root,root) %{_bindir}/pectest
%attr(755,root,root) %{_libdir}/cmpi/libpec_plugin_indication.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pec.conf
