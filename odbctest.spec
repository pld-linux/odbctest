Summary:	iODBC test
Summary(pl):	Narzêdzie testowe dla iODBC
Name:		odbctest
Version:	1.9.2.7
Release:	0.1
License:	LGPL
Group:		Applications/Databases
Vendor:		OpenLink Software <iodbc@openlinksq.com>
Source0:	http://duch.mimuw.edu.pl/~hunter/%{name}-%{version}.tar.gz
URL:		http://www.iodbc.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iODBC connection test application.

%description -l pl
Aplikacja testuj±ca po³±czenia iODBC.

%prep
%setup -q

%build
# TODO: optflags
%{__make}

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
