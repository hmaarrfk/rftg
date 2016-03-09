Name: rftg
Version: 0.9.4
Release: 1%{?dist}
Summary: Race for the Galaxy AI

Group: Games
License: GPL
URL: http://www.keldon.net/rftg/

Source: http://www.keldon.net/rftg/rftg-%{version}.tar.bz2
BuildRequires: gtk2-devel >= 2.24.29

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


%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/*
%{_datadir}/*



%changelog
* Wed Mar 9 2016 Mark Harfouche <markharfouche@gmail.com> 0.9.4-1
- Initial build

