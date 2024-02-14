Name:           joystickwake
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        A joystick-aware screen waker
License:        MIT
URL:            https://github.com/KyleGospo/joystickwake

Source:         {{{ git_dir_pack }}}
BuildArch:      noarch
	
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
A joystick-aware screen waker

# Disable debug packages
%define debug_package %{nil}

%prep
{{{ git_dir_setup_macro }}}

%build
%py3_build

%install
%py3_install
mkdir -p %{buildroot}%{_mandir}/man1/

%files
%license LICENSE
%{python3_sitelib}/%{name}-*.egg-info/
%{_bindir}/%{name}
%{_sysconfdir}/xdg/autostart/%{name}.desktop

%changelog
{{{ git_dir_changelog }}}