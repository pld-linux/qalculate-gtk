Summary:	Modern desktop calculator
Summary(pl.UTF-8):	Nowoczesny kalkulator
Name:		qalculate-gtk
Version:	3.1.0
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	https://github.com/Qalculate/qalculate-gtk/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	92306458a4e8afd8ee6a0276872bf6dc
URL:		http://qalculate.github.io/
BuildRequires:	automake
BuildRequires:	cln-devel >= 1.1.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libgnome-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libqalculate-devel >= 3.1.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.3.8
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.1.4
Requires(post,postun):	scrollkeeper
Requires:	libqalculate >= 0.9.7-3
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

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_pixmapsdir}/*.png
%{_datadir}/appdata/qalculate-gtk.appdata.xml
