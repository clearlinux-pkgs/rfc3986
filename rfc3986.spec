#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rfc3986
Version  : 1.5.0
Release  : 46
URL      : https://files.pythonhosted.org/packages/79/30/5b1b6c28c105629cc12b33bdcbb0b11b5bb1880c6cfbd955f9e792921aa8/rfc3986-1.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/79/30/5b1b6c28c105629cc12b33bdcbb0b11b5bb1880c6cfbd955f9e792921aa8/rfc3986-1.5.0.tar.gz
Summary  : Validating URI References per RFC 3986
Group    : Development/Tools
License  : Apache-2.0
Requires: rfc3986-license = %{version}-%{release}
Requires: rfc3986-python = %{version}-%{release}
Requires: rfc3986-python3 = %{version}-%{release}
Requires: idna
BuildRequires : buildreq-distutils3
BuildRequires : idna
BuildRequires : py
BuildRequires : pytest

%description
=======
        
        A Python implementation of `RFC 3986`_ including validation and authority 
        parsing.
        
        Installation
        ------------

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
Provides: pypi(rfc3986)

%description python3
python3 components for the rfc3986 package.


%prep
%setup -q -n rfc3986-1.5.0
cd %{_builddir}/rfc3986-1.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1620661225
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
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
cp %{_builddir}/rfc3986-1.5.0/LICENSE %{buildroot}/usr/share/package-licenses/rfc3986/731674b4b036fc2010f7f85b1c3160be4d298d48
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rfc3986/731674b4b036fc2010f7f85b1c3160be4d298d48

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
