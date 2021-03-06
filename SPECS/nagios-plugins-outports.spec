%define debug_package %{nil}

Summary:	Nagios plugin - check_outports
Name:		nagios-plugins-outports
Version:	0.1
Release:	2.vortex%{?dist}
Vendor:		Vortex RPM
License:	MIT
Group:		Applications/System
URL:		https://github.com/thesharp/nagios-plugins-outports
Source0:	%{name}-%{version}.tar.gz
Requires:	nagios-plugins
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This nagios plugin is used to check the percentage of the free outgoing ports
available on every network interface.

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
install -D -p -m 0755 check_outports %{buildroot}%{_libdir}/nagios/plugins/check_outports

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/nagios/plugins/check_outports
%doc README.md LICENSE

%changelog
* Fri Oct 10 2014  Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 0.1-2.vortex
- Fix.

* Fri Oct 10 2014  Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 0.1-1.vortex
- Initial packaging.

