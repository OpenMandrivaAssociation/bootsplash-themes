%define name bootsplash-themes
%define version 2.1.0
%define release %mkrel 6
%define scriptdir %{_datadir}/bootsplash/scripts/

Summary:	Bootsplash themes
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:		%{name}-%{version}.tar.bz2
License:	GPL
Group:		System/Kernel and hardware
BuildRoot:	%{_tmppath}/%{name}-buildroot
Url:		http://www.mandrivalinux.com/cgi-bin/cvsweb.cgi/soft/bootsplash/
Requires:	bootsplash
Requires:	mandriva-theme

BuildArch: noarch

%description
Additional themes for bootsplash:
- Linux
- Ayo
- Ayo-73labAllstar
- Ayo-ElvinTooka
- Ayo-FrozenBubble
- Ayo-Misspingus3
- Ayo-Misspingus4

"-tux" themes use Tux logo instead of theme picture in console

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT{%_sysconfdir,%_datadir}/bootsplash/themes/{RadiantStar,Enterprise{,-spot}}

%post
# update current theme
if [ -x %scriptdir/switch-themes ]; then 
    %scriptdir/switch-themes -u
fi
 
%postun
# switch back to Mandriva theme on full removal
if [ "$1" = "0" ]; then
  if [ -x %scriptdir/switch-themes ]; then 
    %scriptdir/switch-themes Mandriva
  fi
fi

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc README

%dir %_datadir/bootsplash/themes/Linux
%_datadir/bootsplash/themes/Linux/*
%dir %_sysconfdir/bootsplash/themes/Linux
%config(noreplace) %_sysconfdir/bootsplash/themes/Linux/*

%dir %_datadir/bootsplash/themes/Ayo
%_datadir/bootsplash/themes/Ayo/*
%dir %_sysconfdir/bootsplash/themes/Ayo
%config(noreplace) %_sysconfdir/bootsplash/themes/Ayo/*

%dir %_datadir/bootsplash/themes/Ayo-73labAllstar
%_datadir/bootsplash/themes/Ayo-73labAllstar/*
%dir %_sysconfdir/bootsplash/themes/Ayo-73labAllstar
%config(noreplace) %_sysconfdir/bootsplash/themes/Ayo-73labAllstar/*

%dir %_datadir/bootsplash/themes/Ayo-ElvinTooka
%_datadir/bootsplash/themes/Ayo-ElvinTooka/*
%dir %_sysconfdir/bootsplash/themes/Ayo-ElvinTooka
%config(noreplace) %_sysconfdir/bootsplash/themes/Ayo-ElvinTooka/*

%dir %_datadir/bootsplash/themes/Ayo-FrozenBubble
%_datadir/bootsplash/themes/Ayo-FrozenBubble/*
%dir %_sysconfdir/bootsplash/themes/Ayo-FrozenBubble
%config(noreplace) %_sysconfdir/bootsplash/themes/Ayo-FrozenBubble/*

%dir %_datadir/bootsplash/themes/Ayo-Misspingus3
%_datadir/bootsplash/themes/Ayo-Misspingus3/*
%dir %_sysconfdir/bootsplash/themes/Ayo-Misspingus3
%config(noreplace) %_sysconfdir/bootsplash/themes/Ayo-Misspingus3/*

%dir %_datadir/bootsplash/themes/Ayo-Misspingus4
%_datadir/bootsplash/themes/Ayo-Misspingus4/*
%dir %_sysconfdir/bootsplash/themes/Ayo-Misspingus4
%config(noreplace) %_sysconfdir/bootsplash/themes/Ayo-Misspingus4/*

# -tux themes

%dir %_datadir/bootsplash/themes/Mandriva-tux
%_datadir/bootsplash/themes/Mandriva-tux/*
%dir %_sysconfdir/bootsplash/themes/Mandriva-tux
%config(noreplace) %_sysconfdir/bootsplash/themes/Mandriva-tux/*

%dir %_datadir/bootsplash/themes/Enterprise-tux
%_datadir/bootsplash/themes/Enterprise-tux/*
%dir %_sysconfdir/bootsplash/themes/Enterprise-tux
%config(noreplace) %_sysconfdir/bootsplash/themes/Enterprise-tux/*

%dir %_datadir/bootsplash/themes/Enterprise-spot-tux
%_datadir/bootsplash/themes/Enterprise-spot-tux/*
%dir %_sysconfdir/bootsplash/themes/Enterprise-spot-tux
%config(noreplace) %_sysconfdir/bootsplash/themes/Enterprise-spot-tux/*

%dir %_datadir/bootsplash/themes/Ayo-tux
%_datadir/bootsplash/themes/Ayo-tux/*
%dir %_sysconfdir/bootsplash/themes/Ayo-tux
%config(noreplace) %_sysconfdir/bootsplash/themes/Ayo-tux/*

%dir %_datadir/bootsplash/themes/Ayo-73labAllstar-tux
%_datadir/bootsplash/themes/Ayo-73labAllstar-tux/*
%dir %_sysconfdir/bootsplash/themes/Ayo-73labAllstar-tux
%config(noreplace) %_sysconfdir/bootsplash/themes/Ayo-73labAllstar-tux/*

%dir %_datadir/bootsplash/themes/Ayo-ElvinTooka-tux
%_datadir/bootsplash/themes/Ayo-ElvinTooka-tux/*
%dir %_sysconfdir/bootsplash/themes/Ayo-ElvinTooka-tux
%config(noreplace) %_sysconfdir/bootsplash/themes/Ayo-ElvinTooka-tux/*

%dir %_datadir/bootsplash/themes/Ayo-FrozenBubble-tux
%_datadir/bootsplash/themes/Ayo-FrozenBubble-tux/*
%dir %_sysconfdir/bootsplash/themes/Ayo-FrozenBubble-tux
%config(noreplace) %_sysconfdir/bootsplash/themes/Ayo-FrozenBubble-tux/*

%dir %_datadir/bootsplash/themes/Ayo-Misspingus3-tux
%_datadir/bootsplash/themes/Ayo-Misspingus3-tux/*
%dir %_sysconfdir/bootsplash/themes/Ayo-Misspingus3-tux
%config(noreplace) %_sysconfdir/bootsplash/themes/Ayo-Misspingus3-tux/*

%dir %_datadir/bootsplash/themes/Ayo-Misspingus4-tux
%_datadir/bootsplash/themes/Ayo-Misspingus4-tux/*
%dir %_sysconfdir/bootsplash/themes/Ayo-Misspingus4-tux
%config(noreplace) %_sysconfdir/bootsplash/themes/Ayo-Misspingus4-tux/*


