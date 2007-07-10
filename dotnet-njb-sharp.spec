#
%include	/usr/lib/rpm/macros.mono
#
Summary:	.NET support for NJB players
Name:		dotnet-njb-sharp
Version:	0.3.0
Release:	2
License:	GPL
Group:		Development/Libraries
Source0:	http://banshee-project.org/files/njb-sharp/njb-sharp-%{version}.tar.gz
# Source0-md5:	d59525dcfa69d6196b339b519f53525e
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libnjb-devel >= 2.2.4
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.1.16.1
BuildRequires:	pkgconfig
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
njb-sharp provides C# bindings for libnjb, to provide NJB Digital
Audio Player (DAP) support to Mono applications.

%prep
%setup -qn njb-sharp-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
export CPPFLAGS="-I%{_includedir}/libnjb"
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
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/njb-sharp
%{_pkgconfigdir}/njb-sharp.pc
