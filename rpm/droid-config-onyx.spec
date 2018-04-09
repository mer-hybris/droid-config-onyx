# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc
%define device onyx
%define vendor oneplus

%define vendor_pretty OnePlus
%define device_pretty X

#%define rpm_device onyx
#%define rpm_vendor oneplus

%define dcd_path ./

# Community HW adaptations need this
%define community_adaptation 1

# Adjust this for your device
%define pixel_ratio 1.8

%define have_modem 1

Provides: ofono-configs

%define ofono_enable_plugins hfp_ag_bluez5

# Packages to be uninstalled
#Obsoletes: ofono-configs-mer
#Obsoletes: usb-moded-mass-storage-android-config
#Obsoletes: usb-moded-diag-mode-android
#Obsoletes: usb-moded-pc-suite-mode-android

%include droid-configs-device/droid-configs.inc

%pre
if [ "$1" = "2" ]; then
  rm /etc/acdbdata/ -r || :
fi
