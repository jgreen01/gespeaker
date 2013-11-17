Summary:        GTK+ front-end for espeak and MBROLA to speech the read text
Name:           gespeaker
Version:        0.8.2
Release:        1
License:        GPLv2+
URL:            http://gespeaker.muflone.com/
Source0:        https://github.com/muflone/%{name}/archive/%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  desktop-file-utils python-devel
BuildArch:      noarch
Requires:       python >= 2.7
Requires:       pygtk2
Requires:       alsa-utils
Requires:       espeak

%description
Gespeaker allows you to play a text in many languages with settings
for voice, pitch, volume and speed. The read text can also be 
recorded to WAV file for future listening.

%prep
%setup -q 

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} 
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{python_sitelib}/*.egg-info
%{_datadir}/doc/%{name}/*
%{_mandir}/man1/%{name}.1.gz

%changelog
* Sat Nov 16 2013 Muflone <webreg(at)vbsimple.net> 0.8.2-1
- First build

