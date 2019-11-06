Name:          libgusb
Version:       0.3.0
Release:       5
Summary:       GObject-based library for libusb1
License:       LGPLv2+
URL:           https://github.com/hughsie/libgusb
Source0:       http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz
BuildRequires: vala-devel vala-tools meson libusb1-devel gtk-doc gobject-introspection-devel glib2-devel

%description
GUsb is a GObject wrapper for libusb1 that makes it easy to do
asynchronous control, bulk and interrupt transfers with proper
cancellation and integration into a mainloop.This makes it easy 
to integrate low level USB transfers with your high-level 
application or system daemon.    

%package       devel
Summary:       Development files and Header files for %{name}
Requires:      %{name} = %{version}-%{release}

%description   devel
The %{name}-devel package contains libraries and header files for %{name}.

%package_help

%prep
%autosetup -n  %{name}-%{version} -p1

%build
%meson -Dvapi=true -Dtests=true
%meson_build

%install
%meson_install
%ldconfig_scriptlets

%files 
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_libdir}/girepository-1.0/GUsb-1.0.typelib
%{_libdir}/libgusb.so.*

%files  devel
%defattr(-,root,root)
%{_bindir}/gusbcmd
%{_libdir}/libgusb.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/gusb-1/gusb/*.h
%{_includedir}/gusb-1/gusb.h
%{_datadir}/gir-1.0/GUsb-1.0.gir
%{_datadir}/vala/vapi/*

%files  help
%defattr(-,root,root)
%doc NEWS README.md 
%{_datadir}/gtk-doc/html/gusb/*

%changelog
* Wed Oct 9 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.3.0-5
- Type:bugfix
- Id:NA
- SUG:NA
- DESC: Modify the license

* Wed Sep 4 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.3.0-4
- Type:enhancement
- Id:NA
- SUG:NA
- DESC: Add a new subpackage of help

* Thu Aug 22 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.3.0-3
- Package init 
