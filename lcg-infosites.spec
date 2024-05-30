Name: lcg-infosites
Version: 3.2.0
Release: 1%{?dist}
Summary: Command line tool for the WLCG information system
Group: Applications/Internet
License: ASL 2.0
URL: https://github.com/EGI-Federation/lcg-infosites
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildRequires: rsync
BuildRequires: make
Requires: perl-LDAP

%description
lcg-infosites is a simple command line tool in Perl for the grid information
system

%prep
%setup -q

%build
# Nothing to build

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/lcg-infosites
%{_mandir}/man1/lcg-infosites.*
%doc AUTHORS.md README.md
%license COPYRIGHT LICENSE.txt
%doc %{_docdir}/%{name}-%{version}/README.md
%doc %{_docdir}/%{name}-%{version}/AUTHORS.md
%license %{_datadir}/licenses/%{name}-%{version}/COPYRIGHT
%license %{_datadir}/licenses/%{name}-%{version}/LICENSE.txt

%changelog
* Thu May 30 2024 Baptiste Grenier <baptiste.grenier@egi.eu> - 3.2.0
 - Lint PERL. (#13) (Baptiste Grenier)
 - Lint files. (#12) (Baptiste Grenier)
 - Add community files and GitHub actions. Target CentOS 7, AlmaLinux 8 and 9. (#7) (Baptiste Grenier)
 - Add missing EL9 dependency. (#6) (Adam Boutcher)

* Thu Apr 26 2012 Laurence Field <laurence.field@cern.ch> - 3.1.0
 - Improved the spec file for EPEL compliance
 - FHS compliant
