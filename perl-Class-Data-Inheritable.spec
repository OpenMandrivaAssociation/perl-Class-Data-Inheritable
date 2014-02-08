%define upstream_name    Class-Data-Inheritable
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Inheritable, overridable class data
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Class::Data::Inheritable is for creating accessor/mutators to class data. That
is, if you want to store something about your class as a whole (instead of
about a single object). This data is then inherited by your subclasses and can
be overriden.

%prep
%setup -q  -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/Class
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.80.0-4mdv2012.0
+ Revision: 765084
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.80.0-3
+ Revision: 763527
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.80.0-2
+ Revision: 667042
- mass rebuild

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.1
+ Revision: 403007
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.08-3mdv2009.0
+ Revision: 255897
- rebuild

* Sat Jan 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2008.1
+ Revision: 158295
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 0.06-1mdv2008.0
+ Revision: 19780
- 0.06


* Mon Aug 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2007.0
- New version 0.05
- spec cleanup

* Mon Sep 26 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.04-1mdk
- New release 0.04

* Thu Sep 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.02-7mdk
- rebuild

