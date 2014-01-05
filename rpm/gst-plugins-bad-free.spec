# Conditional building of X11 related things
%bcond_with X11
Name:       gst-plugins-bad-free

Summary:    GStreamer streaming media framework bad-free plug-ins
Version:    0.10.23
Release:    1
Group:      Applications/Multimedia
License:    LGPLv2+ and LGPLv2
URL:        http://gstreamer.freedesktop.org/
Source0:    gst-plugins-bad-free-%{version}.tar.bz2
Source1:    gst-p-bad-cleanup.sh
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(orc-0.4) >= 0.4.5
BuildRequires:  pkgconfig(gstreamer-0.10)
BuildRequires:  pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:  pkgconfig(libexif)
%if %{with X11}
BuildRequires:  pkgconfig(xt)
%endif
BuildRequires:  check
BuildRequires:  gettext-devel
BuildRequires:  vim

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.
This package contains plug-ins that are not tested well enough, or the code
is not of good enough quality.


%package devel
Summary:    Development tools for GStreamer bad free plugins
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for the GStreamer media framework bad free plug-ins



%prep
%setup -q -n %{name}-%{version}/gst-plugins-bad
chmod +x %{_sourcedir}/gst-p-bad-cleanup.sh

%build

# filter bad sources
%{_sourcedir}/gst-p-bad-cleanup.sh
export NOCONFIGURE=1
%autogen
%reconfigure --disable-static \
    --with-package-name='Mer GStreamer Bad Free Plugins package' \
    --with-package-origin='http://www.merproject.org/' \
    --enable-experimental \
    --disable-gtk-doc \
    --disable-nls \
    --enable-orc

make %{?jobs:-j%jobs}


%install
rm -rf %{buildroot}
%make_install

mv %{buildroot}/%{_libdir}/pkgconfig/gstreamer-plugins-bad-0.10.pc %{buildroot}/%{_libdir}/pkgconfig/gstreamer-plugins-bad-free-0.10.pc
rm -rf %{buildroot}/%{_datadir}/gtk-doc


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libgstbasevideo-0.10.so.*
%{_libdir}/libgstphotography-0.10.so.*
%{_libdir}/libgstsignalprocessor-0.10.so.*
%{_libdir}/libgstbasecamerabinsrc-0.10.so.*
%{_libdir}/libgstcodecparsers-0.10.so.*
#%{_libdir}/gstreamer-0.10/libgst*.so
%{_libdir}/gstreamer-0.10/libgstliveadder.so
%{_libdir}/gstreamer-0.10/libgstrtpmux.so
%{_libdir}/gstreamer-0.10/libgstdtmf.so
%{_libdir}/gstreamer-0.10/libgstsdpelem.so
%{_libdir}/gstreamer-0.10/libgstautoconvert.so
%{_libdir}/gstreamer-0.10/libgstcamerabin.so
%{_libdir}/gstreamer-0.10/libgstcamerabin2.so
%{_libdir}/gstreamer-0.10/libgstjpegformat.so
%{_libdir}/gstreamer-0.10/libgstrawparse.so
%{_libdir}/gstreamer-0.10/libgstshm.so
%{_libdir}/gstreamer-0.10/libgstvideomaxrate.so
%{_libdir}/gstreamer-0.10/libgstvideoparsersbad.so
%{_libdir}/gstreamer-0.10/libgstfragmented.so
%{_libdir}/gstreamer-0.10/libgstmpegtsdemux.so
%ifarch %{ix86} x86_64
%{_libdir}/gstreamer-0.10/libgstreal.so
%endif
#debugging plugin
%{_libdir}/gstreamer-0.10/libgstdebugutilsbad.so

# From extras
#%{_libdir}/gstreamer-0.10/libgstwildmidi.so
#%ifarch %{ix86}
#%{_libdir}/gstreamer-0.10/libgstvp8.so
#%endif

%files devel
%defattr(-,root,root,-)
%{_libdir}/libgstbasevideo-0.10.so
%{_libdir}/libgstphotography-0.10.so
%{_libdir}/libgstsignalprocessor-0.10.so
%{_libdir}/libgstbasecamerabinsrc-0.10.so
%{_libdir}/libgstcodecparsers-0.10.so
%{_includedir}/gstreamer-0.10/gst/interfaces/photography*
%{_includedir}/gstreamer-0.10/gst/basecamerabinsrc
%{_includedir}/gstreamer-0.10/gst/signalprocessor
%{_includedir}/gstreamer-0.10/gst/video
%{_includedir}/gstreamer-0.10/gst/codecparsers
%{_libdir}/pkgconfig/gstreamer-plugins-bad-free-0.10.pc
%{_libdir}/pkgconfig/gstreamer-basevideo-0.10.pc
%{_libdir}/pkgconfig/gstreamer-codecparsers-0.10.pc
