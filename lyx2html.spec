Summary: Simple lyx to html converter
Name:    lyx2html
Version: 0.2
Release: 11
Source0: %{name}-%{version}.tar.bz2
Patch:	%{name}-makefile.patch
License: GPL
URL: https://www.netmeister.org/apps/lyx2html/index.html
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
%setup
%patch -p0

%build
%make

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
make DESTDIR=%{buildroot} install

%clean

%files
%defattr(-,root,root)
%{_bindir}/lyx2html
%defattr(644,root,root,755)
%doc README COPYING
%{_mandir}/man1/*




%changelog
* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.2-9mdv2009.0
+ Revision: 251574
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.2-7mdv2008.1
+ Revision: 170972
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.2-6mdv2008.1
+ Revision: 129565
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import lyx2html


* Tue Apr 26 2005 Lenny Cartier <lenny@mandriva.com> 0.2-6mdk
- rebuild

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.2-5mdk
- rebuild

* Mon Jan 27 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.2-4mdk
- rebuild

* Thu Aug 29 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.2-3mdk
- rebuild

* Tue Aug 21 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.2-2mdk
- rebuild

* Mon Jan 22 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.2-1mdk
- updated to 0.2

* Mon Sep 11 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.1-2mdk
- cleanup

* Mon Aug 28 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.1-1mdk
- patch makefile for BM
- used srpm from Jan Schaumann <jschauma@netmeister.org> :
	- First spec file for Mandrake distribution.

