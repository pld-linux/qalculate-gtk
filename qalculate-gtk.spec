Summary:	Modern desktop calculator
Summary(pl.UTF-8):   Nowoczesny kalkulator
Name:		qalculate-gtk
Version:	0.9.4
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://dl.sourceforge.net/qalculate/%{name}-%{version}.tar.gz
# Source0-md5:	ac9adea6799ea4019b5a45869cff3cff
URL:		http://qalculate.sourceforge.net/
BuildRequires:	automake
BuildRequires:	cln-devel >= 1.1.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libgnome-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libqalculate-devel >= %{version}
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.3.8
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.1.4
Requires(post,postun):	scrollkeeper
Requires:	gnuplot
Requires:	libqalculate >= %{version}
Provides:	qalculate = %{version}-%{release}
Obsoletes:	qalculate
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
cp -f /usr/share/automake/config.sub .
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
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_datadir}/%{name}
%{_pixmapsdir}/*.png
%{_omf_dest_dir}/%{name}
