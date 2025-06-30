Summary:	Modern desktop calculator
Summary(pl.UTF-8):	Nowoczesny kalkulator
Name:		qalculate-gtk
Version:	5.6.0
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	https://github.com/Qalculate/qalculate-gtk/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	99b536134f3501ffc964c55d42948a56
URL:		https://qalculate.github.io/
BuildRequires:	automake
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	glib2-devel >= 1:2.4
BuildRequires:	gtk+3-devel >= 3.12
BuildRequires:	intltool
BuildRequires:	libqalculate-devel >= %{version}
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.3.8
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.000
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.4
Requires:	gtk+3 >= 3.12
Requires:	hicolor-icon-theme
Requires:	libqalculate >= %{version}
Suggests:	gnuplot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qalculate is a modern multi-purpose desktop calculator. It is small
and simple to use but with much power. Features include arbitrary
precision, plotting, and a graphical interface (GTK+).

%description -l pl.UTF-8
Qalculate jest nowoczesnym, wielozadaniowym kalkulatorem. Jest mały i
prosty w użyciu, lecz posiada duże możliwości. Podstawowymi cechami
programu są nieograniczona precyzja, możliwość rysowania wykresów i
graficzny interfejs (GTK+).

%package search-provider
Summary:	Qalculate-gtk search provider for GNOME Shell
Summary(pl.UTF-8):	Usługa wyszukiwania Qalculate-gtk dla powłoki GNOME
Group:		Applications/Math
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-shell >= 3

%description search-provider
Qalculate-gtk search provider for GNOME Shell.

%description search-provider -l pl.UTF-8
Usługa wyszukiwania Qalculate-gtk dla powłoki GNOME.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged in doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/qalculate-gtk

%{__mv} $RPM_BUILD_ROOT%{_localedir}/pt{_PT,}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/html
%attr(755,root,root) %{_bindir}/qalculate-gtk
%{_desktopdir}/qalculate-gtk.desktop
%{_mandir}/man1/qalculate-gtk.1*
%{_iconsdir}/hicolor/*x*/apps/qalculate.png
%{_iconsdir}/hicolor/scalable/apps/qalculate.svg
%{_datadir}/metainfo/qalculate-gtk.appdata.xml

%files search-provider
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/qalculate-search-provider
%{_datadir}/dbus-1/services/io.github.Qalculate.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/io.github.Qalculate.search-provider.ini
