%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	VersionControl_SVN
Summary:	%{_pearname} - OO wrapper interface for the Subversion command-line client
Summary(pl.UTF-8):	%{_pearname} - obiektowy interfejs do klienta Subversion
Name:		php-pear-%{_pearname}
Version:	0.4.0
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8affc1d2d5fa42e9a2f915e4942bf323
URL:		http://pear.php.net/package/VersionControl_SVN/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.9.4
Requires:	php-pear-XML_Parser >= 1.3.4
Requires:	subversion
Obsoletes:	php-pear-VersionControl_SVN-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VersionControl_SVN is a simple OO-style interface for Subversion, the
free/open-source version control system.

VersionControl_SVN can be used to manage trees of source code, text
files, image files -- just about any collection of files.

Some of VersionControl_SVN's features:

 - Full support of svn command-line client's subcommands.
 - Use of flexible error reporting provided by PEAR_ErrorStack.
 - Multi-object factory.
 - Source fully documented with PHPDoc.
 - Stable, extensible interface.
 - Collection of helpful quickstart examples and tutorials.

What can be done with VersionControl_SVN?

 - Make your source code available to your remote dev team or project
   manager.
 - Build your own WYSIWYG web interface to a Subversion repository.
 - Add true version control to a content management system!

VersionControl_SVN is tested against Subversion 1.0.4

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
VersionControl_SVN to prosty, obiektowy interfejs do Subversion,
darmowego systemu kontroli wersji o otwartych źródłach.

VersionControl_SVN może być używany do zarządzania drzewami kodów
źródłowych, plików tekstowych, grafik -- w zasadzie dowolnego zestawu
plików.

Niektóre z cech VersionControl_SVN:

 - pełna obsługa podpoleceń klienta svn,
 - możliwość korzystania z elastycznego systemu raportowania błędów
   dzięki wykorzystaniu PEAR_ErrorStack
 - źródła w pełni udokumentowane przy użyciu PHPDoc,
 - stabilny, rozszerzalny interfejs
 - zestaw przydatnych przykładów i tutoriali,

Co można zrobić za pomocą VersionConrol_SVN:

 - udostępnić kod źródłowy innym programistom lub kierownikowi
   projektu,
 - stworzyć własny interfejs WWW do repozytorium Subversion,
 - dodać prawdziwą kontrolę wersji do systemu zarządzania treścią!

VersionControl_SVN został przetestowany z Subversion w wersji 1.0.4.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

mv docs/VersionControl_SVN/docs/examples .
mv docs/VersionControl_SVN/docs/tutorials examples

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_examplesdir}/%{name}-%{version}}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/VersionControl/SVN.php
%{php_pear_dir}/VersionControl/SVN

%{_examplesdir}/%{name}-%{version}
