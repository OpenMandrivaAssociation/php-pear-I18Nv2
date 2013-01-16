%define		_class		I18Nv2
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	0.11.4
Release:	%mkrel 10
Summary:	Internationalization
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/I18Nv2/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires:	php-iconv
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This package provides basic support to localize your application, like
locale based formatting of dates, numbers and currency.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/examples
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.11.4-8mdv2011.0
+ Revision: 667521
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.11.4-7mdv2011.0
+ Revision: 607113
- rebuild

* Fri Dec 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.11.4-6mdv2010.1
+ Revision: 473539
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.11.4-5mdv2010.0
+ Revision: 426649
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.11.4-4mdv2009.0
+ Revision: 224750
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.11.4-3mdv2008.1
+ Revision: 178520
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.11.4-2mdv2008.0
+ Revision: 15468
- rule out the PHPUnit.php dep


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.11.4-1mdv2007.0
+ Revision: 81154
- Import php-pear-I18Nv2

* Sat Apr 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.11.4-1mdk
- 0.11.4

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.11.3-8mdk
- new group (Development/PHP)

* Mon Jan 16 2006 Oden Eriksson <oeriksson@mandriva.com> 0.11.3-7mdk
- fix deps

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.11.3-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.11.3-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.11.3-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.11.3-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.11.3-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.11.3-1mdk
- initial Mandriva package (PLD import)

