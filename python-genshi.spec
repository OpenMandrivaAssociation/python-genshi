%define module genshi
%bcond tests 1

Name:		python-genshi
Version:	0.7.10
Release:	1
Summary:	Toolkit for stream-based generation of output for the web
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://genshi.edgewall.org/
# URL:		https://github.com/edgewall/genshi
Source0:	https://github.com/edgewall/genshi/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(babel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif

%description
Genshi is a Python library that provides an integrated set of
components for parsing, generating, and processing HTML, XML or other
textual content for output generation on the web. The major feature is
a template language, which is heavily inspired by Kid.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info
# Remove executable bit from examples
find examples/ -type f | xargs chmod a-x

%build -p
export LDFLAGS="%{ldflags} -lpython%{pyver}"

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitearch}:${PWD}"
# silence the py3.15 deprecation warnings, we are not there yet.
pytest genshi/ -W ignore::DeprecationWarning
%endif

%files
%license COPYING
%doc ChangeLog doc examples README.md
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info
