%include	/usr/lib/rpm/macros.mono
Summary:	.NET support for NJB players
Summary(pl.UTF-8):	Obsługa odtwarzaczy NJB z poziomu .NET
Name:		dotnet-njb-sharp
Version:	0.3.0
Release:	3
License:	MIT
Group:		Libraries
Source0:	http://banshee-project.org/files/njb-sharp/njb-sharp-%{version}.tar.gz
# Source0-md5:	d59525dcfa69d6196b339b519f53525e
Patch0:		%{name}-sonames.patch
URL:		http://banshee-project.org/Subprojects/Njb-sharp
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libnjb-devel >= 2.2.4
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.1.16.1
BuildRequires:	pkgconfig
# through njb-sharp.dll.config
%ifarch %{x8664} ia64 ppc64 s390x sparc64
Requires:	libnjb.so.5()(64bit)
%else
Requires:	libnjb.so.5
%endif
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
njb-sharp provides C# bindings for libnjb, to provide NJB Digital
Audio Player (DAP) support to Mono applications.

%description -l pl.UTF-8
njb-sharp udostępnia wiązania C# dla libnjb, aby zapewnić obsługę
odtwarzaczy NJB Digital Audio Player (DAP) w aplikacjach Mono.

%prep
%setup -qn njb-sharp-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	CPPFLAGS="-I%{_includedir}/libnjb" \
	--disable-static

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/njb-sharp/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%dir %{_libdir}/njb-sharp
%attr(755,root,root) %{_libdir}/njb-sharp/libnjbglue.so
%{_libdir}/njb-sharp/njb-sharp.dll
%{_libdir}/njb-sharp/njb-sharp.dll.config
# -devel?
%{_libdir}/njb-sharp/njb-sharp.dll.mdb
%{_pkgconfigdir}/njb-sharp.pc
