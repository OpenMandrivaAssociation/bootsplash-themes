%define scriptdir %{_datadir}/bootsplash/scripts/

Summary:	Bootsplash themes
Name:		bootsplash-themes
Version:	2.1.0
Release:	9
Source:		%{name}-%{version}.tar.bz2
License:	GPL
Group:		System/Kernel and hardware
Url:		https://www.mandrivalinux.com/cgi-bin/cvsweb.cgi/soft/bootsplash/
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
%autosetup -p1

%build
%make_build

%install
%make_install

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




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.0-7mdv2011.0
+ Revision: 616812
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 2.1.0-6mdv2010.0
+ Revision: 424686
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 2.1.0-5mdv2009.0
+ Revision: 240449
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 2.1.0-3mdv2008.0
+ Revision: 64788
- rebuild


* Tue Mar 06 2007 Olivier Blin <oblin@mandriva.com> 2.1.0-2mdv2007.0
+ Revision: 133609
- remove themes containing the Mandrake name
- Import bootsplash-themes

* Sat Aug 13 2005 Olivier Blin <oblin@mandriva.com> 2.1.0-1mdk
- switch to Mandriva
- misc Makefile cleanups
- remove Prefix tag

* Thu Feb 10 2005 Olivier Blin <oblin@mandrakesoft.com> 2.0.0-11mdk
- Mandrake theme is now called Mandrakelinux

