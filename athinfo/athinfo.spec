%define name athinfo
%define version 10.3
%define unmangled_version 10.3
%define release 1

Name:      %{name}
Version:   %{version}
Release:   %{release}
License:   MIT
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix:    %{_prefix}
BuildArch: noarch
Vendor:    Evan Broder <UNKNOWN>
URL:       https://github.com/mit-athena/athinfo
Source0:   https://github.com/dm-vdo/athinfo/archive/refs/heads/main.tar.gz
Summary:   Retrieve information about Athena workstations

BuildRequires: python3
Requires:      python3

%description
Athinfo is a client for retreiving information from remote hosts without
either requiring authentication from the client end OR creating security
holes on the remote host.

%prep
%setup -n %{name}-main

%build
python3 setup.py build

%install
python3 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Thu Dec 09 2021 Andy Walsh <awalsh@redhat.com> - 10.3-1
- Initial build
