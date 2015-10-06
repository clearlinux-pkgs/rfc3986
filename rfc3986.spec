#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rfc3986
Version  : 0.2.2
Release  : 14
URL      : https://pypi.python.org/packages/source/r/rfc3986/rfc3986-0.2.2.tar.gz
Source0  : https://pypi.python.org/packages/source/r/rfc3986/rfc3986-0.2.2.tar.gz
Summary  : Validating URI References per RFC 3986
Group    : Development/Tools
License  : Apache-2.0
Requires: rfc3986-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
rfc3986
=======
A Python implementation of `RFC 3986`_ including validation and authority
parsing. Coming soon: `Reference Resolution <http://tools.ietf.org/html/rfc3986#section-5>`_.

%package python
Summary: python components for the rfc3986 package.
Group: Default

%description python
python components for the rfc3986 package.


%prep
%setup -q -n rfc3986-0.2.2

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
py.test-2.7
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
