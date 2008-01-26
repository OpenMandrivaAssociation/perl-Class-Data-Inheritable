%define module  Class-Data-Inheritable
%define name    perl-%{module}
%define version 0.08
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Inheritable, overridable class data
License: 	GPL or Artistic
Group: 	    Development/Perl
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Class/%{module}-%{version}.tar.gz
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Class::Data::Inheritable is for creating accessor/mutators to class data. That
is, if you want to store something about your class as a whole (instead of
about a single object). This data is then inherited by your subclasses and can
be overriden.

%prep
%setup -q  -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/Class
%{_mandir}/*/*

