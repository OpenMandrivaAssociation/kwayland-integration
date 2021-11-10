%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{plasmaver} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary: 	KDE Library for integration with the Wayland display server
Name: 		kwayland-integration
Version:	5.23.3
Release: 	1
Source0: 	http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Url: 		http://kde.org/
License: 	GPL
Group: 		System/Libraries
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5IdleTime)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5Wayland)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5WaylandClient)
BuildRequires:	cmake(Qt5XkbCommonSupport)
BuildRequires:	cmake(Qt5WaylandClient)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	cmake(WaylandProtocols)
BuildRequires:	cmake(WaylandScanner)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	plasma-wayland-protocols
BuildRequires:	wayland-tools
BuildRequires:	qt5-qtwayland-private-devel
Requires:	kwayland

%description
KDE Library for integration  Wayland display server.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%dir %{_libdir}/qt5/plugins/kf5/org.kde.kidletime.platforms

%{_libdir}/qt5/plugins/kf5/kwindowsystem/KF5WindowSystemKWaylandPlugin.so
%{_libdir}/qt5/plugins/kf5/org.kde.kidletime.platforms/KF5IdleTimeKWaylandPlugin.so
%{_libdir}/qt5/plugins/kf5/kguiaddons/kmodifierkey/kmodifierkey_wayland.so

%{_datadir}/qlogging-categories5/kwindowsystem.kwayland.categories
