%define version 2.2.26
%define release 1
%define major 0
%define libname %mklibname %{name}_ %{major}
%define develname %mklibname %{name} -d

Name: udunits2
Version: %version
Release: %release
Summary: A library for manipulating units of physical quantities
License: Freely distributable (BSD-like)
Group: Sciences/Mathematics
URL: http://my.unidata.ucar.edu/content/software/udunits/index.html
Source0: ftp://ftp.unidata.ucar.edu/pub/udunits/udunits-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-gfortran, gcc-c++, groff
BuildRequires: perl-devel
BuildRequires: bison
BuildRequires: pkgconfig(expat)
BuildRequires: texinfo

%description
The Unidata units utility, udunits, supports conversion of unit specifications 
between formatted and binary forms, arithmetic manipulation of unit 
specifications, and conversion of values between compatible scales of 
measurement. A unit is the amount by which a physical quantity is measured. For
example:

                  Physical Quantity   Possible Unit
                  _________________   _____________
                        time              weeks
                      distance         centimeters
                        power             watts

This utility works interactively and has two modes. In one mode, both an input 
and output unit specification are given, causing the utility to print the 
conversion between them. In the other mode, only an input unit specification is
given. This causes the utility to print the definition -- in standard units -- 
of the input unit.

%package -n %{libname}
Group: System/Libraries
Summary: Libraries for udunits
Provides: lib%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the files needed for compiling programs using
the udunits library.

%package -n %{develname}
Group: Development/Other
Summary: Headers and libraries for udunits
Requires: %{name} = %{version}-%{release}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}


%description -n %{develname}
This package contains the files needed for compiling programs using
the udunits library.

%prep
%setup -q -n udunits-%{version}

%build
%ifarch x86_64
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
%endif
export LD_MATH=-lm 

%configure2_5x --disable-static --docdir %{_docdir}/%{name}

%make_build

%install
%make_install install-html

# We need to do this to avoid conflicting with udunits v1
mkdir -p %{buildroot}%{_includedir}/%{name}/
mv %{buildroot}%{_includedir}/*.h %{buildroot}%{_includedir}/%{name}/
# Don't ship static libs
find %{buildroot} -name '*.la' -delete

# doc
install -p -m0644 ANNOUNCEMENT udunits2.pdf %{buildroot}%{_docdir}/%{name}/

%files
%defattr(-,root,root)
%doc ANNOUNCEMENT CHANGE_LOG LICENSE
%doc udunits2.html udunits2.pdf
%{_bindir}/%{name}
%{_datadir}/udunits/*.xml
%{_infodir}/*.info*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/%{name}/*.h
%{_libdir}/*.so
%{_libdir}/*.a



%changelog
* Wed Feb 17 2010 Emmanuel Andry <eandry@mandriva.org> 2.1.12-3mdv2010.1
+ Revision: 507289
- fix provides

* Tue Jan 19 2010 Emmanuel Andry <eandry@mandriva.org> 2.1.12-2mdv2010.1
+ Revision: 493468
- add missing provides

* Sat Jan 16 2010 Emmanuel Andry <eandry@mandriva.org> 2.1.12-1mdv2010.1
+ Revision: 492387
- import udunits2


