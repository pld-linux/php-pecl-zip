%define		php_name	php%{?php_suffix}
%define		modname	zip
%define		status		stable
Summary:	%{modname} - a zip management extension
Summary(pl.UTF-8):	%{modname} - zarządzanie archiwami zip
Name:		%{php_name}-pecl-%{modname}
Version:	1.15.4
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	https://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	e11a38c022c270fe9c237594f21ec70b
URL:		https://pecl.php.net/package/zip/
BuildRequires:	%{php_name}-devel >= 3:5.0.4
BuildRequires:	rpmbuild(macros) >= 1.650
BuildRequires:	zziplib-devel
%{?requires_php_extension}
Provides:	php(zip)
Obsoletes:	php-pear-%{modname}
Obsoletes:	php-zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zip is an extension to create, modify and read zip files.

In PECL status of this package is: %{status}.

%description -l pl.UTF-8
Zip jest rozszerzeniem umożliwiającym tworzenie, modyfikację oraz
odczyt archiwów zip.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc CREDITS
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
