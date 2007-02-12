Summary:	iODBC test
Summary(pl.UTF-8):   Narzędzie testowe dla iODBC
Name:		odbctest
Version:	1.9.2.7
Release:	0.1
License:	LGPL
Group:		Applications/Databases
Source0:	http://duch.mimuw.edu.pl/~hunter/%{name}-%{version}.tar.gz
# Source0-md5:	d9bf0d2362402a0c187f9f22456d20c8
URL:		http://www.iodbc.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iODBC connection test application.

%description -l pl.UTF-8
Aplikacja testująca połączenia iODBC.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install odbctest $RPM_BUILD_ROOT%{_bindir}/odbctest

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE LICENSE.BSD LICENSE.LGPL
%attr(755,root,root) %{_bindir}/odbctest
