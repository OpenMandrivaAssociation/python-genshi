Name:           python-genshi
Version:	0.7.3
Release:	1
Summary:        Toolkit for stream-based generation of output for the web

Group:          Development/Python
License:        BSD
URL:            http://genshi.edgewall.org/
Source0:	https://files.pythonhosted.org/packages/cd/ef/ac21ced1b5e7be3bacbc57f9d3d765064b58beb597b8022ad12c5a8c24ea/Genshi-0.7.3.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-devel
BuildRequires:	python-setuptools

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


%changelog
* Thu Apr 07 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.6-3mdv2011.0
+ Revision: 651818
- Rebuild for adding pythonegg provides.

* Sun Oct 31 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.6-2mdv2011.0
+ Revision: 590975
- rebuild for python-2.7
- drop obsolete %%py_requires macro

* Sun Sep 12 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.6-1mdv2011.0
+ Revision: 577726
- update to new version 0.6

* Wed May 05 2010 Funda Wang <fwang@mandriva.org> 0.5.1-4mdv2010.1
+ Revision: 542296
- BR python-setuptools for bug#53946

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.5.1-3mdv2010.0
+ Revision: 442125
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.5.1-2mdv2009.1
+ Revision: 323715
- rebuild

* Tue Aug 19 2008 Colin Guthrie <cguthrie@mandriva.org> 0.5.1-1mdv2009.0
+ Revision: 273651
- New version 0.5.1

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.5-2mdv2009.0
+ Revision: 269024
- rebuild early 2009.0 package (before pixel changes)

* Mon Jun 09 2008 Colin Guthrie <cguthrie@mandriva.org> 0.5-1mdv2009.0
+ Revision: 217248
- New version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Oct 21 2007 Jérôme Soyer <saispo@mandriva.org> 0.4.4-1mdv2008.1
+ Revision: 100807
- New release 0.4.4

* Mon Jun 18 2007 Jérôme Soyer <saispo@mandriva.org> 0.4.1-2mdv2008.0
+ Revision: 40696
- Bump Release
- Fix RPM Group and Encoding bug #31422

* Sun Jun 10 2007 Jérôme Soyer <saispo@mandriva.org> 0.4.1-1mdv2008.0
+ Revision: 37925
- Add switch python
- Remove noardh
- Import python-genshi


