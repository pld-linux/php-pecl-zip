%define		_modname	zip
%define		_status		stable
Summary:	%{_modname} - a zip management extension
Summary(pl):	%{_modname} - zarządzanie archiwami zip
Name:		php-pecl-%{_modname}
Version:	1.0
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	255203b19e46c0512e6ab3780ba2d2e5
URL:		http://pecl.php.net/package/zip/
BuildRequires:	libtool
BuildRequires:	php-devel
BuildRequires:	zziplib-devel
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
Obsoletes:	php-zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
Zip is an extension to read zip files.

In PECL status of this package is: %{_status}.

%description -l pl
Zip jest rozszerzeniem umożliwiającym odczyt archiwów zip.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/CREDITS
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
