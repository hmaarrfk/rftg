Name: rftg
Version: 0.9.4
Release: 7%{?dist}
Summary: Race for the Galaxy AI

Group: Amusements/Games
License: GPLv2+
URL: http://www.keldon.net/rftg/

Source0: http://www.keldon.net/%{name}/%{name}-%{version}.tar.bz2
Source1: %{name}.desktop
Source2: %{name}.png
Source3: %{name}.appdata.xml

BuildRequires: gtk2-devel >= 2.24.29
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

%description
This is a project to create artificial intelligence opponent(s) for the card game Race for the Galaxy. Currently, the base game and all three expansions are supported.

Online multiplayer is supported.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
%make_install

install -m 644 -D %{_sourcedir}/%{name}.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

install -m 644 -D %{_sourcedir}/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

install -m 755 -d %{buildroot}%{_datadir}/applications
desktop-file-install -m 644 --delete-original --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{_sourcedir}/%{name}.desktop

%check
desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%post
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*



%changelog
* Mon May 09 2016 Mark Harfouche <mark.harfouche@gmail.com> - 0.9.4-7
- For some reason, the appdata wasn't included before

* Mon May 09 2016 Mark Harfouche <mark.harfouche@gmail.com> - 0.9.4-6
- Added the correct license GPLv2+ to the spec file.

* Mon May 09 2016 Mark Harfouche <mark.harfouche@gmail.com> - 0.9.4-5
- rebuilt

* Mon May 09 2016 Mark Harfouche <mark.harfouche@gmail.com> - 0.9.4-4
- Added categories. More fixes to the appdata file

* Sun May 08 2016 Mark Harfouche <mark.harfouche@gmail.com> - 0.9.4-3
- Added appdata

* Fri Mar 11 2016 Mark Harfouche <mark.harfouche@gmail.com> - 0.9.4-2
- Now with a launcher

* Wed Mar 9 2016 Mark Harfouche <markharfouche@gmail.com> 0.9.4-1
- Initial build

