#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rfc3986
Version  : 1.3.0
Release  : 29
URL      : https://files.pythonhosted.org/packages/8b/5f/452af943db1ee24875fd1c51b5ce15c0e4e0b1340ffc72ff8f199af90382/rfc3986-1.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/8b/5f/452af943db1ee24875fd1c51b5ce15c0e4e0b1340ffc72ff8f199af90382/rfc3986-1.3.0.tar.gz
Summary  : Validating URI References per RFC 3986
Group    : Development/Tools
License  : Apache-2.0
Requires: rfc3986-license = %{version}-%{release}
Requires: rfc3986-python = %{version}-%{release}
Requires: rfc3986-python3 = %{version}-%{release}
Requires: idna
BuildRequires : buildreq-distutils3
BuildRequires : py
BuildRequires : pytest

%description
rfc3986
=======
A Python implementation of `RFC 3986`_ including validation and authority
parsing.

%package license
Summary: license components for the rfc3986 package.
Group: Default

%description license
license components for the rfc3986 package.


%package python
Summary: python components for the rfc3986 package.
Group: Default
Requires: rfc3986-python3 = %{version}-%{release}

%description python
python components for the rfc3986 package.


%package python3
Summary: python3 components for the rfc3986 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the rfc3986 package.


%prep
%setup -q -n rfc3986-1.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555896981
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rfc3986
cp LICENSE %{buildroot}/usr/share/package-licenses/rfc3986/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rfc3986/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
