%define module  Class-Data-Inheritable
%define name    perl-%{module}
%define version 0.05
%define release %mkrel 1
%define	pdir	Class

Name: 		    %{name}
Version: 	    %{version}
Release: 	    %{release}
Summary: 	    Inheritable, overridable class data
License: 	    GPL or Artistic
Group: 		    Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/WWW/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
BuildArch: 	    noarch
BuildRoot: 	    %{_tmppath}/%{name}-%{version}

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

