%define device suzu
%define vendor sony

%define rpm_device f5121
%define rpm_vendor qualcomm

%define vendor_pretty Sony
%define device_pretty Xperia X

%define have_custom_img_boot 1
%define have_custom_img_recovery 1

%define droid_target_aarch64 1

%define device_variant -userdebug
%define lunch_device aosp_f5121
%define pre_actions sudo update-java-alternatives -s java-1.7.0-openjdk-amd64

%define makefstab_skip_entries /system none /sys/fs/pstore

%define straggler_files\
    /selinux_version\
    /service_contexts\
%{nil}

Requires: droid-system

%define obs_requires\
    BuildRequires: droid-system-vendor-obsbuild\
%{nil}

%include rpm/dhd/droid-hal-device.inc

