Name:           python-genshi
Version:        0.5
Release:        %mkrel 2
Summary:        Toolkit for stream-based generation of output for the web

Group:          Development/Python
License:        BSD
URL:            http://genshi.edgewall.org/
Source0:        http://ftp.edgewall.com/pub/genshi/Genshi-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  python-devel

%description
Genshi is a Python library that provides an integrated set of
components for parsing, generating, and processing HTML, XML or other
textual content for output generation on the web. The major feature is
a template language, which is heavily inspired by Kid.

%prep
%setup -q -n Genshi-%{version}
find examples -type f | xargs chmod a-x

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --install-purelib=%py_platsitedir

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING doc examples README.txt
%{py_platsitedir}/*
