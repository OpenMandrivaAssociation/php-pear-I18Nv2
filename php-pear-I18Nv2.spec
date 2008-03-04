%define		_class		I18Nv2
%define		_status		beta
%define		_pearname	%{_class}

%define		_requires_exceptions pear(PHPUnit.php)

Summary:	%{_pearname} - internationalization
Name:		php-pear-%{_pearname}
Version:	0.11.4
Release:	%mkrel 3
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
URL:		http://pear.php.net/package/I18Nv2/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires:	php-iconv
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This package provides basic support to localize your application, like
locale based formatting of dates, numbers and currency.

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/{Country,DecoratedList,Language,Locale,Currency}

install %{_pearname}-%{version}/I18Nv2.php %{buildroot}%{_datadir}/pear
install %{_pearname}-%{version}/{Locale,CommonList,Country,Language,Currency,AreaCode,Encoding,Timezone,Negotiator,DecoratedList}.php %{buildroot}%{_datadir}/pear/%{_class}
install %{_pearname}-%{version}/Country/*.php %{buildroot}%{_datadir}/pear/%{_class}/Country
install %{_pearname}-%{version}/DecoratedList/*.php %{buildroot}%{_datadir}/pear/%{_class}/DecoratedList
install %{_pearname}-%{version}/Language/*.php %{buildroot}%{_datadir}/pear/%{_class}/Language
install %{_pearname}-%{version}/Locale/*.php %{buildroot}%{_datadir}/pear/%{_class}/Locale
install %{_pearname}-%{version}/Currency/*.php %{buildroot}%{_datadir}/pear/%{_class}/Currency
   
install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/tests
%doc %{_pearname}-%{version}/docs/examples
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{_pearname}.xml
