%define upstream_name    Class-Data-Inheritable
%define upstream_version 0.08

Summary:	Inheritable, overridable class data
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	16
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

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
%{_mandir}/man3/*

