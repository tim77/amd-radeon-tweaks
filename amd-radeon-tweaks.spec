Name: amd-radeon-tweaks
Version: 0
Release: 1%{?dist}
Summary: AMD Radeon tweaks
BuildArch: noarch

License: GPLv3+
URL: https://github.com/tim77/amd-radeon-tweaks
Source0: %{url}/archive/main/%{name}-main.tar.gz

BuildRequires: systemd-rpm-macros

%description
Systemd startup service for tweaks on AMD Radeon videocards. Overclocking,
undervolting, power limit and such.

Currently it used for Radeon VII card.

⚠️ You shouldn't use this software without understanding what are you doing
and without modifying current values for your card.

Enable:

  sudo systemctl enable --now amd-radeon-tweaks.service

Tune setting:

  sudoedit /usr/sbin/amd-radeon-tweaks.sh


%prep
%autosetup -n %{name}-main -p1


%install
install -Dp src/%{name}.service -t %{buildroot}%{_prefix}/lib/systemd/system/
install -Dp src/%{name}.sh -t %{buildroot}%{_sbindir}


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%doc README.md
%license LICENSE
%{_sbindir}/%{name}.sh
%{_unitdir}/*.service


%changelog
* Sat Apr 17 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0-1
- Initial package
