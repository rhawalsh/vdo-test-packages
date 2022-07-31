%define repo_name utility-mill
%define repo_branch main

%define name python3-%{repo_name}
%define version 1.0.5
%define unmangled_version 1.0.5
%define release 1

Summary: %{name}
Name: %{name}
Version: %{version}
Release: %{release}
URL:     https://github.com/dm-vdo/python-support-utility-mill
Source0: %{url}/archive/refs/heads/main.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch

%if 0%{?rhel} && 0%{?rhel} < 9
BuildRequires: python39
BuildRequires: python39-pyyaml
BuildRequires: python39-setuptools
Requires: python39
Requires: python39-pyyaml
%else
BuildRequires: python3
BuildRequires: python3-pyyaml
BuildRequires: python3-setuptools
Requires: python3
Requires: python3-pyyaml
%endif

%description
UNKNOWN

%prep
%setup -n python-support-utility-mill-%{repo_branch}

%build
python3 setup.py build

%install
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Tue Jul 26 2022 Joe Shimkus <jshimkush@redhat.com> - 1.0.5-1
- Make functional rpm for RHEL earlier than 9.0.
- Sync version with setup.py.
