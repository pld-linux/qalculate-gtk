Summary:	Modern desktop calculator
Summary(pl.UTF-8):	Nowoczesny kalkulator
Name:		qalculate-gtk
Version:	5.1.0
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	https://github.com/Qalculate/qalculate-gtk/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	bfeb597dfe7b8d8a79c3bc0c849ee960
URL:		https://qalculate.github.io/
BuildRequires:	automake
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	glib2-devel >= 2.4
BuildRequires:	gtk+3-devel >= 3.12
BuildRequires:	intltool
BuildRequires:	libqalculate-devel >= 5.1.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.3.8
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.000
Requires(post,postun):	scrollkeeper
Requires:	libqalculate >= 5.1.0
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

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/html
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_mandir}/man1/qalculate-gtk.1.*
%{_iconsdir}/hicolor/*x*/apps/qalculate.png
%{_iconsdir}/hicolor/scalable/apps/qalculate.svg
%{_datadir}/metainfo/qalculate-gtk.appdata.xml

%files search-provider
%defattr(644,root,root,755)
%attr(755,roor,root) %{_libexecdir}/qalculate-search-provider
%{_datadir}/dbus-1/services/io.github.Qalculate.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/io.github.Qalculate.search-provider.ini
