%define upstream_name    String-Flogger
%define upstream_version 1.101244

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	String munging for loggers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/String/String-Flogger-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(JSON)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Sub::Exporter)

BuildArch:	noarch
Requires:	perl(JSON)

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.101.241-2mdv2011.0
+ Revision: 656966
- rebuild for updated spec-helper

* Wed Feb 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.101.241-1
+ Revision: 635244
- update to new version 1.101241

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.101.240-1mdv2011.0
+ Revision: 552633
- update to 1.101240

* Thu Mar 04 2010 Jérôme Quelin <jquelin@mandriva.org> 1.1.0-2mdv2010.1
+ Revision: 514207
- adding missing requires:

* Fri May 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.1.0-1mdv2010.0
+ Revision: 380977
- adding missing buildrequires:
- import perl-String-Flogger


* Fri May 29 2009 cpan2dist 1.001-1mdv
- initial mdv release, generated with cpan2dist



