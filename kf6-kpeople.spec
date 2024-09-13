%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6People
%define devname %mklibname KF6People -d
#define git 20240217

Name: kf6-kpeople
Version: 6.6.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kpeople/-/archive/master/kpeople-master.tar.bz2#/kpeople-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/frameworks/%{major}/kpeople-%{version}.tar.xz
%endif
Summary: Provides access to all contacts and aggregates them by person
URL: https://invent.kde.org/frameworks/kpeople
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: gettext
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6Contacts)
Requires: %{libname} = %{EVRD}

%description
Provides access to all contacts and aggregates them by person

%package -n %{libname}
Summary: Provides access to all contacts and aggregates them by person
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Provides access to all contacts and aggregates them by person

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Provides access to all contacts and aggregates them by person

%prep
%autosetup -p1 -n kpeople-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kpeople.*

%files -n %{devname}
%{_includedir}/KF6/KPeople
%{_libdir}/cmake/KF6People
%{_qtdir}/doc/KF6People.*

%files -n %{libname}
%{_libdir}/libKF6People.so*
%{_libdir}/libKF6PeopleBackend.so*
%{_libdir}/libKF6PeopleWidgets.so*
%{_qtdir}/qml/org/kde/people
%{_qtdir}/plugins/kpeople
