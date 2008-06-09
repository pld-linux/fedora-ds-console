%define major_version 1.1
%define minor_version 1

%define shortname fedora-ds
%define pkgname   dirsrv

Summary:	Fedora Directory Server Management Console
Name:		fedora-ds-console
Version:	%{major_version}.%{minor_version}
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://directory.fedoraproject.org/sources/%{name}-%{version}.tar.bz2
# Source0-md5:	ee0401937a81ce2466292a4f9b14e20a
URL:		http://directory.fedoraproject.org
BuildArch:	noarch
BuildRequires:	ant >= 1.6.2
BuildRequires:	idm-console-framework
BuildRequires:	ldapsdk
Requires:	%{shortname}-admin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Java based remote management console used for Managing Fedora
Directory Server.

%prep
%setup -q

%build
%ant \
	-Dbuilt.dir=`pwd`/built \
	-Dconsole.location=%{_javadir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/html/java
install built/package/%{shortname}* $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/html/java
install -d $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/manual/en/slapd/help
install help/en/*.html $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/manual/en/slapd
install help/en/tokens.map $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/manual/en/slapd
install help/en/help/*.html $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/manual/en/slapd/help

# create symlinks
cd $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/html/java
ln -s %{shortname}-%{version}.jar %{shortname}-%{major_version}.jar
ln -s %{shortname}-%{version}.jar %{shortname}.jar
ln -s %{shortname}-%{version}_en.jar %{shortname}-%{major_version}_en.jar
ln -s %{shortname}-%{version}_en.jar %{shortname}_en.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%{_datadir}/%{pkgname}/html/java/%{shortname}-%{version}.jar
%{_datadir}/%{pkgname}/html/java/%{shortname}-%{major_version}.jar
%{_datadir}/%{pkgname}/html/java/%{shortname}.jar
%{_datadir}/%{pkgname}/html/java/%{shortname}-%{version}_en.jar
%{_datadir}/%{pkgname}/html/java/%{shortname}-%{major_version}_en.jar
%{_datadir}/%{pkgname}/html/java/%{shortname}_en.jar
%dir %{_datadir}/%{pkgname}/manual/en/slapd
%{_datadir}/%{pkgname}/manual/en/slapd/tokens.map
%doc %{_datadir}/%{pkgname}/manual/en/slapd/*.html
%doc %{_datadir}/%{pkgname}/manual/en/slapd/help/*.html
