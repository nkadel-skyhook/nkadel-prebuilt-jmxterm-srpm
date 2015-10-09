%global realname jmxterm
%global rcversion -alpha-4-uber

Summary: Jmxterm
Name: prebuilt-jmxterm
Version: 1.0
# Use funny subversion name to match rcversion, as needed
Release: 0.1.appha4uber%{?dist}
License: Apache
Group: Network/Daemons
URL: https://github.com/jiaqi/jmxterm
Source0: %{realname}-%{version}%{rcversion}.jar
BuildRoot: %{_tmppath}/%{name}-%{version}%{rcversion}-root
BuildArch: noarch
# jmxterm seems pretty insensitive to java versions
Requires: java

%description
Jmxterm is a command line based interactive JMX client. It's designed
to allw user to access a Java MBean server from command line without
graphical environment. In another workd. it's a command line based
jconsole

%prep
%setup -c -T -n %{realname}-%{version}%{rcverison}
cat >jmxterm.sh <<EOF
#!/bin/sh
#
# jmxterm - jmxterm wrapper script
#

java -jar %{_libexecdir}/%{realname}/%{realname}-%{version}%{rcversion}.jar
EOF

%build

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d ${RPM_BUILD_ROOT}%{_libexecdir}/%{realname}
%{__install} -m 644  %{SOURCE0} ${RPM_BUILD_ROOT}%{_libexecdir}/%{realname}/%{realname}-%{version}%{rcversion}.jar
%{__install} -d ${RPM_BUILD_ROOT}%{_bindir}
%{__install} -m 755 jmxterm.sh ${RPM_BUILD_ROOT}%{_bindir}/jmxterm

%pre

%post

%preun

%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir %{_libexecdir}/%{realname}
%attr(644,root,root) %{_libexecdir}/%{realname}/%{realname}-%{version}%{rcversion}.jar
%attr(755,root,root) %{_bindir}/jmxterm

%changelog
* Fri Oct  9 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com>
- Set up prebuilt-jmxterm RPM
