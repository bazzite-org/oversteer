Name:       oversteer
Version:    {{{ git_dir_version }}}
Release:    1%{?dist}
Summary:    Steering Wheel Manager for Linux

License:    GPLv3
URL:        https://github.com/berarma/oversteer
VCS:        {{{ git_dir_vcs }}}
Source:     {{{ git_dir_pack }}}


BuildArch:      noarch
BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-pyudev
BuildRequires:  python3-pyxdg
BuildRequires:  python3-libevdev
BuildRequires:  python3-evdev
BuildRequires:  python3-matplotlib
BuildRequires:  python3-scipy
BuildRequires:  libgudev-devel
BuildRequires:  appstream-devel
BuildRequires:  desktop-file-utils
BuildRequires:  systemd-udev

Requires:   python3-gobject
Requires:   python3-pyudev
Requires:   python3-pyxdg
Requires:   python3-libevdev
Requires:   appstream
Requires:   desktop-file-utils
Requires:   python3-matplotlib
Requires:   python3-scipy
Requires:   python3-matplotlib-gtk3
Requires:   python3-evdev
Requires:   librsvg2
Requires:   oversteer-udev

%description
Oversteer is an application to configure Logitech Wheels.

%prep
{{{ git_dir_setup_macro }}}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/oversteer
%dir %{python3_sitelib}/oversteer/
%pycached %{python3_sitelib}/oversteer/__init__.py
%pycached %{python3_sitelib}/oversteer/application.py
%pycached %{python3_sitelib}/oversteer/gtk_ui.py
%pycached %{python3_sitelib}/oversteer/gui.py
%{python3_sitelib}/oversteer/main.css
%{python3_sitelib}/oversteer/main.ui
%pycached %{python3_sitelib}/oversteer/device.py
%pycached %{python3_sitelib}/oversteer/device_manager.py
%pycached %{python3_sitelib}/oversteer/combined_chart.py
%pycached %{python3_sitelib}/oversteer/gtk_handlers.py
%pycached %{python3_sitelib}/oversteer/linear_chart.py
%pycached %{python3_sitelib}/oversteer/model.py
%pycached %{python3_sitelib}/oversteer/performance_chart.py
%pycached %{python3_sitelib}/oversteer/signal.py
%pycached %{python3_sitelib}/oversteer/test.py
%pycached %{python3_sitelib}/oversteer/wheel_ids.py
%{_datadir}/applications/org.berarma.Oversteer.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.berarma.Oversteer.svg
%{_datadir}/metainfo/org.berarma.Oversteer.appdata.xml

%package udev
Summary: udev rules for oversteer

%description udev
%{summary}

%files udev
/usr/lib/udev/rules.d/99-thrustmaster-wheel-perms.rules
/usr/lib/udev/rules.d/99-logitech-wheel-perms.rules
/usr/lib/udev/rules.d/99-fanatec-wheel-perms.rules

%changelog
{{{ git_dir_changelog }}}
