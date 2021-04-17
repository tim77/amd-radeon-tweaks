# AMD Radeon tweaks

Systemd startup service for tweaks on AMD Radeon videocards. Overclocking, undervolting, power limit and such.

Currently it used for Radeon VII card.

⚠️ You shouldn't use this software without understanding what are you doing and without modifying current values for your card.

### Install

#### Pre-requisites

In order to be able to change voltages and clocks you will have to add to your kernel command line:

```sh
amdgpu.ppfeaturemask=0xffffffff
```

#### 📦 [Fedora [COPR]](https://copr.fedorainfracloud.org/coprs/atim/amd-radeon-tweaks/)

```
sudo dnf copr enable atim/amd-radeon-tweaks -y
sudo dnf install amd-radeon-tweaks
```

#### Run

```
sudo systemctl enable --now amd-radeon-tweaks.service
```

### Tune setting

```sh
sudoedit /usr/sbin/amd-radeon-tweaks.sh
```
