# $Revision:$, $Date:$
#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	CSS
%define		pnam	Minifier
Summary:	CSS::Minifier - Perl extension for minifying CSS
Name:		perl-CSS-Minifier
Version:	0.01
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CSS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	04f64c08c9268fd0fc619ef8110d2cf4
URL:		http://search.cpan.org/dist/CSS-Minifier/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module removes unnecessary whitespace from CSS. The primary
requirement developing this module is to not break working
stylesheets: if working CSS is in input then working CSS is output.
The Mac/Internet Explorer comment hack will be minimized but not
stripped and so will continue to function.

This module understands space, horizontal tab, new line, carriage
return, and form feed characters to be whitespace. Any other
characters that may be considered whitespace are not minimized. These
other characters include paragraph separator and vertical tab.

For static CSS files, it is recommended that you minify during the
build stage of web deployment. If you minify on-the-fly then it might
be a good idea to cache the minified file. Minifying static files
on-the-fly repeatedly is wasteful.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/CSS/Minifier.pm
%{_mandir}/man3/*
