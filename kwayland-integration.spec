%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{plasmaver} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary: 	KDE Library for integration with the Wayland display server
Name: 		kwayland-integration
Version: 	5.4.0
Release: 	1
Source0: 	http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Url: 		http://kde.org/
License: 	GPL
Group: 		System/Libraries
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5IdleTime)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5Wayland)
BuildRequires:	pkgconfig(Qt5Core)

%description
KDE Library for integration  Wayland display server.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
