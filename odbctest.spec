# comment out this to autofind of package requirements
# instead of manually specifing using "Requires" lines
AutoReqProv:	no

Name:		odbctest
Version:	1.9.2.7
Release:	0.1
Summary:	iODBC test
Group:		Applications/Databases
License:	LGPL
Vendor:		OpenLink Software <iodbc@openlinksq.com>
URL:		http://www.iodbc.org/
Source0:	http://duch.mimuw.edu.pl/~hunter/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	glibc-devel >= 2.0
Requires:	glibc >= 2.0

%description
iODBC connection test application.

%description -l pl
Aplikacja testuj±ca po³±czenia iODBC.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}
install -d $RPM_BUILD_ROOT%{_bindir}
cp odbctest $RPM_BUILD_ROOT%{_bindir}/odbctest

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# docs go to /usr/share/doc/[package-name]-[version]
%doc LICENSE LICENSE.BSD LICENSE.LGPL
%attr(755,root,root) %{_bindir}/odbctest
