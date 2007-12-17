%define name lyx2html
%define version 0.2
%define release  %mkrel 6

Summary: Lyx2html is a simple lyx to html converter
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch:	%{name}-makefile.patch.bz2
License: GPL
URL: http://www.netmeister.org/apps/lyx2html/index.html
Group: Text tools

%description
"lyx2html" is a very simple Lyx to HTML converter. As the name 
suggests, it takes a ".lyx" document as input and generates an 
HTML-file following a few simple rules. "lyx2html" can be very 
useful for generation documentation. This is a beta-release, 
meaning there are probably still a lot of bugs in the program,
and that it might not generate the expected output or that it 
might even segfault on you.

%prep
rm -rf $RPM_BUILD_ROOT

%setup
%patch -p 1

%build
%make

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
make DESTDIR=$RPM_BUILD_ROOT install

%clean

%files
%defattr(-,root,root)
%{_bindir}/lyx2html
%defattr(644,root,root,755)
%doc README COPYING
%{_mandir}/man1/*


