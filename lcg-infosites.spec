Name:				lcg-infosites
Version:			3.1.0
Release:			3%{?dist}
Summary:			Command line tool for the WLCG information system
Group:				Applications/Internet
License:			ASL 2.0
URL:				http://svnweb.cern.ch/trac/gridinfo/wiki
Source:			%{name}-%{version}.tar.gz

BuildRoot:			%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:			noarch
BuildRequires: rsync
BuildRequires: make

%description
lcg-infosites is a simple command line tool in Perl for 
the WLCG information system

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/lcg-infosites
%{_mandir}/man1/lcg-infosites.*

%changelog
* Thu Apr 26 2012 Laurence Field <laurence.field@cern.ch> - 3.1.0
 - Improved the spec file for EPEL compliance
 - FHS compliant


