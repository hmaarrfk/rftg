Name: rftg
Version: 0.9.4
Release: 2%{?dist}
Summary: Race for the Galaxy AI

Group: Games
License: GPL
URL: http://www.keldon.net/rftg/

Source0: http://www.keldon.net/rftg/rftg-%{version}.tar.bz2
Source1: rftg.desktop
Source2: rftg.png
BuildRequires: gtk2-devel >= 2.24.29
BuildRequires: desktop-file-utils

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

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
cp %{_sourcedir}/rftg.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --delete-original --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{_sourcedir}/rftg.desktop

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
%{_bindir}/rftg
%{_bindir}/do_train
%{_datadir}/rftg
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/256x256/apps/*



%changelog
* Fri Mar 11 2016 Mark Harfouche <mark.harfouche@gmail.com> - 0.9.4-2
- Now with a launcher

* Wed Mar 9 2016 Mark Harfouche <markharfouche@gmail.com> 0.9.4-1
- Initial build

