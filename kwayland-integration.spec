%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{plasmaver} |cut -d. -f2`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary: 	KDE Library for integration with the Wayland display server
Name: 		kwayland-integration
Version:	6.4.1
Release: 	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/kwayland-integration/-/archive/%{gitbranch}/kwayland-integration-%{gitbranchd}.tar.bz2#/kwayland-integration-%{git}.tar.bz2
%else
Source0: 	http://download.kde.org/%{stable}/plasma/%{plasmaver}/kwayland-integration-%{version}.tar.xz
%endif
Url: 		https://kde.org/
License: 	GPL
Group: 		System/Libraries

BuildRequires:	cmake(ECM)

BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5WaylandClient)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(QtWaylandScanner)
BuildRequires:	cmake(KF5Wayland)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	qt5-qtwayland
BuildRequires:	qt5-qtwayland-private-devel
BuildRequires:	cmake(WaylandProtocols)
BuildRequires:	cmake(WaylandScanner)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	plasma-wayland-protocols
BuildRequires:	wayland-tools
Requires:	kwayland >= 6.0

BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

# Renamed after 6.0 2025-04-27
%rename plasma6-kwayland-integration

%description
KDE Library for integration  Wayland display server.

%files
%{_libdir}/qt5/plugins/kf5/kwindowsystem/KF5WindowSystemKWaylandPlugin.so
%{_datadir}/qlogging-categories5/kwindowsystem.kwayland.categories
