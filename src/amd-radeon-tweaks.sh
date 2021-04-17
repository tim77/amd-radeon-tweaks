#! /usr/bin/bash

echo "manual" > /sys/class/drm/card0/device/power_dpm_force_performance_level

### Changing the core voltage
# echo "vc 2 1801 1126" > /sys/class/drm/card0/device/pp_od_clk_voltage
echo "vc 2 1801 1020" > /sys/class/drm/card0/device/pp_od_clk_voltage
echo "vc 1 1304 825" > /sys/class/drm/card0/device/pp_od_clk_voltage
echo "c" > /sys/class/drm/card0/device/pp_od_clk_voltage

### Changing the memory clock
# echo "m 1 1000" > /sys/class/drm/card0/device/pp_od_clk_voltage
# echo "c" > /sys/class/drm/card0/device/pp_od_clk_voltage

### Changing the power limit
###   * 150W
echo "150000000" > /sys/class/drm/card0/device/hwmon/hwmon1/power1_cap
