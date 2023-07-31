Summary: FSL Community BSP Linux mainline based kernel with backported features and fixes
Name: linux-fslc
Version: 6.1.38+git0+085682f3fc
Release: r0
License: GPL-2.0-only
Group: base
Packager: Poky <poky@lists.yoctoproject.org>
BuildRequires: bc-native
BuildRequires: bison-native
BuildRequires: kmod-native
BuildRequires: pkgconfig-native
BuildRequires: virtual/arm-poky-linux-gnueabi-binutils
BuildRequires: virtual/arm-poky-linux-gnueabi-gcc

%description
Linux kernel based on mainline kernel used by FSL Community BSP in order to
provide support for some backported features and fixes, or because it was
applied in linux-next and takes some time to become part of a stable
version, or because it is not applicable for upstreaming.

%package -n linux-fslc-src
Summary: FSL Community BSP Linux mainline based kernel with backported features and fixes - Source files
License: GPL-2.0-only
Group: devel

%description -n linux-fslc-src
Linux kernel based on mainline kernel used by FSL Community BSP in order to
provide support for some backported features and fixes, or because it was
applied in linux-next and takes some time to become part of a stable
version, or because it is not applicable for upstreaming.  This package
contains sources for debugging purposes.

%package -n kernel-dbg
Summary: FSL Community BSP Linux mainline based kernel with backported features and fixes
License: GPL-2.0-only
Group: base

%description -n kernel-dbg
Linux kernel based on mainline kernel used by FSL Community BSP in order to
provide support for some backported features and fixes, or because it was
applied in linux-next and takes some time to become part of a stable
version, or because it is not applicable for upstreaming.

%package -n kernel
Summary: FSL Community BSP Linux mainline based kernel with backported features and fixes
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e = 6.1.38+git0+085682f3fc-r0

%description -n kernel
Linux kernel based on mainline kernel used by FSL Community BSP in order to
provide support for some backported features and fixes, or because it was
applied in linux-next and takes some time to become part of a stable
version, or because it is not applicable for upstreaming.

%package -n kernel-6.1.38-fslc+g085682f3fc7e
Summary: FSL Community BSP Linux mainline based kernel with backported features and fixes
License: GPL-2.0-only
Group: base
Recommends: kernel-image-6.1.38-fslc+g085682f3fc7e = 6.1.38+git0+085682f3fc-r0
Provides: kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-base = 6.1.38+git0+085682f3fc

%description -n kernel-6.1.38-fslc+g085682f3fc7e
Linux kernel based on mainline kernel used by FSL Community BSP in order to
provide support for some backported features and fixes, or because it was
applied in linux-next and takes some time to become part of a stable
version, or because it is not applicable for upstreaming.

%package -n kernel-vmlinux
Summary: FSL Community BSP Linux mainline based kernel with backported features and fixes
License: GPL-2.0-only
Group: base

%description -n kernel-vmlinux
Linux kernel based on mainline kernel used by FSL Community BSP in order to
provide support for some backported features and fixes, or because it was
applied in linux-next and takes some time to become part of a stable
version, or because it is not applicable for upstreaming.

%package -n kernel-image-6.1.38-fslc+g085682f3fc7e
Summary: FSL Community BSP Linux mainline based kernel with backported features and fixes
License: GPL-2.0-only
Group: base
Requires: kernel-image-zimage-6.1.38-fslc+g085682f3fc7e = 6.1.38+git0+085682f3fc-r0
Provides: kernel-image = 6.1.38+git0+085682f3fc

%description -n kernel-image-6.1.38-fslc+g085682f3fc7e
Linux kernel based on mainline kernel used by FSL Community BSP in order to
provide support for some backported features and fixes, or because it was
applied in linux-next and takes some time to become part of a stable
version, or because it is not applicable for upstreaming.

%package -n kernel-dev
Summary: FSL Community BSP Linux mainline based kernel with backported features and fixes
License: GPL-2.0-only
Group: base
Recommends: kernel-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-base-dev
Recommends: kernel-image-zimage-dev
Recommends: kernel-module-a8293-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-adv7180-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-af9013-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-af9033-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-ascot2e-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-atbm8830-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-ath-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-ath10k-core-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-ath10k-sdio-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-au8522-common-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-au8522-decoder-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-au8522-dig-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-bcm3510-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-binfmt-misc-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-bnep-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-brcmfmac-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-brcmutil-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-cdc-acm-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-cdc-eem-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-coda-vpu-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-crc-itu-t-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-crc7-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-cx22700-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-cx22702-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-cx24110-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-cx24113-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-cx24116-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-cx24117-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-cx24120-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-cx24123-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-cxd2099-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-cxd2820r-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-cxd2841er-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-cxd2880-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-cxd2880-spi-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-da9063-wdt-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-dib0070-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-dib0090-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-dib3000mb-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-dib3000mc-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-dib7000m-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-dib7000p-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-dib8000-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-dib9000-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-dmatest-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-drx39xyj-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-drxd-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-drxk-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-ds3000-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-dvb-pll-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-dw-hdmi-ahb-audio-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-e4000-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-ec100-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-ehset-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-fc0011-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-fc0012-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-fc0013-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-fc2580-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-ftdi-sio-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-g-audio-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-g-ether-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-g-ffs-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-g-mass-storage-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-g-ncm-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-g-serial-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-g-zero-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-gadgetfs-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-gpio-siox-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-helene-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-horus3a-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-i2c-algo-pca-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-i2c-algo-pcf-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-imx-sdma-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-imx-vdoa-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-irq-imx-mu-msi-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-isl6405-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-isl6421-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-isl6423-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-isofs-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-it913x-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-itd1000-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-ix2505v-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-l64781-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-lg2160-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-lgdt3305-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-lgdt3306a-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-lgdt330x-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-lgs8gl5-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-lgs8gxx-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-libcrc32c-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-lnbh25-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-lnbh29-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-lnbp21-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-lnbp22-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-m88ds3103-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-m88rs2000-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-m88rs6000t-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-max2165-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-mb86a16-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-mb86a20s-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-mc44s803-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-mn88443x-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-mn88472-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-mn88473-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-msdos-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-msi001-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-mt2060-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-mt2063-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-mt20xx-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-mt2131-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-mt2266-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-mt312-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-mt352-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-mwifiex-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-mwifiex-pcie-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-mwifiex-sdio-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-mxl301rf-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-mxl5005s-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-mxl5007t-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-mxl5xx-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-mxl692-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-nls-iso8859-15-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-nxt200x-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-nxt6000-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-option-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-or51132-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-or51211-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-ov2680-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-ov5640-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-ov5645-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-pegasus-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-psmouse-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-qm1d1b0004-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-qm1d1c0042-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-qt1010-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-r820t-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-rn5t618-power-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-rtl2830-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-rtl2832-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-rtl2832-sdr-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-rtl8150-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-s5h1409-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-s5h1411-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-s5h1420-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-s5h1432-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-s921-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-serport-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-si2157-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-si2165-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-si2168-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-si21xx-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-siox-bus-gpio-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-siox-core-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-snd-hwdep-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-snd-usb-audio-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-snd-usbmidi-lib-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-sp2-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-sp887x-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-stb0899-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-stb6000-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-stb6100-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-stv0288-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-stv0297-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-stv0299-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-stv0367-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-stv0900-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-stv090x-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-stv0910-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-stv6110-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-stv6110x-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-stv6111-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tc90522-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tda10021-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tda10023-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tda10048-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tda1004x-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tda10071-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tda10086-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tda18212-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tda18218-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tda18250-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tda18271-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tda18271c2dd-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tda665x-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tda8083-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tda8261-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tda826x-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tda827x-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tda8290-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tda9887-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tea5761-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tea5767-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-ts2020-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tua6100-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tua9001-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tuner-simple-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-tuner-types-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-udf-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-usb-wwan-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-usbserial-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-usbtest-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-uvcvideo-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-v4l2-jpeg-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-ves1820-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-ves1x93-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-wl12xx-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-wl18xx-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-wlcore-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-wlcore-sdio-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-xc2028-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-xc4000-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-xc5000-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-zd1301-demod-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-zl10036-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-zl10039-6.1.38-fslc+g085682f3fc7e-dev
Recommends: kernel-module-zl10353-6.1.38-fslc+g085682f3fc7e-dev

%description -n kernel-dev
Linux kernel based on mainline kernel used by FSL Community BSP in order to
provide support for some backported features and fixes, or because it was
applied in linux-next and takes some time to become part of a stable
version, or because it is not applicable for upstreaming.

%package -n kernel-modules
Summary: FSL Community BSP Linux mainline based kernel with backported features and fixes
License: GPL-2.0-only
Group: base
Requires: kernel-module-a8293-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-adv7180-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-af9013-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-af9033-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-ascot2e-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-atbm8830-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-ath-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-ath10k-core-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-ath10k-sdio-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-au8522-common-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-au8522-decoder-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-au8522-dig-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-bcm3510-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-binfmt-misc-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-bnep-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-brcmfmac-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-brcmutil-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-cdc-acm-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-cdc-eem-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-coda-vpu-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-crc-itu-t-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-crc7-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-cx22700-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-cx22702-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-cx24110-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-cx24113-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-cx24116-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-cx24117-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-cx24120-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-cx24123-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-cxd2099-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-cxd2820r-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-cxd2841er-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-cxd2880-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-cxd2880-spi-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-da9063-wdt-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-dib0070-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-dib0090-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-dib3000mb-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-dib3000mc-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-dib7000m-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-dib7000p-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-dib8000-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-dib9000-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-dmatest-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-drx39xyj-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-drxd-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-drxk-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-ds3000-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-dvb-pll-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-dw-hdmi-ahb-audio-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-e4000-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-ec100-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-ehset-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-fc0011-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-fc0012-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-fc0013-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-fc2580-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-ftdi-sio-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-g-audio-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-g-ether-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-g-ffs-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-g-mass-storage-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-g-ncm-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-g-serial-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-g-zero-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-gadgetfs-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-gpio-siox-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-helene-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-horus3a-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-i2c-algo-pca-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-i2c-algo-pcf-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-imx-sdma-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-imx-vdoa-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-irq-imx-mu-msi-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-isl6405-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-isl6421-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-isl6423-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-isofs-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-it913x-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-itd1000-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-ix2505v-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-l64781-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-lg2160-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-lgdt3305-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-lgdt3306a-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-lgdt330x-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-lgs8gl5-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-lgs8gxx-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-libcrc32c-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-lnbh25-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-lnbh29-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-lnbp21-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-lnbp22-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-m88ds3103-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-m88rs2000-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-m88rs6000t-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-max2165-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-mb86a16-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-mb86a20s-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-mc44s803-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-mn88443x-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-mn88472-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-mn88473-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-msdos-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-msi001-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-mt2060-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-mt2063-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-mt20xx-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-mt2131-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-mt2266-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-mt312-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-mt352-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-mwifiex-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-mwifiex-pcie-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-mwifiex-sdio-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-mxl301rf-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-mxl5005s-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-mxl5007t-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-mxl5xx-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-mxl692-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-nls-iso8859-15-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-nxt200x-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-nxt6000-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-option-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-or51132-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-or51211-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-ov2680-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-ov5640-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-ov5645-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-pegasus-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-psmouse-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-qm1d1b0004-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-qm1d1c0042-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-qt1010-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-r820t-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-rn5t618-power-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-rtl2830-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-rtl2832-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-rtl2832-sdr-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-rtl8150-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-s5h1409-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-s5h1411-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-s5h1420-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-s5h1432-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-s921-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-serport-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-si2157-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-si2165-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-si2168-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-si21xx-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-siox-bus-gpio-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-siox-core-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-snd-hwdep-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-snd-usb-audio-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-snd-usbmidi-lib-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-sp2-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-sp887x-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-stb0899-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-stb6000-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-stb6100-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-stv0288-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-stv0297-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-stv0299-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-stv0367-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-stv0900-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-stv090x-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-stv0910-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-stv6110-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-stv6110x-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-stv6111-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tc90522-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tda10021-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tda10023-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tda10048-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tda1004x-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tda10071-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tda10086-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tda18212-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tda18218-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tda18250-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tda18271-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tda18271c2dd-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tda665x-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tda8083-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tda8261-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tda826x-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tda827x-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tda8290-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tda9887-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tea5761-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tea5767-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-ts2020-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tua6100-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tua9001-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tuner-simple-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tuner-types-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-udf-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-usb-wwan-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-usbserial-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-usbtest-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-uvcvideo-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-v4l2-jpeg-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-ves1820-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-ves1x93-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-wl12xx-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-wl18xx-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-wlcore-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-wlcore-sdio-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-xc2028-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-xc4000-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-xc5000-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-zd1301-demod-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-zl10036-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-zl10039-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-zl10353-6.1.38-fslc+g085682f3fc7e

%description -n kernel-modules
Kernel modules meta package

%package -n kernel-image-zimage-6.1.38-fslc+g085682f3fc7e
Summary: FSL Community BSP Linux mainline based kernel with backported features and fixes
License: GPL-2.0-only
Group: base
Provides: kernel-image-zimage = 6.1.38+git0+085682f3fc

%description -n kernel-image-zimage-6.1.38-fslc+g085682f3fc7e
Linux kernel based on mainline kernel used by FSL Community BSP in order to
provide support for some backported features and fixes, or because it was
applied in linux-next and takes some time to become part of a stable
version, or because it is not applicable for upstreaming.

%package -n kernel-devicetree
Summary: FSL Community BSP Linux mainline based kernel with backported features and fixes
License: GPL-2.0-only
Group: base

%description -n kernel-devicetree
Linux kernel based on mainline kernel used by FSL Community BSP in order to
provide support for some backported features and fixes, or because it was
applied in linux-next and takes some time to become part of a stable
version, or because it is not applicable for upstreaming.

%package -n kernel-module-dmatest-6.1.38-fslc+g085682f3fc7e
Summary: dmatest kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-dmatest

%description -n kernel-module-dmatest-6.1.38-fslc+g085682f3fc7e
dmatest kernel module

%package -n kernel-module-imx-sdma-6.1.38-fslc+g085682f3fc7e
Summary: imx-sdma kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-imx-sdma

%description -n kernel-module-imx-sdma-6.1.38-fslc+g085682f3fc7e
imx-sdma kernel module; i.MX SDMA driver

%package -n kernel-module-gpio-siox-6.1.38-fslc+g085682f3fc7e
Summary: gpio-siox kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-siox-core-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-siox-core-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-siox-core-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-gpio-siox

%description -n kernel-module-gpio-siox-6.1.38-fslc+g085682f3fc7e
gpio-siox kernel module; SIOX gpio driver

%package -n kernel-module-dw-hdmi-ahb-audio-6.1.38-fslc+g085682f3fc7e
Summary: dw-hdmi-ahb-audio kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-dw-hdmi-ahb-audio

%description -n kernel-module-dw-hdmi-ahb-audio-6.1.38-fslc+g085682f3fc7e
dw-hdmi-ahb-audio kernel module; Synopsis Designware HDMI AHB ALSA
interface

%package -n kernel-module-i2c-algo-pca-6.1.38-fslc+g085682f3fc7e
Summary: i2c-algo-pca kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-i2c-algo-pca

%description -n kernel-module-i2c-algo-pca-6.1.38-fslc+g085682f3fc7e
i2c-algo-pca kernel module; I2C-Bus PCA9564/PCA9665 algorithm

%package -n kernel-module-i2c-algo-pcf-6.1.38-fslc+g085682f3fc7e
Summary: i2c-algo-pcf kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-i2c-algo-pcf

%description -n kernel-module-i2c-algo-pcf-6.1.38-fslc+g085682f3fc7e
i2c-algo-pcf kernel module; I2C-Bus PCF8584 algorithm

%package -n kernel-module-psmouse-6.1.38-fslc+g085682f3fc7e
Summary: psmouse kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-psmouse

%description -n kernel-module-psmouse-6.1.38-fslc+g085682f3fc7e
psmouse kernel module; PS/2 mouse driver

%package -n kernel-module-serport-6.1.38-fslc+g085682f3fc7e
Summary: serport kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-serport

%description -n kernel-module-serport-6.1.38-fslc+g085682f3fc7e
serport kernel module; Input device TTY line discipline

%package -n kernel-module-irq-imx-mu-msi-6.1.38-fslc+g085682f3fc7e
Summary: irq-imx-mu-msi kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-irq-imx-mu-msi

%description -n kernel-module-irq-imx-mu-msi-6.1.38-fslc+g085682f3fc7e
irq-imx-mu-msi kernel module; Freescale MU MSI controller driver

%package -n kernel-module-a8293-6.1.38-fslc+g085682f3fc7e
Summary: a8293 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-a8293

%description -n kernel-module-a8293-6.1.38-fslc+g085682f3fc7e
a8293 kernel module; Allegro A8293 SEC driver

%package -n kernel-module-af9013-6.1.38-fslc+g085682f3fc7e
Summary: af9013 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-af9013

%description -n kernel-module-af9013-6.1.38-fslc+g085682f3fc7e
af9013 kernel module; Afatech AF9013 DVB-T demodulator driver

%package -n kernel-module-af9033-6.1.38-fslc+g085682f3fc7e
Summary: af9033 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-af9033

%description -n kernel-module-af9033-6.1.38-fslc+g085682f3fc7e
af9033 kernel module; Afatech AF9033 DVB-T demodulator driver

%package -n kernel-module-ascot2e-6.1.38-fslc+g085682f3fc7e
Summary: ascot2e kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-ascot2e

%description -n kernel-module-ascot2e-6.1.38-fslc+g085682f3fc7e
ascot2e kernel module; Sony ASCOT2E terr/cab tuner driver

%package -n kernel-module-atbm8830-6.1.38-fslc+g085682f3fc7e
Summary: atbm8830 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-atbm8830

%description -n kernel-module-atbm8830-6.1.38-fslc+g085682f3fc7e
atbm8830 kernel module; AltoBeam ATBM8830/8831 GB20600 demodulator driver

%package -n kernel-module-au8522-common-6.1.38-fslc+g085682f3fc7e
Summary: au8522-common kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-au8522-common

%description -n kernel-module-au8522-common-6.1.38-fslc+g085682f3fc7e
au8522-common kernel module; Auvitek AU8522 QAM-B/ATSC Demodulator driver

%package -n kernel-module-au8522-decoder-6.1.38-fslc+g085682f3fc7e
Summary: au8522-decoder kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-au8522-common-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-au8522-common-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-au8522-common-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-au8522-decoder

%description -n kernel-module-au8522-decoder-6.1.38-fslc+g085682f3fc7e
au8522-decoder kernel module

%package -n kernel-module-au8522-dig-6.1.38-fslc+g085682f3fc7e
Summary: au8522-dig kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-au8522-common-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-au8522-common-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-au8522-common-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-au8522-dig

%description -n kernel-module-au8522-dig-6.1.38-fslc+g085682f3fc7e
au8522-dig kernel module; Auvitek AU8522 QAM-B/ATSC Demodulator driver

%package -n kernel-module-bcm3510-6.1.38-fslc+g085682f3fc7e
Summary: bcm3510 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-bcm3510

%description -n kernel-module-bcm3510-6.1.38-fslc+g085682f3fc7e
bcm3510 kernel module; Broadcom BCM3510 ATSC (8VSB/16VSB & ITU J83 AnnexB
FEC QAM64/256) demodulator driver

%package -n kernel-module-cx22700-6.1.38-fslc+g085682f3fc7e
Summary: cx22700 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-cx22700

%description -n kernel-module-cx22700-6.1.38-fslc+g085682f3fc7e
cx22700 kernel module; Conexant CX22700 DVB-T Demodulator driver

%package -n kernel-module-cx22702-6.1.38-fslc+g085682f3fc7e
Summary: cx22702 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-cx22702

%description -n kernel-module-cx22702-6.1.38-fslc+g085682f3fc7e
cx22702 kernel module; Conexant CX22702 DVB-T Demodulator driver

%package -n kernel-module-cx24110-6.1.38-fslc+g085682f3fc7e
Summary: cx24110 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-cx24110

%description -n kernel-module-cx24110-6.1.38-fslc+g085682f3fc7e
cx24110 kernel module; Conexant CX24110 DVB-S Demodulator driver

%package -n kernel-module-cx24113-6.1.38-fslc+g085682f3fc7e
Summary: cx24113 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-cx24113

%description -n kernel-module-cx24113-6.1.38-fslc+g085682f3fc7e
cx24113 kernel module; DVB Frontend module for Conexant
CX24113/CX24128hardware

%package -n kernel-module-cx24116-6.1.38-fslc+g085682f3fc7e
Summary: cx24116 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-cx24116

%description -n kernel-module-cx24116-6.1.38-fslc+g085682f3fc7e
cx24116 kernel module; DVB Frontend module for Conexant cx24116/cx24118
hardware

%package -n kernel-module-cx24117-6.1.38-fslc+g085682f3fc7e
Summary: cx24117 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-cx24117

%description -n kernel-module-cx24117-6.1.38-fslc+g085682f3fc7e
cx24117 kernel module; DVB Frontend module for Conexant cx24117/cx24132
hardware

%package -n kernel-module-cx24120-6.1.38-fslc+g085682f3fc7e
Summary: cx24120 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-cx24120

%description -n kernel-module-cx24120-6.1.38-fslc+g085682f3fc7e
cx24120 kernel module; DVB Frontend module for Conexant CX24120/CX24118
hardware

%package -n kernel-module-cx24123-6.1.38-fslc+g085682f3fc7e
Summary: cx24123 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-cx24123

%description -n kernel-module-cx24123-6.1.38-fslc+g085682f3fc7e
cx24123 kernel module; DVB Frontend module for Conexant
CX24123/CX24109/CX24113 hardware

%package -n kernel-module-cxd2099-6.1.38-fslc+g085682f3fc7e
Summary: cxd2099 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-cxd2099

%description -n kernel-module-cxd2099-6.1.38-fslc+g085682f3fc7e
cxd2099 kernel module; Sony CXD2099AR Common Interface controller driver

%package -n kernel-module-cxd2820r-6.1.38-fslc+g085682f3fc7e
Summary: cxd2820r kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-cxd2820r

%description -n kernel-module-cxd2820r-6.1.38-fslc+g085682f3fc7e
cxd2820r kernel module; Sony CXD2820R demodulator driver

%package -n kernel-module-cxd2841er-6.1.38-fslc+g085682f3fc7e
Summary: cxd2841er kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-cxd2841er

%description -n kernel-module-cxd2841er-6.1.38-fslc+g085682f3fc7e
cxd2841er kernel module; Sony CXD2837/38/41/43/54ER DVB-C/C2/T/T2/S/S2
demodulator driver

%package -n kernel-module-dib0070-6.1.38-fslc+g085682f3fc7e
Summary: dib0070 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-dib0070

%description -n kernel-module-dib0070-6.1.38-fslc+g085682f3fc7e
dib0070 kernel module; Driver for the DiBcom 0070 base-band RF Tuner

%package -n kernel-module-dib0090-6.1.38-fslc+g085682f3fc7e
Summary: dib0090 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-dib0090

%description -n kernel-module-dib0090-6.1.38-fslc+g085682f3fc7e
dib0090 kernel module; Driver for the DiBcom 0090 base-band RF Tuner

%package -n kernel-module-dib3000mb-6.1.38-fslc+g085682f3fc7e
Summary: dib3000mb kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-dib3000mb

%description -n kernel-module-dib3000mb-6.1.38-fslc+g085682f3fc7e
dib3000mb kernel module; DiBcom 3000M-B DVB-T demodulator

%package -n kernel-module-dib3000mc-6.1.38-fslc+g085682f3fc7e
Summary: dib3000mc kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-dib3000mc

%description -n kernel-module-dib3000mc-6.1.38-fslc+g085682f3fc7e
dib3000mc kernel module; Driver for the DiBcom 3000MC/P COFDM demodulator

%package -n kernel-module-dib7000m-6.1.38-fslc+g085682f3fc7e
Summary: dib7000m kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-dib7000m

%description -n kernel-module-dib7000m-6.1.38-fslc+g085682f3fc7e
dib7000m kernel module; Driver for the DiBcom 7000MA/MB/PA/PB/MC COFDM
demodulator

%package -n kernel-module-dib7000p-6.1.38-fslc+g085682f3fc7e
Summary: dib7000p kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-dib7000p

%description -n kernel-module-dib7000p-6.1.38-fslc+g085682f3fc7e
dib7000p kernel module; Driver for the DiBcom 7000PC COFDM demodulator

%package -n kernel-module-dib8000-6.1.38-fslc+g085682f3fc7e
Summary: dib8000 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-dib8000

%description -n kernel-module-dib8000-6.1.38-fslc+g085682f3fc7e
dib8000 kernel module; Driver for the DiBcom 8000 ISDB-T demodulator

%package -n kernel-module-dib9000-6.1.38-fslc+g085682f3fc7e
Summary: dib9000 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-dib9000

%description -n kernel-module-dib9000-6.1.38-fslc+g085682f3fc7e
dib9000 kernel module; Driver for the DiBcom 9000 COFDM demodulator

%package -n kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e
Summary: dibx000-common kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-dibx000-common

%description -n kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e
dibx000-common kernel module; Common function the DiBcom demodulator family

%package -n kernel-module-drxd-6.1.38-fslc+g085682f3fc7e
Summary: drxd kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-drxd

%description -n kernel-module-drxd-6.1.38-fslc+g085682f3fc7e
drxd kernel module; DRXD driver

%package -n kernel-module-drxk-6.1.38-fslc+g085682f3fc7e
Summary: drxk kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-drxk

%description -n kernel-module-drxk-6.1.38-fslc+g085682f3fc7e
drxk kernel module; DRX-K driver

%package -n kernel-module-ds3000-6.1.38-fslc+g085682f3fc7e
Summary: ds3000 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-ds3000

%description -n kernel-module-ds3000-6.1.38-fslc+g085682f3fc7e
ds3000 kernel module; DVB Frontend module for Montage Technology DS3000
hardware

%package -n kernel-module-dvb-pll-6.1.38-fslc+g085682f3fc7e
Summary: dvb-pll kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-dvb-pll

%description -n kernel-module-dvb-pll-6.1.38-fslc+g085682f3fc7e
dvb-pll kernel module; dvb pll library

%package -n kernel-module-ec100-6.1.38-fslc+g085682f3fc7e
Summary: ec100 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-ec100

%description -n kernel-module-ec100-6.1.38-fslc+g085682f3fc7e
ec100 kernel module; E3C EC100 DVB-T demodulator driver

%package -n kernel-module-helene-6.1.38-fslc+g085682f3fc7e
Summary: helene kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-helene

%description -n kernel-module-helene-6.1.38-fslc+g085682f3fc7e
helene kernel module; Sony HELENE Sat/Ter tuner driver

%package -n kernel-module-horus3a-6.1.38-fslc+g085682f3fc7e
Summary: horus3a kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-horus3a

%description -n kernel-module-horus3a-6.1.38-fslc+g085682f3fc7e
horus3a kernel module; Sony HORUS3A satellite tuner driver

%package -n kernel-module-isl6405-6.1.38-fslc+g085682f3fc7e
Summary: isl6405 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-isl6405

%description -n kernel-module-isl6405-6.1.38-fslc+g085682f3fc7e
isl6405 kernel module; Driver for lnb supply and control ic isl6405

%package -n kernel-module-isl6421-6.1.38-fslc+g085682f3fc7e
Summary: isl6421 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-isl6421

%description -n kernel-module-isl6421-6.1.38-fslc+g085682f3fc7e
isl6421 kernel module; Driver for lnb supply and control ic isl6421

%package -n kernel-module-isl6423-6.1.38-fslc+g085682f3fc7e
Summary: isl6423 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-isl6423

%description -n kernel-module-isl6423-6.1.38-fslc+g085682f3fc7e
isl6423 kernel module; ISL6423 SEC

%package -n kernel-module-itd1000-6.1.38-fslc+g085682f3fc7e
Summary: itd1000 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-itd1000

%description -n kernel-module-itd1000-6.1.38-fslc+g085682f3fc7e
itd1000 kernel module; Integrant ITD1000 driver

%package -n kernel-module-ix2505v-6.1.38-fslc+g085682f3fc7e
Summary: ix2505v kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-ix2505v

%description -n kernel-module-ix2505v-6.1.38-fslc+g085682f3fc7e
ix2505v kernel module; DVB IX2505V tuner driver

%package -n kernel-module-l64781-6.1.38-fslc+g085682f3fc7e
Summary: l64781 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-l64781

%description -n kernel-module-l64781-6.1.38-fslc+g085682f3fc7e
l64781 kernel module; LSI L64781 DVB-T Demodulator driver

%package -n kernel-module-lg2160-6.1.38-fslc+g085682f3fc7e
Summary: lg2160 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-lg2160

%description -n kernel-module-lg2160-6.1.38-fslc+g085682f3fc7e
lg2160 kernel module; LG Electronics LG216x ATSC/MH Demodulator Driver

%package -n kernel-module-lgdt3305-6.1.38-fslc+g085682f3fc7e
Summary: lgdt3305 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-lgdt3305

%description -n kernel-module-lgdt3305-6.1.38-fslc+g085682f3fc7e
lgdt3305 kernel module; LG Electronics LGDT3304/5 ATSC/QAM-B Demodulator
Driver

%package -n kernel-module-lgdt3306a-6.1.38-fslc+g085682f3fc7e
Summary: lgdt3306a kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-lgdt3306a

%description -n kernel-module-lgdt3306a-6.1.38-fslc+g085682f3fc7e
lgdt3306a kernel module; LG Electronics LGDT3306A ATSC/QAM-B Demodulator
Driver

%package -n kernel-module-lgdt330x-6.1.38-fslc+g085682f3fc7e
Summary: lgdt330x kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-lgdt330x

%description -n kernel-module-lgdt330x-6.1.38-fslc+g085682f3fc7e
lgdt330x kernel module; LGDT330X (ATSC 8VSB & ITU-T J.83 AnnexB 64/256 QAM)
Demodulator Driver

%package -n kernel-module-lgs8gl5-6.1.38-fslc+g085682f3fc7e
Summary: lgs8gl5 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-lgs8gl5

%description -n kernel-module-lgs8gl5-6.1.38-fslc+g085682f3fc7e
lgs8gl5 kernel module; Legend Silicon LGS-8GL5 DMB-TH Demodulator driver

%package -n kernel-module-lgs8gxx-6.1.38-fslc+g085682f3fc7e
Summary: lgs8gxx kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-lgs8gxx

%description -n kernel-module-lgs8gxx-6.1.38-fslc+g085682f3fc7e
lgs8gxx kernel module; Legend Silicon LGS8913/LGS8GXX DMB-TH demodulator
driver

%package -n kernel-module-lnbh25-6.1.38-fslc+g085682f3fc7e
Summary: lnbh25 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-lnbh25

%description -n kernel-module-lnbh25-6.1.38-fslc+g085682f3fc7e
lnbh25 kernel module; ST LNBH25 driver

%package -n kernel-module-lnbh29-6.1.38-fslc+g085682f3fc7e
Summary: lnbh29 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-lnbh29

%description -n kernel-module-lnbh29-6.1.38-fslc+g085682f3fc7e
lnbh29 kernel module; STMicroelectronics LNBH29 driver

%package -n kernel-module-lnbp21-6.1.38-fslc+g085682f3fc7e
Summary: lnbp21 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-lnbp21

%description -n kernel-module-lnbp21-6.1.38-fslc+g085682f3fc7e
lnbp21 kernel module; Driver for lnb supply and control ic lnbp21, lnbh24

%package -n kernel-module-lnbp22-6.1.38-fslc+g085682f3fc7e
Summary: lnbp22 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-lnbp22

%description -n kernel-module-lnbp22-6.1.38-fslc+g085682f3fc7e
lnbp22 kernel module; Driver for lnb supply and control ic lnbp22

%package -n kernel-module-m88ds3103-6.1.38-fslc+g085682f3fc7e
Summary: m88ds3103 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-m88ds3103

%description -n kernel-module-m88ds3103-6.1.38-fslc+g085682f3fc7e
m88ds3103 kernel module; Montage Technology M88DS3103 DVB-S/S2 demodulator
driver

%package -n kernel-module-m88rs2000-6.1.38-fslc+g085682f3fc7e
Summary: m88rs2000 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-m88rs2000

%description -n kernel-module-m88rs2000-6.1.38-fslc+g085682f3fc7e
m88rs2000 kernel module; M88RS2000 DVB-S Demodulator driver

%package -n kernel-module-mb86a16-6.1.38-fslc+g085682f3fc7e
Summary: mb86a16 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-mb86a16

%description -n kernel-module-mb86a16-6.1.38-fslc+g085682f3fc7e
mb86a16 kernel module

%package -n kernel-module-mb86a20s-6.1.38-fslc+g085682f3fc7e
Summary: mb86a20s kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-mb86a20s

%description -n kernel-module-mb86a20s-6.1.38-fslc+g085682f3fc7e
mb86a20s kernel module; DVB Frontend module for Fujitsu mb86A20s hardware

%package -n kernel-module-mn88443x-6.1.38-fslc+g085682f3fc7e
Summary: mn88443x kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-mn88443x

%description -n kernel-module-mn88443x-6.1.38-fslc+g085682f3fc7e
mn88443x kernel module; Socionext MN88443x series demodulator driver.

%package -n kernel-module-mn88472-6.1.38-fslc+g085682f3fc7e
Summary: mn88472 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-mn88472

%description -n kernel-module-mn88472-6.1.38-fslc+g085682f3fc7e
mn88472 kernel module; Panasonic MN88472 DVB-T/T2/C demodulator driver

%package -n kernel-module-mn88473-6.1.38-fslc+g085682f3fc7e
Summary: mn88473 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-mn88473

%description -n kernel-module-mn88473-6.1.38-fslc+g085682f3fc7e
mn88473 kernel module; Panasonic MN88473 DVB-T/T2/C demodulator driver

%package -n kernel-module-mt312-6.1.38-fslc+g085682f3fc7e
Summary: mt312 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-mt312

%description -n kernel-module-mt312-6.1.38-fslc+g085682f3fc7e
mt312 kernel module; Zarlink VP310/MT312/ZL10313 DVB-S Demodulator driver

%package -n kernel-module-mt352-6.1.38-fslc+g085682f3fc7e
Summary: mt352 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-mt352

%description -n kernel-module-mt352-6.1.38-fslc+g085682f3fc7e
mt352 kernel module; Zarlink MT352 DVB-T Demodulator driver

%package -n kernel-module-mxl5xx-6.1.38-fslc+g085682f3fc7e
Summary: mxl5xx kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-mxl5xx

%description -n kernel-module-mxl5xx-6.1.38-fslc+g085682f3fc7e
mxl5xx kernel module; MaxLinear MxL5xx DVB-S/S2 tuner-demodulator driver

%package -n kernel-module-mxl692-6.1.38-fslc+g085682f3fc7e
Summary: mxl692 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-mxl692

%description -n kernel-module-mxl692-6.1.38-fslc+g085682f3fc7e
mxl692 kernel module; MaxLinear MxL692 demodulator/tuner driver

%package -n kernel-module-nxt200x-6.1.38-fslc+g085682f3fc7e
Summary: nxt200x kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-nxt200x

%description -n kernel-module-nxt200x-6.1.38-fslc+g085682f3fc7e
nxt200x kernel module; NXT200X (ATSC 8VSB & ITU-T J.83 AnnexB 64/256 QAM)
Demodulator Driver

%package -n kernel-module-nxt6000-6.1.38-fslc+g085682f3fc7e
Summary: nxt6000 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-nxt6000

%description -n kernel-module-nxt6000-6.1.38-fslc+g085682f3fc7e
nxt6000 kernel module; NxtWave NXT6000 DVB-T demodulator driver

%package -n kernel-module-or51132-6.1.38-fslc+g085682f3fc7e
Summary: or51132 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-or51132

%description -n kernel-module-or51132-6.1.38-fslc+g085682f3fc7e
or51132 kernel module; OR51132 ATSC [pcHDTV HD-3000] (8VSB & ITU J83 AnnexB
FEC QAM64/256) Demodulator Driver

%package -n kernel-module-or51211-6.1.38-fslc+g085682f3fc7e
Summary: or51211 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-or51211

%description -n kernel-module-or51211-6.1.38-fslc+g085682f3fc7e
or51211 kernel module; Oren OR51211 VSB [pcHDTV HD-2000] Demodulator Driver

%package -n kernel-module-rtl2830-6.1.38-fslc+g085682f3fc7e
Summary: rtl2830 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-rtl2830

%description -n kernel-module-rtl2830-6.1.38-fslc+g085682f3fc7e
rtl2830 kernel module; Realtek RTL2830 DVB-T demodulator driver

%package -n kernel-module-rtl2832-6.1.38-fslc+g085682f3fc7e
Summary: rtl2832 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-rtl2832

%description -n kernel-module-rtl2832-6.1.38-fslc+g085682f3fc7e
rtl2832 kernel module; Realtek RTL2832 DVB-T demodulator driver

%package -n kernel-module-rtl2832-sdr-6.1.38-fslc+g085682f3fc7e
Summary: rtl2832-sdr kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-rtl2832-sdr

%description -n kernel-module-rtl2832-sdr-6.1.38-fslc+g085682f3fc7e
rtl2832-sdr kernel module; Realtek RTL2832 SDR driver

%package -n kernel-module-s5h1409-6.1.38-fslc+g085682f3fc7e
Summary: s5h1409 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-s5h1409

%description -n kernel-module-s5h1409-6.1.38-fslc+g085682f3fc7e
s5h1409 kernel module; Samsung S5H1409 QAM-B/ATSC Demodulator driver

%package -n kernel-module-s5h1411-6.1.38-fslc+g085682f3fc7e
Summary: s5h1411 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-s5h1411

%description -n kernel-module-s5h1411-6.1.38-fslc+g085682f3fc7e
s5h1411 kernel module; Samsung S5H1411 QAM-B/ATSC Demodulator driver

%package -n kernel-module-s5h1420-6.1.38-fslc+g085682f3fc7e
Summary: s5h1420 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-s5h1420

%description -n kernel-module-s5h1420-6.1.38-fslc+g085682f3fc7e
s5h1420 kernel module; Samsung S5H1420/PnpNetwork PN1010 DVB-S Demodulator
driver

%package -n kernel-module-s5h1432-6.1.38-fslc+g085682f3fc7e
Summary: s5h1432 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-s5h1432

%description -n kernel-module-s5h1432-6.1.38-fslc+g085682f3fc7e
s5h1432 kernel module; Samsung s5h1432 DVB-T Demodulator driver

%package -n kernel-module-s921-6.1.38-fslc+g085682f3fc7e
Summary: s921 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-s921

%description -n kernel-module-s921-6.1.38-fslc+g085682f3fc7e
s921 kernel module; DVB Frontend module for Sharp S921 hardware

%package -n kernel-module-si2165-6.1.38-fslc+g085682f3fc7e
Summary: si2165 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-si2165

%description -n kernel-module-si2165-6.1.38-fslc+g085682f3fc7e
si2165 kernel module; Silicon Labs Si2165 DVB-C/-T Demodulator driver

%package -n kernel-module-si2168-6.1.38-fslc+g085682f3fc7e
Summary: si2168 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-si2168

%description -n kernel-module-si2168-6.1.38-fslc+g085682f3fc7e
si2168 kernel module; Silicon Labs Si2168 DVB-T/T2/C demodulator driver

%package -n kernel-module-si21xx-6.1.38-fslc+g085682f3fc7e
Summary: si21xx kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-si21xx

%description -n kernel-module-si21xx-6.1.38-fslc+g085682f3fc7e
si21xx kernel module; SL SI21XX DVB Demodulator driver

%package -n kernel-module-sp2-6.1.38-fslc+g085682f3fc7e
Summary: sp2 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-sp2

%description -n kernel-module-sp2-6.1.38-fslc+g085682f3fc7e
sp2 kernel module; CIMaX SP2/HF CI driver

%package -n kernel-module-sp887x-6.1.38-fslc+g085682f3fc7e
Summary: sp887x kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-sp887x

%description -n kernel-module-sp887x-6.1.38-fslc+g085682f3fc7e
sp887x kernel module; Spase sp887x DVB-T demodulator driver

%package -n kernel-module-stb0899-6.1.38-fslc+g085682f3fc7e
Summary: stb0899 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-stb0899

%description -n kernel-module-stb0899-6.1.38-fslc+g085682f3fc7e
stb0899 kernel module; STB0899 Multi-Std frontend

%package -n kernel-module-stb6000-6.1.38-fslc+g085682f3fc7e
Summary: stb6000 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-stb6000

%description -n kernel-module-stb6000-6.1.38-fslc+g085682f3fc7e
stb6000 kernel module; DVB STB6000 driver

%package -n kernel-module-stb6100-6.1.38-fslc+g085682f3fc7e
Summary: stb6100 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-stb6100

%description -n kernel-module-stb6100-6.1.38-fslc+g085682f3fc7e
stb6100 kernel module; STB6100 Silicon tuner

%package -n kernel-module-stv0288-6.1.38-fslc+g085682f3fc7e
Summary: stv0288 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-stv0288

%description -n kernel-module-stv0288-6.1.38-fslc+g085682f3fc7e
stv0288 kernel module; ST STV0288 DVB Demodulator driver

%package -n kernel-module-stv0297-6.1.38-fslc+g085682f3fc7e
Summary: stv0297 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-stv0297

%description -n kernel-module-stv0297-6.1.38-fslc+g085682f3fc7e
stv0297 kernel module; ST STV0297 DVB-C Demodulator driver

%package -n kernel-module-stv0299-6.1.38-fslc+g085682f3fc7e
Summary: stv0299 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-stv0299

%description -n kernel-module-stv0299-6.1.38-fslc+g085682f3fc7e
stv0299 kernel module; ST STV0299 DVB Demodulator driver

%package -n kernel-module-stv0367-6.1.38-fslc+g085682f3fc7e
Summary: stv0367 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-stv0367

%description -n kernel-module-stv0367-6.1.38-fslc+g085682f3fc7e
stv0367 kernel module; ST STV0367 DVB-C/T demodulator driver

%package -n kernel-module-stv0900-6.1.38-fslc+g085682f3fc7e
Summary: stv0900 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-stv0900

%description -n kernel-module-stv0900-6.1.38-fslc+g085682f3fc7e
stv0900 kernel module; ST STV0900 frontend

%package -n kernel-module-stv090x-6.1.38-fslc+g085682f3fc7e
Summary: stv090x kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-stv090x

%description -n kernel-module-stv090x-6.1.38-fslc+g085682f3fc7e
stv090x kernel module; STV090x Multi-Std Broadcast frontend

%package -n kernel-module-stv0910-6.1.38-fslc+g085682f3fc7e
Summary: stv0910 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-stv0910

%description -n kernel-module-stv0910-6.1.38-fslc+g085682f3fc7e
stv0910 kernel module; ST STV0910 multistandard frontend driver

%package -n kernel-module-stv6110-6.1.38-fslc+g085682f3fc7e
Summary: stv6110 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-stv6110

%description -n kernel-module-stv6110-6.1.38-fslc+g085682f3fc7e
stv6110 kernel module; ST STV6110 driver

%package -n kernel-module-stv6110x-6.1.38-fslc+g085682f3fc7e
Summary: stv6110x kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-stv6110x

%description -n kernel-module-stv6110x-6.1.38-fslc+g085682f3fc7e
stv6110x kernel module; STV6110x Silicon tuner

%package -n kernel-module-stv6111-6.1.38-fslc+g085682f3fc7e
Summary: stv6111 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-stv6111

%description -n kernel-module-stv6111-6.1.38-fslc+g085682f3fc7e
stv6111 kernel module; ST STV6111 satellite tuner driver

%package -n kernel-module-tc90522-6.1.38-fslc+g085682f3fc7e
Summary: tc90522 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tc90522

%description -n kernel-module-tc90522-6.1.38-fslc+g085682f3fc7e
tc90522 kernel module; Toshiba TC90522 frontend

%package -n kernel-module-tda10021-6.1.38-fslc+g085682f3fc7e
Summary: tda10021 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tda10021

%description -n kernel-module-tda10021-6.1.38-fslc+g085682f3fc7e
tda10021 kernel module; Philips TDA10021 DVB-C demodulator driver

%package -n kernel-module-tda10023-6.1.38-fslc+g085682f3fc7e
Summary: tda10023 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tda10023

%description -n kernel-module-tda10023-6.1.38-fslc+g085682f3fc7e
tda10023 kernel module; Philips TDA10023 DVB-C demodulator driver

%package -n kernel-module-tda10048-6.1.38-fslc+g085682f3fc7e
Summary: tda10048 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tda10048

%description -n kernel-module-tda10048-6.1.38-fslc+g085682f3fc7e
tda10048 kernel module; NXP TDA10048HN DVB-T Demodulator driver

%package -n kernel-module-tda1004x-6.1.38-fslc+g085682f3fc7e
Summary: tda1004x kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tda1004x

%description -n kernel-module-tda1004x-6.1.38-fslc+g085682f3fc7e
tda1004x kernel module; Philips TDA10045H & TDA10046H DVB-T Demodulator

%package -n kernel-module-tda10071-6.1.38-fslc+g085682f3fc7e
Summary: tda10071 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tda10071

%description -n kernel-module-tda10071-6.1.38-fslc+g085682f3fc7e
tda10071 kernel module; NXP TDA10071 DVB-S/S2 demodulator driver

%package -n kernel-module-tda10086-6.1.38-fslc+g085682f3fc7e
Summary: tda10086 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tda10086

%description -n kernel-module-tda10086-6.1.38-fslc+g085682f3fc7e
tda10086 kernel module; Philips TDA10086 DVB-S Demodulator

%package -n kernel-module-tda18271c2dd-6.1.38-fslc+g085682f3fc7e
Summary: tda18271c2dd kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tda18271c2dd

%description -n kernel-module-tda18271c2dd-6.1.38-fslc+g085682f3fc7e
tda18271c2dd kernel module; TDA18271C2 driver

%package -n kernel-module-tda665x-6.1.38-fslc+g085682f3fc7e
Summary: tda665x kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tda665x

%description -n kernel-module-tda665x-6.1.38-fslc+g085682f3fc7e
tda665x kernel module; TDA665x driver

%package -n kernel-module-tda8083-6.1.38-fslc+g085682f3fc7e
Summary: tda8083 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tda8083

%description -n kernel-module-tda8083-6.1.38-fslc+g085682f3fc7e
tda8083 kernel module; Philips TDA8083 DVB-S Demodulator

%package -n kernel-module-tda8261-6.1.38-fslc+g085682f3fc7e
Summary: tda8261 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tda8261

%description -n kernel-module-tda8261-6.1.38-fslc+g085682f3fc7e
tda8261 kernel module; TDA8261 8PSK/QPSK Tuner

%package -n kernel-module-tda826x-6.1.38-fslc+g085682f3fc7e
Summary: tda826x kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tda826x

%description -n kernel-module-tda826x-6.1.38-fslc+g085682f3fc7e
tda826x kernel module; DVB TDA826x driver

%package -n kernel-module-ts2020-6.1.38-fslc+g085682f3fc7e
Summary: ts2020 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-ts2020

%description -n kernel-module-ts2020-6.1.38-fslc+g085682f3fc7e
ts2020 kernel module; Montage Technology TS2020 - Silicon tuner driver
module

%package -n kernel-module-tua6100-6.1.38-fslc+g085682f3fc7e
Summary: tua6100 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tua6100

%description -n kernel-module-tua6100-6.1.38-fslc+g085682f3fc7e
tua6100 kernel module; DVB tua6100 driver

%package -n kernel-module-ves1820-6.1.38-fslc+g085682f3fc7e
Summary: ves1820 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-ves1820

%description -n kernel-module-ves1820-6.1.38-fslc+g085682f3fc7e
ves1820 kernel module; VLSI VES1820 DVB-C Demodulator driver

%package -n kernel-module-ves1x93-6.1.38-fslc+g085682f3fc7e
Summary: ves1x93 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-ves1x93

%description -n kernel-module-ves1x93-6.1.38-fslc+g085682f3fc7e
ves1x93 kernel module; VLSI VES1x93 DVB-S Demodulator driver

%package -n kernel-module-zd1301-demod-6.1.38-fslc+g085682f3fc7e
Summary: zd1301-demod kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-zd1301-demod

%description -n kernel-module-zd1301-demod-6.1.38-fslc+g085682f3fc7e
zd1301-demod kernel module; ZyDAS ZD1301 demodulator driver

%package -n kernel-module-zl10036-6.1.38-fslc+g085682f3fc7e
Summary: zl10036 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-zl10036

%description -n kernel-module-zl10036-6.1.38-fslc+g085682f3fc7e
zl10036 kernel module; DVB ZL10036 driver

%package -n kernel-module-zl10039-6.1.38-fslc+g085682f3fc7e
Summary: zl10039 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-zl10039

%description -n kernel-module-zl10039-6.1.38-fslc+g085682f3fc7e
zl10039 kernel module; Zarlink ZL10039 DVB-S tuner driver

%package -n kernel-module-zl10353-6.1.38-fslc+g085682f3fc7e
Summary: zl10353 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-zl10353

%description -n kernel-module-zl10353-6.1.38-fslc+g085682f3fc7e
zl10353 kernel module; Zarlink ZL10353 DVB-T demodulator driver

%package -n kernel-module-cxd2880-6.1.38-fslc+g085682f3fc7e
Summary: cxd2880 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-cxd2880

%description -n kernel-module-cxd2880-6.1.38-fslc+g085682f3fc7e
cxd2880 kernel module; Sony CXD2880 DVB-T2/T tuner + demod driver

%package -n kernel-module-drx39xyj-6.1.38-fslc+g085682f3fc7e
Summary: drx39xyj kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-drx39xyj

%description -n kernel-module-drx39xyj-6.1.38-fslc+g085682f3fc7e
drx39xyj kernel module; Micronas DRX39xxj Frontend

%package -n kernel-module-adv7180-6.1.38-fslc+g085682f3fc7e
Summary: adv7180 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-adv7180

%description -n kernel-module-adv7180-6.1.38-fslc+g085682f3fc7e
adv7180 kernel module; Analog Devices ADV7180 video decoder driver

%package -n kernel-module-ov2680-6.1.38-fslc+g085682f3fc7e
Summary: ov2680 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-ov2680

%description -n kernel-module-ov2680-6.1.38-fslc+g085682f3fc7e
ov2680 kernel module; OV2680 CMOS Image Sensor driver

%package -n kernel-module-ov5640-6.1.38-fslc+g085682f3fc7e
Summary: ov5640 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-ov5640

%description -n kernel-module-ov5640-6.1.38-fslc+g085682f3fc7e
ov5640 kernel module; OV5640 MIPI Camera Subdev Driver

%package -n kernel-module-ov5645-6.1.38-fslc+g085682f3fc7e
Summary: ov5645 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-ov5645

%description -n kernel-module-ov5645-6.1.38-fslc+g085682f3fc7e
ov5645 kernel module; Omnivision OV5645 Camera Driver

%package -n kernel-module-coda-vpu-6.1.38-fslc+g085682f3fc7e
Summary: coda-vpu kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-imx-vdoa-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-v4l2-jpeg-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-imx-vdoa-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-v4l2-jpeg-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-imx-vdoa-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-v4l2-jpeg-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-coda-vpu

%description -n kernel-module-coda-vpu-6.1.38-fslc+g085682f3fc7e
coda-vpu kernel module; Coda multi-standard codec V4L2 driver

%package -n kernel-module-imx-vdoa-6.1.38-fslc+g085682f3fc7e
Summary: imx-vdoa kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-imx-vdoa

%description -n kernel-module-imx-vdoa-6.1.38-fslc+g085682f3fc7e
imx-vdoa kernel module; Video Data Order Adapter

%package -n kernel-module-cxd2880-spi-6.1.38-fslc+g085682f3fc7e
Summary: cxd2880-spi kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-cxd2880-spi

%description -n kernel-module-cxd2880-spi-6.1.38-fslc+g085682f3fc7e
cxd2880-spi kernel module; Sony CXD2880 DVB-T2/T tuner + demod driver SPI
adapter

%package -n kernel-module-e4000-6.1.38-fslc+g085682f3fc7e
Summary: e4000 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-e4000

%description -n kernel-module-e4000-6.1.38-fslc+g085682f3fc7e
e4000 kernel module; Elonics E4000 silicon tuner driver

%package -n kernel-module-fc0011-6.1.38-fslc+g085682f3fc7e
Summary: fc0011 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-fc0011

%description -n kernel-module-fc0011-6.1.38-fslc+g085682f3fc7e
fc0011 kernel module; Fitipower FC0011 silicon tuner driver

%package -n kernel-module-fc0012-6.1.38-fslc+g085682f3fc7e
Summary: fc0012 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-fc0012

%description -n kernel-module-fc0012-6.1.38-fslc+g085682f3fc7e
fc0012 kernel module; Fitipower FC0012 silicon tuner driver

%package -n kernel-module-fc0013-6.1.38-fslc+g085682f3fc7e
Summary: fc0013 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-fc0013

%description -n kernel-module-fc0013-6.1.38-fslc+g085682f3fc7e
fc0013 kernel module; Fitipower FC0013 silicon tuner driver

%package -n kernel-module-fc2580-6.1.38-fslc+g085682f3fc7e
Summary: fc2580 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-fc2580

%description -n kernel-module-fc2580-6.1.38-fslc+g085682f3fc7e
fc2580 kernel module; FCI FC2580 silicon tuner driver

%package -n kernel-module-it913x-6.1.38-fslc+g085682f3fc7e
Summary: it913x kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-it913x

%description -n kernel-module-it913x-6.1.38-fslc+g085682f3fc7e
it913x kernel module; ITE IT913X silicon tuner driver

%package -n kernel-module-m88rs6000t-6.1.38-fslc+g085682f3fc7e
Summary: m88rs6000t kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-m88rs6000t

%description -n kernel-module-m88rs6000t-6.1.38-fslc+g085682f3fc7e
m88rs6000t kernel module; Montage M88RS6000 internal tuner driver

%package -n kernel-module-max2165-6.1.38-fslc+g085682f3fc7e
Summary: max2165 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-max2165

%description -n kernel-module-max2165-6.1.38-fslc+g085682f3fc7e
max2165 kernel module; Maxim MAX2165 silicon tuner driver

%package -n kernel-module-mc44s803-6.1.38-fslc+g085682f3fc7e
Summary: mc44s803 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-mc44s803

%description -n kernel-module-mc44s803-6.1.38-fslc+g085682f3fc7e
mc44s803 kernel module; Freescale MC44S803 silicon tuner driver

%package -n kernel-module-msi001-6.1.38-fslc+g085682f3fc7e
Summary: msi001 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-msi001

%description -n kernel-module-msi001-6.1.38-fslc+g085682f3fc7e
msi001 kernel module; Mirics MSi001

%package -n kernel-module-mt2060-6.1.38-fslc+g085682f3fc7e
Summary: mt2060 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-mt2060

%description -n kernel-module-mt2060-6.1.38-fslc+g085682f3fc7e
mt2060 kernel module; Microtune MT2060 silicon tuner driver

%package -n kernel-module-mt2063-6.1.38-fslc+g085682f3fc7e
Summary: mt2063 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-mt2063

%description -n kernel-module-mt2063-6.1.38-fslc+g085682f3fc7e
mt2063 kernel module; MT2063 Silicon tuner

%package -n kernel-module-mt20xx-6.1.38-fslc+g085682f3fc7e
Summary: mt20xx kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-mt20xx

%description -n kernel-module-mt20xx-6.1.38-fslc+g085682f3fc7e
mt20xx kernel module; Microtune tuner driver

%package -n kernel-module-mt2131-6.1.38-fslc+g085682f3fc7e
Summary: mt2131 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-mt2131

%description -n kernel-module-mt2131-6.1.38-fslc+g085682f3fc7e
mt2131 kernel module; Microtune MT2131 silicon tuner driver

%package -n kernel-module-mt2266-6.1.38-fslc+g085682f3fc7e
Summary: mt2266 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-mt2266

%description -n kernel-module-mt2266-6.1.38-fslc+g085682f3fc7e
mt2266 kernel module; Microtune MT2266 silicon tuner driver

%package -n kernel-module-mxl301rf-6.1.38-fslc+g085682f3fc7e
Summary: mxl301rf kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-mxl301rf

%description -n kernel-module-mxl301rf-6.1.38-fslc+g085682f3fc7e
mxl301rf kernel module; MaxLinear MXL301RF tuner

%package -n kernel-module-mxl5005s-6.1.38-fslc+g085682f3fc7e
Summary: mxl5005s kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-mxl5005s

%description -n kernel-module-mxl5005s-6.1.38-fslc+g085682f3fc7e
mxl5005s kernel module; MaxLinear MXL5005S silicon tuner driver

%package -n kernel-module-mxl5007t-6.1.38-fslc+g085682f3fc7e
Summary: mxl5007t kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-mxl5007t

%description -n kernel-module-mxl5007t-6.1.38-fslc+g085682f3fc7e
mxl5007t kernel module; MaxLinear MxL5007T Silicon IC tuner driver

%package -n kernel-module-qm1d1b0004-6.1.38-fslc+g085682f3fc7e
Summary: qm1d1b0004 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-qm1d1b0004

%description -n kernel-module-qm1d1b0004-6.1.38-fslc+g085682f3fc7e
qm1d1b0004 kernel module; Sharp QM1D1B0004

%package -n kernel-module-qm1d1c0042-6.1.38-fslc+g085682f3fc7e
Summary: qm1d1c0042 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-qm1d1c0042

%description -n kernel-module-qm1d1c0042-6.1.38-fslc+g085682f3fc7e
qm1d1c0042 kernel module; Sharp QM1D1C0042 tuner

%package -n kernel-module-qt1010-6.1.38-fslc+g085682f3fc7e
Summary: qt1010 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-qt1010

%description -n kernel-module-qt1010-6.1.38-fslc+g085682f3fc7e
qt1010 kernel module; Quantek QT1010 silicon tuner driver

%package -n kernel-module-r820t-6.1.38-fslc+g085682f3fc7e
Summary: r820t kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-r820t

%description -n kernel-module-r820t-6.1.38-fslc+g085682f3fc7e
r820t kernel module; Rafael Micro r820t silicon tuner driver

%package -n kernel-module-si2157-6.1.38-fslc+g085682f3fc7e
Summary: si2157 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-si2157

%description -n kernel-module-si2157-6.1.38-fslc+g085682f3fc7e
si2157 kernel module; Silicon Labs Si2141/Si2146/2147/2148/2157/2158
silicon tuner driver

%package -n kernel-module-tda18212-6.1.38-fslc+g085682f3fc7e
Summary: tda18212 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tda18212

%description -n kernel-module-tda18212-6.1.38-fslc+g085682f3fc7e
tda18212 kernel module; NXP TDA18212HN silicon tuner driver

%package -n kernel-module-tda18218-6.1.38-fslc+g085682f3fc7e
Summary: tda18218 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tda18218

%description -n kernel-module-tda18218-6.1.38-fslc+g085682f3fc7e
tda18218 kernel module; NXP TDA18218HN silicon tuner driver

%package -n kernel-module-tda18250-6.1.38-fslc+g085682f3fc7e
Summary: tda18250 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tda18250

%description -n kernel-module-tda18250-6.1.38-fslc+g085682f3fc7e
tda18250 kernel module; NXP TDA18250 silicon tuner driver

%package -n kernel-module-tda18271-6.1.38-fslc+g085682f3fc7e
Summary: tda18271 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tda18271

%description -n kernel-module-tda18271-6.1.38-fslc+g085682f3fc7e
tda18271 kernel module; NXP TDA18271HD analog / digital tuner driver

%package -n kernel-module-tda827x-6.1.38-fslc+g085682f3fc7e
Summary: tda827x kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tda827x

%description -n kernel-module-tda827x-6.1.38-fslc+g085682f3fc7e
tda827x kernel module; DVB TDA827x driver

%package -n kernel-module-tda8290-6.1.38-fslc+g085682f3fc7e
Summary: tda8290 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tda8290

%description -n kernel-module-tda8290-6.1.38-fslc+g085682f3fc7e
tda8290 kernel module; Philips/NXP TDA8290/TDA8295 analog IF demodulator
driver

%package -n kernel-module-tda9887-6.1.38-fslc+g085682f3fc7e
Summary: tda9887 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tda9887

%description -n kernel-module-tda9887-6.1.38-fslc+g085682f3fc7e
tda9887 kernel module

%package -n kernel-module-tea5761-6.1.38-fslc+g085682f3fc7e
Summary: tea5761 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tea5761

%description -n kernel-module-tea5761-6.1.38-fslc+g085682f3fc7e
tea5761 kernel module; Philips TEA5761 FM tuner driver

%package -n kernel-module-tea5767-6.1.38-fslc+g085682f3fc7e
Summary: tea5767 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tea5767

%description -n kernel-module-tea5767-6.1.38-fslc+g085682f3fc7e
tea5767 kernel module; Philips TEA5767 FM tuner driver

%package -n kernel-module-tua9001-6.1.38-fslc+g085682f3fc7e
Summary: tua9001 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tua9001

%description -n kernel-module-tua9001-6.1.38-fslc+g085682f3fc7e
tua9001 kernel module; Infineon TUA9001 silicon tuner driver

%package -n kernel-module-tuner-simple-6.1.38-fslc+g085682f3fc7e
Summary: tuner-simple kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-tuner-types-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-tuner-types-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-tuner-types-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tuner-simple

%description -n kernel-module-tuner-simple-6.1.38-fslc+g085682f3fc7e
tuner-simple kernel module; Simple 4-control-bytes style tuner driver

%package -n kernel-module-tuner-types-6.1.38-fslc+g085682f3fc7e
Summary: tuner-types kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-tuner-types

%description -n kernel-module-tuner-types-6.1.38-fslc+g085682f3fc7e
tuner-types kernel module; Simple tuner device type database

%package -n kernel-module-xc2028-6.1.38-fslc+g085682f3fc7e
Summary: xc2028 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-xc2028

%description -n kernel-module-xc2028-6.1.38-fslc+g085682f3fc7e
xc2028 kernel module; Xceive xc2028/xc3028 tuner driver

%package -n kernel-module-xc4000-6.1.38-fslc+g085682f3fc7e
Summary: xc4000 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-xc4000

%description -n kernel-module-xc4000-6.1.38-fslc+g085682f3fc7e
xc4000 kernel module; Xceive xc4000 silicon tuner driver

%package -n kernel-module-xc5000-6.1.38-fslc+g085682f3fc7e
Summary: xc5000 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-xc5000

%description -n kernel-module-xc5000-6.1.38-fslc+g085682f3fc7e
xc5000 kernel module; Xceive xc5000 silicon tuner driver

%package -n kernel-module-uvcvideo-6.1.38-fslc+g085682f3fc7e
Summary: uvcvideo kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-uvcvideo

%description -n kernel-module-uvcvideo-6.1.38-fslc+g085682f3fc7e
uvcvideo kernel module; USB Video Class driver

%package -n kernel-module-v4l2-jpeg-6.1.38-fslc+g085682f3fc7e
Summary: v4l2-jpeg kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-v4l2-jpeg

%description -n kernel-module-v4l2-jpeg-6.1.38-fslc+g085682f3fc7e
v4l2-jpeg kernel module; V4L2 JPEG header parser helpers

%package -n kernel-module-cdc-eem-6.1.38-fslc+g085682f3fc7e
Summary: cdc-eem kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-cdc-eem

%description -n kernel-module-cdc-eem-6.1.38-fslc+g085682f3fc7e
cdc-eem kernel module; USB CDC EEM

%package -n kernel-module-pegasus-6.1.38-fslc+g085682f3fc7e
Summary: pegasus kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-pegasus

%description -n kernel-module-pegasus-6.1.38-fslc+g085682f3fc7e
pegasus kernel module; Pegasus/Pegasus II USB Ethernet driver

%package -n kernel-module-rtl8150-6.1.38-fslc+g085682f3fc7e
Summary: rtl8150 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-rtl8150

%description -n kernel-module-rtl8150-6.1.38-fslc+g085682f3fc7e
rtl8150 kernel module; rtl8150 based usb-ethernet driver

%package -n kernel-module-ath-6.1.38-fslc+g085682f3fc7e
Summary: ath kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-ath

%description -n kernel-module-ath-6.1.38-fslc+g085682f3fc7e
ath kernel module; Shared library for Atheros wireless LAN cards.

%package -n kernel-module-ath10k-core-6.1.38-fslc+g085682f3fc7e
Summary: ath10k-core kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-ath-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-ath-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-ath-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-ath10k-core

%description -n kernel-module-ath10k-core-6.1.38-fslc+g085682f3fc7e
ath10k-core kernel module; Core module for Qualcomm Atheros 802.11ac
wireless LAN cards.

%package -n kernel-module-ath10k-sdio-6.1.38-fslc+g085682f3fc7e
Summary: ath10k-sdio kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-ath10k-core-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-ath10k-core-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-ath10k-core-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-ath10k-sdio

%description -n kernel-module-ath10k-sdio-6.1.38-fslc+g085682f3fc7e
ath10k-sdio kernel module; Driver support for Qualcomm Atheros 802.11ac
WLAN SDIO devices

%package -n kernel-module-brcmfmac-6.1.38-fslc+g085682f3fc7e
Summary: brcmfmac kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-brcmutil-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-brcmutil-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-brcmutil-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-brcmfmac

%description -n kernel-module-brcmfmac-6.1.38-fslc+g085682f3fc7e
brcmfmac kernel module; Broadcom 802.11 wireless LAN fullmac driver.

%package -n kernel-module-brcmutil-6.1.38-fslc+g085682f3fc7e
Summary: brcmutil kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-brcmutil

%description -n kernel-module-brcmutil-6.1.38-fslc+g085682f3fc7e
brcmutil kernel module; Broadcom 802.11n wireless LAN driver utilities.

%package -n kernel-module-mwifiex-6.1.38-fslc+g085682f3fc7e
Summary: mwifiex kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-mwifiex

%description -n kernel-module-mwifiex-6.1.38-fslc+g085682f3fc7e
mwifiex kernel module; Marvell WiFi-Ex Driver version 1.0

%package -n kernel-module-mwifiex-pcie-6.1.38-fslc+g085682f3fc7e
Summary: mwifiex-pcie kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-mwifiex-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-mwifiex-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-mwifiex-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-mwifiex-pcie

%description -n kernel-module-mwifiex-pcie-6.1.38-fslc+g085682f3fc7e
mwifiex-pcie kernel module; Marvell WiFi-Ex PCI-Express Driver version 1.0

%package -n kernel-module-mwifiex-sdio-6.1.38-fslc+g085682f3fc7e
Summary: mwifiex-sdio kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-mwifiex-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-mwifiex-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-mwifiex-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-mwifiex-sdio

%description -n kernel-module-mwifiex-sdio-6.1.38-fslc+g085682f3fc7e
mwifiex-sdio kernel module; Marvell WiFi-Ex SDIO Driver version 1.0

%package -n kernel-module-wl12xx-6.1.38-fslc+g085682f3fc7e
Summary: wl12xx kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-wlcore-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-wlcore-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-wlcore-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-wl12xx

%description -n kernel-module-wl12xx-6.1.38-fslc+g085682f3fc7e
wl12xx kernel module

%package -n kernel-module-wl18xx-6.1.38-fslc+g085682f3fc7e
Summary: wl18xx kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-wlcore-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-wlcore-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-wlcore-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-wl18xx

%description -n kernel-module-wl18xx-6.1.38-fslc+g085682f3fc7e
wl18xx kernel module

%package -n kernel-module-wlcore-6.1.38-fslc+g085682f3fc7e
Summary: wlcore kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-wlcore

%description -n kernel-module-wlcore-6.1.38-fslc+g085682f3fc7e
wlcore kernel module

%package -n kernel-module-wlcore-sdio-6.1.38-fslc+g085682f3fc7e
Summary: wlcore-sdio kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-wlcore-sdio

%description -n kernel-module-wlcore-sdio-6.1.38-fslc+g085682f3fc7e
wlcore-sdio kernel module

%package -n kernel-module-rn5t618-power-6.1.38-fslc+g085682f3fc7e
Summary: rn5t618-power kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-rn5t618-power

%description -n kernel-module-rn5t618-power-6.1.38-fslc+g085682f3fc7e
rn5t618-power kernel module; Power supply driver for RICOH RN5T618

%package -n kernel-module-siox-bus-gpio-6.1.38-fslc+g085682f3fc7e
Summary: siox-bus-gpio kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-siox-core-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-siox-core-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-siox-core-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-siox-bus-gpio

%description -n kernel-module-siox-bus-gpio-6.1.38-fslc+g085682f3fc7e
siox-bus-gpio kernel module

%package -n kernel-module-siox-core-6.1.38-fslc+g085682f3fc7e
Summary: siox-core kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-siox-core

%description -n kernel-module-siox-core-6.1.38-fslc+g085682f3fc7e
siox-core kernel module; Eckelmann SIOX driver core

%package -n kernel-module-cdc-acm-6.1.38-fslc+g085682f3fc7e
Summary: cdc-acm kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-cdc-acm

%description -n kernel-module-cdc-acm-6.1.38-fslc+g085682f3fc7e
cdc-acm kernel module; USB Abstract Control Model driver for USB modems and
ISDN adapters

%package -n kernel-module-g-audio-6.1.38-fslc+g085682f3fc7e
Summary: g-audio kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-g-audio

%description -n kernel-module-g-audio-6.1.38-fslc+g085682f3fc7e
g-audio kernel module; Linux USB Audio Gadget

%package -n kernel-module-g-ether-6.1.38-fslc+g085682f3fc7e
Summary: g-ether kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-g-ether

%description -n kernel-module-g-ether-6.1.38-fslc+g085682f3fc7e
g-ether kernel module; RNDIS/Ethernet Gadget

%package -n kernel-module-g-ffs-6.1.38-fslc+g085682f3fc7e
Summary: g-ffs kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-g-ffs

%description -n kernel-module-g-ffs-6.1.38-fslc+g085682f3fc7e
g-ffs kernel module; USB Function Filesystem

%package -n kernel-module-g-mass-storage-6.1.38-fslc+g085682f3fc7e
Summary: g-mass-storage kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-g-mass-storage

%description -n kernel-module-g-mass-storage-6.1.38-fslc+g085682f3fc7e
g-mass-storage kernel module; Mass Storage Gadget

%package -n kernel-module-g-ncm-6.1.38-fslc+g085682f3fc7e
Summary: g-ncm kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-g-ncm

%description -n kernel-module-g-ncm-6.1.38-fslc+g085682f3fc7e
g-ncm kernel module; NCM Gadget

%package -n kernel-module-g-serial-6.1.38-fslc+g085682f3fc7e
Summary: g-serial kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-g-serial

%description -n kernel-module-g-serial-6.1.38-fslc+g085682f3fc7e
g-serial kernel module; Gadget Serial v2.4

%package -n kernel-module-g-zero-6.1.38-fslc+g085682f3fc7e
Summary: g-zero kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-g-zero

%description -n kernel-module-g-zero-6.1.38-fslc+g085682f3fc7e
g-zero kernel module

%package -n kernel-module-gadgetfs-6.1.38-fslc+g085682f3fc7e
Summary: gadgetfs kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-gadgetfs

%description -n kernel-module-gadgetfs-6.1.38-fslc+g085682f3fc7e
gadgetfs kernel module; USB Gadget filesystem

%package -n kernel-module-ehset-6.1.38-fslc+g085682f3fc7e
Summary: ehset kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-ehset

%description -n kernel-module-ehset-6.1.38-fslc+g085682f3fc7e
ehset kernel module; USB Driver for EHSET Test Fixture

%package -n kernel-module-usbtest-6.1.38-fslc+g085682f3fc7e
Summary: usbtest kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-usbtest

%description -n kernel-module-usbtest-6.1.38-fslc+g085682f3fc7e
usbtest kernel module; USB Core/HCD Testing Driver

%package -n kernel-module-ftdi-sio-6.1.38-fslc+g085682f3fc7e
Summary: ftdi-sio kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-usbserial-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-usbserial-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-usbserial-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-ftdi-sio

%description -n kernel-module-ftdi-sio-6.1.38-fslc+g085682f3fc7e
ftdi-sio kernel module; USB FTDI Serial Converters Driver

%package -n kernel-module-option-6.1.38-fslc+g085682f3fc7e
Summary: option kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-usb-wwan-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-usbserial-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-usb-wwan-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-usbserial-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-usb-wwan-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-usbserial-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-option

%description -n kernel-module-option-6.1.38-fslc+g085682f3fc7e
option kernel module; USB Driver for GSM modems

%package -n kernel-module-usb-wwan-6.1.38-fslc+g085682f3fc7e
Summary: usb-wwan kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-usbserial-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-usbserial-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-usbserial-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-usb-wwan

%description -n kernel-module-usb-wwan-6.1.38-fslc+g085682f3fc7e
usb-wwan kernel module; USB Driver for GSM modems

%package -n kernel-module-usbserial-6.1.38-fslc+g085682f3fc7e
Summary: usbserial kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-usbserial

%description -n kernel-module-usbserial-6.1.38-fslc+g085682f3fc7e
usbserial kernel module; USB Serial Driver core

%package -n kernel-module-da9063-wdt-6.1.38-fslc+g085682f3fc7e
Summary: da9063-wdt kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-da9063-wdt

%description -n kernel-module-da9063-wdt-6.1.38-fslc+g085682f3fc7e
da9063-wdt kernel module; Watchdog driver for Dialog DA9063

%package -n kernel-module-binfmt-misc-6.1.38-fslc+g085682f3fc7e
Summary: binfmt-misc kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-binfmt-misc

%description -n kernel-module-binfmt-misc-6.1.38-fslc+g085682f3fc7e
binfmt-misc kernel module

%package -n kernel-module-msdos-6.1.38-fslc+g085682f3fc7e
Summary: msdos kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-msdos

%description -n kernel-module-msdos-6.1.38-fslc+g085682f3fc7e
msdos kernel module; MS-DOS filesystem support

%package -n kernel-module-isofs-6.1.38-fslc+g085682f3fc7e
Summary: isofs kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-isofs

%description -n kernel-module-isofs-6.1.38-fslc+g085682f3fc7e
isofs kernel module

%package -n kernel-module-nls-iso8859-15-6.1.38-fslc+g085682f3fc7e
Summary: nls-iso8859-15 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-nls-iso8859-15

%description -n kernel-module-nls-iso8859-15-6.1.38-fslc+g085682f3fc7e
nls-iso8859-15 kernel module

%package -n kernel-module-udf-6.1.38-fslc+g085682f3fc7e
Summary: udf kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-crc-itu-t-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-crc-itu-t-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-crc-itu-t-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-udf

%description -n kernel-module-udf-6.1.38-fslc+g085682f3fc7e
udf kernel module; Universal Disk Format Filesystem

%package -n kernel-module-crc-itu-t-6.1.38-fslc+g085682f3fc7e
Summary: crc-itu-t kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-crc-itu-t

%description -n kernel-module-crc-itu-t-6.1.38-fslc+g085682f3fc7e
crc-itu-t kernel module; CRC ITU-T V.41 calculations

%package -n kernel-module-crc7-6.1.38-fslc+g085682f3fc7e
Summary: crc7 kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-crc7

%description -n kernel-module-crc7-6.1.38-fslc+g085682f3fc7e
crc7 kernel module; CRC7 calculations

%package -n kernel-module-libcrc32c-6.1.38-fslc+g085682f3fc7e
Summary: libcrc32c kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-libcrc32c

%description -n kernel-module-libcrc32c-6.1.38-fslc+g085682f3fc7e
libcrc32c kernel module; CRC32c (Castagnoli) calculations

%package -n kernel-module-bnep-6.1.38-fslc+g085682f3fc7e
Summary: bnep kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-bnep

%description -n kernel-module-bnep-6.1.38-fslc+g085682f3fc7e
bnep kernel module; Bluetooth BNEP ver 1.3

%package -n kernel-module-snd-hwdep-6.1.38-fslc+g085682f3fc7e
Summary: snd-hwdep kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-snd-hwdep

%description -n kernel-module-snd-hwdep-6.1.38-fslc+g085682f3fc7e
snd-hwdep kernel module; Hardware dependent layer

%package -n kernel-module-snd-usb-audio-6.1.38-fslc+g085682f3fc7e
Summary: snd-usb-audio kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-snd-hwdep-6.1.38-fslc+g085682f3fc7e
Requires: kernel-module-snd-usbmidi-lib-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-snd-hwdep-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-module-snd-usbmidi-lib-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-snd-hwdep-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-module-snd-usbmidi-lib-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-snd-usb-audio

%description -n kernel-module-snd-usb-audio-6.1.38-fslc+g085682f3fc7e
snd-usb-audio kernel module; USB Audio

%package -n kernel-module-snd-usbmidi-lib-6.1.38-fslc+g085682f3fc7e
Summary: snd-usbmidi-lib kernel module
License: GPL-2.0-only
Group: base
Requires: kernel-6.1.38-fslc+g085682f3fc7e
Requires(post): kernel-6.1.38-fslc+g085682f3fc7e
Requires(postun): kernel-6.1.38-fslc+g085682f3fc7e
Provides: kernel-module-snd-usbmidi-lib

%description -n kernel-module-snd-usbmidi-lib-6.1.38-fslc+g085682f3fc7e
snd-usbmidi-lib kernel module; USB Audio/MIDI helper module

%post -n kernel-6.1.38-fslc+g085682f3fc7e
# kernel-6.1.38-fslc+g085682f3fc7e - postinst
set -e
	if [ ! -e "$D/lib/modules/6.1.38-fslc+g085682f3fc7e" ]; then
		mkdir -p $D/lib/modules/6.1.38-fslc+g085682f3fc7e
	fi
	if [ -n "$D" ]; then
		depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
	else
		depmod -a 6.1.38-fslc+g085682f3fc7e
	fi


%post -n kernel-image-zimage-6.1.38-fslc+g085682f3fc7e
# kernel-image-zimage-6.1.38-fslc+g085682f3fc7e - postinst
set -e
set +e
if [ -n "$D" ]; then
    ln -sf zImage-6.1.38-fslc+g085682f3fc7e $D/boot/zImage > /dev/null 2>&1
else
    ln -sf zImage-6.1.38-fslc+g085682f3fc7e boot/zImage > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        echo "Filesystem on boot/ doesn't support symlinks, falling back to copied image (zImage)."
        install -m 0644 boot/zImage-6.1.38-fslc+g085682f3fc7e boot/zImage
    fi
fi
set -e


%postun -n kernel-image-zimage-6.1.38-fslc+g085682f3fc7e
# kernel-image-zimage-6.1.38-fslc+g085682f3fc7e - postrm
if [ "$1" = "0" ] ; then
set -e
set +e
if [ -f "boot/zImage" -o -L "boot/zImage" ]; then
    rm -f boot/zImage  > /dev/null 2>&1
fi
set -e
fi

%post -n kernel-module-dmatest-6.1.38-fslc+g085682f3fc7e
# kernel-module-dmatest-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-dmatest-6.1.38-fslc+g085682f3fc7e
# kernel-module-dmatest-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-imx-sdma-6.1.38-fslc+g085682f3fc7e
# kernel-module-imx-sdma-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-imx-sdma-6.1.38-fslc+g085682f3fc7e
# kernel-module-imx-sdma-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-gpio-siox-6.1.38-fslc+g085682f3fc7e
# kernel-module-gpio-siox-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-gpio-siox-6.1.38-fslc+g085682f3fc7e
# kernel-module-gpio-siox-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-dw-hdmi-ahb-audio-6.1.38-fslc+g085682f3fc7e
# kernel-module-dw-hdmi-ahb-audio-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-dw-hdmi-ahb-audio-6.1.38-fslc+g085682f3fc7e
# kernel-module-dw-hdmi-ahb-audio-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-i2c-algo-pca-6.1.38-fslc+g085682f3fc7e
# kernel-module-i2c-algo-pca-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-i2c-algo-pca-6.1.38-fslc+g085682f3fc7e
# kernel-module-i2c-algo-pca-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-i2c-algo-pcf-6.1.38-fslc+g085682f3fc7e
# kernel-module-i2c-algo-pcf-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-i2c-algo-pcf-6.1.38-fslc+g085682f3fc7e
# kernel-module-i2c-algo-pcf-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-psmouse-6.1.38-fslc+g085682f3fc7e
# kernel-module-psmouse-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-psmouse-6.1.38-fslc+g085682f3fc7e
# kernel-module-psmouse-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-serport-6.1.38-fslc+g085682f3fc7e
# kernel-module-serport-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-serport-6.1.38-fslc+g085682f3fc7e
# kernel-module-serport-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-irq-imx-mu-msi-6.1.38-fslc+g085682f3fc7e
# kernel-module-irq-imx-mu-msi-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-irq-imx-mu-msi-6.1.38-fslc+g085682f3fc7e
# kernel-module-irq-imx-mu-msi-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-a8293-6.1.38-fslc+g085682f3fc7e
# kernel-module-a8293-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-a8293-6.1.38-fslc+g085682f3fc7e
# kernel-module-a8293-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-af9013-6.1.38-fslc+g085682f3fc7e
# kernel-module-af9013-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-af9013-6.1.38-fslc+g085682f3fc7e
# kernel-module-af9013-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-af9033-6.1.38-fslc+g085682f3fc7e
# kernel-module-af9033-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-af9033-6.1.38-fslc+g085682f3fc7e
# kernel-module-af9033-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-ascot2e-6.1.38-fslc+g085682f3fc7e
# kernel-module-ascot2e-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-ascot2e-6.1.38-fslc+g085682f3fc7e
# kernel-module-ascot2e-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-atbm8830-6.1.38-fslc+g085682f3fc7e
# kernel-module-atbm8830-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-atbm8830-6.1.38-fslc+g085682f3fc7e
# kernel-module-atbm8830-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-au8522-common-6.1.38-fslc+g085682f3fc7e
# kernel-module-au8522-common-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-au8522-common-6.1.38-fslc+g085682f3fc7e
# kernel-module-au8522-common-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-au8522-decoder-6.1.38-fslc+g085682f3fc7e
# kernel-module-au8522-decoder-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-au8522-decoder-6.1.38-fslc+g085682f3fc7e
# kernel-module-au8522-decoder-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-au8522-dig-6.1.38-fslc+g085682f3fc7e
# kernel-module-au8522-dig-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-au8522-dig-6.1.38-fslc+g085682f3fc7e
# kernel-module-au8522-dig-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-bcm3510-6.1.38-fslc+g085682f3fc7e
# kernel-module-bcm3510-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-bcm3510-6.1.38-fslc+g085682f3fc7e
# kernel-module-bcm3510-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-cx22700-6.1.38-fslc+g085682f3fc7e
# kernel-module-cx22700-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-cx22700-6.1.38-fslc+g085682f3fc7e
# kernel-module-cx22700-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-cx22702-6.1.38-fslc+g085682f3fc7e
# kernel-module-cx22702-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-cx22702-6.1.38-fslc+g085682f3fc7e
# kernel-module-cx22702-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-cx24110-6.1.38-fslc+g085682f3fc7e
# kernel-module-cx24110-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-cx24110-6.1.38-fslc+g085682f3fc7e
# kernel-module-cx24110-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-cx24113-6.1.38-fslc+g085682f3fc7e
# kernel-module-cx24113-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-cx24113-6.1.38-fslc+g085682f3fc7e
# kernel-module-cx24113-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-cx24116-6.1.38-fslc+g085682f3fc7e
# kernel-module-cx24116-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-cx24116-6.1.38-fslc+g085682f3fc7e
# kernel-module-cx24116-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-cx24117-6.1.38-fslc+g085682f3fc7e
# kernel-module-cx24117-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-cx24117-6.1.38-fslc+g085682f3fc7e
# kernel-module-cx24117-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-cx24120-6.1.38-fslc+g085682f3fc7e
# kernel-module-cx24120-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-cx24120-6.1.38-fslc+g085682f3fc7e
# kernel-module-cx24120-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-cx24123-6.1.38-fslc+g085682f3fc7e
# kernel-module-cx24123-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-cx24123-6.1.38-fslc+g085682f3fc7e
# kernel-module-cx24123-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-cxd2099-6.1.38-fslc+g085682f3fc7e
# kernel-module-cxd2099-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-cxd2099-6.1.38-fslc+g085682f3fc7e
# kernel-module-cxd2099-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-cxd2820r-6.1.38-fslc+g085682f3fc7e
# kernel-module-cxd2820r-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-cxd2820r-6.1.38-fslc+g085682f3fc7e
# kernel-module-cxd2820r-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-cxd2841er-6.1.38-fslc+g085682f3fc7e
# kernel-module-cxd2841er-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-cxd2841er-6.1.38-fslc+g085682f3fc7e
# kernel-module-cxd2841er-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-dib0070-6.1.38-fslc+g085682f3fc7e
# kernel-module-dib0070-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-dib0070-6.1.38-fslc+g085682f3fc7e
# kernel-module-dib0070-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-dib0090-6.1.38-fslc+g085682f3fc7e
# kernel-module-dib0090-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-dib0090-6.1.38-fslc+g085682f3fc7e
# kernel-module-dib0090-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-dib3000mb-6.1.38-fslc+g085682f3fc7e
# kernel-module-dib3000mb-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-dib3000mb-6.1.38-fslc+g085682f3fc7e
# kernel-module-dib3000mb-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-dib3000mc-6.1.38-fslc+g085682f3fc7e
# kernel-module-dib3000mc-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-dib3000mc-6.1.38-fslc+g085682f3fc7e
# kernel-module-dib3000mc-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-dib7000m-6.1.38-fslc+g085682f3fc7e
# kernel-module-dib7000m-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-dib7000m-6.1.38-fslc+g085682f3fc7e
# kernel-module-dib7000m-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-dib7000p-6.1.38-fslc+g085682f3fc7e
# kernel-module-dib7000p-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-dib7000p-6.1.38-fslc+g085682f3fc7e
# kernel-module-dib7000p-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-dib8000-6.1.38-fslc+g085682f3fc7e
# kernel-module-dib8000-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-dib8000-6.1.38-fslc+g085682f3fc7e
# kernel-module-dib8000-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-dib9000-6.1.38-fslc+g085682f3fc7e
# kernel-module-dib9000-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-dib9000-6.1.38-fslc+g085682f3fc7e
# kernel-module-dib9000-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e
# kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e
# kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-drxd-6.1.38-fslc+g085682f3fc7e
# kernel-module-drxd-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-drxd-6.1.38-fslc+g085682f3fc7e
# kernel-module-drxd-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-drxk-6.1.38-fslc+g085682f3fc7e
# kernel-module-drxk-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-drxk-6.1.38-fslc+g085682f3fc7e
# kernel-module-drxk-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-ds3000-6.1.38-fslc+g085682f3fc7e
# kernel-module-ds3000-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-ds3000-6.1.38-fslc+g085682f3fc7e
# kernel-module-ds3000-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-dvb-pll-6.1.38-fslc+g085682f3fc7e
# kernel-module-dvb-pll-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-dvb-pll-6.1.38-fslc+g085682f3fc7e
# kernel-module-dvb-pll-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-ec100-6.1.38-fslc+g085682f3fc7e
# kernel-module-ec100-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-ec100-6.1.38-fslc+g085682f3fc7e
# kernel-module-ec100-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-helene-6.1.38-fslc+g085682f3fc7e
# kernel-module-helene-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-helene-6.1.38-fslc+g085682f3fc7e
# kernel-module-helene-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-horus3a-6.1.38-fslc+g085682f3fc7e
# kernel-module-horus3a-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-horus3a-6.1.38-fslc+g085682f3fc7e
# kernel-module-horus3a-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-isl6405-6.1.38-fslc+g085682f3fc7e
# kernel-module-isl6405-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-isl6405-6.1.38-fslc+g085682f3fc7e
# kernel-module-isl6405-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-isl6421-6.1.38-fslc+g085682f3fc7e
# kernel-module-isl6421-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-isl6421-6.1.38-fslc+g085682f3fc7e
# kernel-module-isl6421-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-isl6423-6.1.38-fslc+g085682f3fc7e
# kernel-module-isl6423-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-isl6423-6.1.38-fslc+g085682f3fc7e
# kernel-module-isl6423-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-itd1000-6.1.38-fslc+g085682f3fc7e
# kernel-module-itd1000-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-itd1000-6.1.38-fslc+g085682f3fc7e
# kernel-module-itd1000-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-ix2505v-6.1.38-fslc+g085682f3fc7e
# kernel-module-ix2505v-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-ix2505v-6.1.38-fslc+g085682f3fc7e
# kernel-module-ix2505v-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-l64781-6.1.38-fslc+g085682f3fc7e
# kernel-module-l64781-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-l64781-6.1.38-fslc+g085682f3fc7e
# kernel-module-l64781-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-lg2160-6.1.38-fslc+g085682f3fc7e
# kernel-module-lg2160-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-lg2160-6.1.38-fslc+g085682f3fc7e
# kernel-module-lg2160-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-lgdt3305-6.1.38-fslc+g085682f3fc7e
# kernel-module-lgdt3305-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-lgdt3305-6.1.38-fslc+g085682f3fc7e
# kernel-module-lgdt3305-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-lgdt3306a-6.1.38-fslc+g085682f3fc7e
# kernel-module-lgdt3306a-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-lgdt3306a-6.1.38-fslc+g085682f3fc7e
# kernel-module-lgdt3306a-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-lgdt330x-6.1.38-fslc+g085682f3fc7e
# kernel-module-lgdt330x-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-lgdt330x-6.1.38-fslc+g085682f3fc7e
# kernel-module-lgdt330x-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-lgs8gl5-6.1.38-fslc+g085682f3fc7e
# kernel-module-lgs8gl5-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-lgs8gl5-6.1.38-fslc+g085682f3fc7e
# kernel-module-lgs8gl5-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-lgs8gxx-6.1.38-fslc+g085682f3fc7e
# kernel-module-lgs8gxx-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-lgs8gxx-6.1.38-fslc+g085682f3fc7e
# kernel-module-lgs8gxx-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-lnbh25-6.1.38-fslc+g085682f3fc7e
# kernel-module-lnbh25-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-lnbh25-6.1.38-fslc+g085682f3fc7e
# kernel-module-lnbh25-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-lnbh29-6.1.38-fslc+g085682f3fc7e
# kernel-module-lnbh29-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-lnbh29-6.1.38-fslc+g085682f3fc7e
# kernel-module-lnbh29-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-lnbp21-6.1.38-fslc+g085682f3fc7e
# kernel-module-lnbp21-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-lnbp21-6.1.38-fslc+g085682f3fc7e
# kernel-module-lnbp21-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-lnbp22-6.1.38-fslc+g085682f3fc7e
# kernel-module-lnbp22-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-lnbp22-6.1.38-fslc+g085682f3fc7e
# kernel-module-lnbp22-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-m88ds3103-6.1.38-fslc+g085682f3fc7e
# kernel-module-m88ds3103-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-m88ds3103-6.1.38-fslc+g085682f3fc7e
# kernel-module-m88ds3103-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-m88rs2000-6.1.38-fslc+g085682f3fc7e
# kernel-module-m88rs2000-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-m88rs2000-6.1.38-fslc+g085682f3fc7e
# kernel-module-m88rs2000-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-mb86a16-6.1.38-fslc+g085682f3fc7e
# kernel-module-mb86a16-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-mb86a16-6.1.38-fslc+g085682f3fc7e
# kernel-module-mb86a16-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-mb86a20s-6.1.38-fslc+g085682f3fc7e
# kernel-module-mb86a20s-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-mb86a20s-6.1.38-fslc+g085682f3fc7e
# kernel-module-mb86a20s-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-mn88443x-6.1.38-fslc+g085682f3fc7e
# kernel-module-mn88443x-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-mn88443x-6.1.38-fslc+g085682f3fc7e
# kernel-module-mn88443x-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-mn88472-6.1.38-fslc+g085682f3fc7e
# kernel-module-mn88472-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-mn88472-6.1.38-fslc+g085682f3fc7e
# kernel-module-mn88472-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-mn88473-6.1.38-fslc+g085682f3fc7e
# kernel-module-mn88473-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-mn88473-6.1.38-fslc+g085682f3fc7e
# kernel-module-mn88473-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-mt312-6.1.38-fslc+g085682f3fc7e
# kernel-module-mt312-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-mt312-6.1.38-fslc+g085682f3fc7e
# kernel-module-mt312-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-mt352-6.1.38-fslc+g085682f3fc7e
# kernel-module-mt352-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-mt352-6.1.38-fslc+g085682f3fc7e
# kernel-module-mt352-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-mxl5xx-6.1.38-fslc+g085682f3fc7e
# kernel-module-mxl5xx-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-mxl5xx-6.1.38-fslc+g085682f3fc7e
# kernel-module-mxl5xx-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-mxl692-6.1.38-fslc+g085682f3fc7e
# kernel-module-mxl692-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-mxl692-6.1.38-fslc+g085682f3fc7e
# kernel-module-mxl692-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-nxt200x-6.1.38-fslc+g085682f3fc7e
# kernel-module-nxt200x-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-nxt200x-6.1.38-fslc+g085682f3fc7e
# kernel-module-nxt200x-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-nxt6000-6.1.38-fslc+g085682f3fc7e
# kernel-module-nxt6000-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-nxt6000-6.1.38-fslc+g085682f3fc7e
# kernel-module-nxt6000-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-or51132-6.1.38-fslc+g085682f3fc7e
# kernel-module-or51132-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-or51132-6.1.38-fslc+g085682f3fc7e
# kernel-module-or51132-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-or51211-6.1.38-fslc+g085682f3fc7e
# kernel-module-or51211-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-or51211-6.1.38-fslc+g085682f3fc7e
# kernel-module-or51211-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-rtl2830-6.1.38-fslc+g085682f3fc7e
# kernel-module-rtl2830-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-rtl2830-6.1.38-fslc+g085682f3fc7e
# kernel-module-rtl2830-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-rtl2832-6.1.38-fslc+g085682f3fc7e
# kernel-module-rtl2832-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-rtl2832-6.1.38-fslc+g085682f3fc7e
# kernel-module-rtl2832-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-rtl2832-sdr-6.1.38-fslc+g085682f3fc7e
# kernel-module-rtl2832-sdr-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-rtl2832-sdr-6.1.38-fslc+g085682f3fc7e
# kernel-module-rtl2832-sdr-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-s5h1409-6.1.38-fslc+g085682f3fc7e
# kernel-module-s5h1409-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-s5h1409-6.1.38-fslc+g085682f3fc7e
# kernel-module-s5h1409-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-s5h1411-6.1.38-fslc+g085682f3fc7e
# kernel-module-s5h1411-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-s5h1411-6.1.38-fslc+g085682f3fc7e
# kernel-module-s5h1411-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-s5h1420-6.1.38-fslc+g085682f3fc7e
# kernel-module-s5h1420-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-s5h1420-6.1.38-fslc+g085682f3fc7e
# kernel-module-s5h1420-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-s5h1432-6.1.38-fslc+g085682f3fc7e
# kernel-module-s5h1432-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-s5h1432-6.1.38-fslc+g085682f3fc7e
# kernel-module-s5h1432-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-s921-6.1.38-fslc+g085682f3fc7e
# kernel-module-s921-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-s921-6.1.38-fslc+g085682f3fc7e
# kernel-module-s921-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-si2165-6.1.38-fslc+g085682f3fc7e
# kernel-module-si2165-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-si2165-6.1.38-fslc+g085682f3fc7e
# kernel-module-si2165-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-si2168-6.1.38-fslc+g085682f3fc7e
# kernel-module-si2168-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-si2168-6.1.38-fslc+g085682f3fc7e
# kernel-module-si2168-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-si21xx-6.1.38-fslc+g085682f3fc7e
# kernel-module-si21xx-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-si21xx-6.1.38-fslc+g085682f3fc7e
# kernel-module-si21xx-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-sp2-6.1.38-fslc+g085682f3fc7e
# kernel-module-sp2-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-sp2-6.1.38-fslc+g085682f3fc7e
# kernel-module-sp2-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-sp887x-6.1.38-fslc+g085682f3fc7e
# kernel-module-sp887x-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-sp887x-6.1.38-fslc+g085682f3fc7e
# kernel-module-sp887x-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-stb0899-6.1.38-fslc+g085682f3fc7e
# kernel-module-stb0899-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-stb0899-6.1.38-fslc+g085682f3fc7e
# kernel-module-stb0899-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-stb6000-6.1.38-fslc+g085682f3fc7e
# kernel-module-stb6000-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-stb6000-6.1.38-fslc+g085682f3fc7e
# kernel-module-stb6000-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-stb6100-6.1.38-fslc+g085682f3fc7e
# kernel-module-stb6100-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-stb6100-6.1.38-fslc+g085682f3fc7e
# kernel-module-stb6100-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-stv0288-6.1.38-fslc+g085682f3fc7e
# kernel-module-stv0288-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-stv0288-6.1.38-fslc+g085682f3fc7e
# kernel-module-stv0288-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-stv0297-6.1.38-fslc+g085682f3fc7e
# kernel-module-stv0297-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-stv0297-6.1.38-fslc+g085682f3fc7e
# kernel-module-stv0297-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-stv0299-6.1.38-fslc+g085682f3fc7e
# kernel-module-stv0299-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-stv0299-6.1.38-fslc+g085682f3fc7e
# kernel-module-stv0299-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-stv0367-6.1.38-fslc+g085682f3fc7e
# kernel-module-stv0367-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-stv0367-6.1.38-fslc+g085682f3fc7e
# kernel-module-stv0367-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-stv0900-6.1.38-fslc+g085682f3fc7e
# kernel-module-stv0900-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-stv0900-6.1.38-fslc+g085682f3fc7e
# kernel-module-stv0900-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-stv090x-6.1.38-fslc+g085682f3fc7e
# kernel-module-stv090x-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-stv090x-6.1.38-fslc+g085682f3fc7e
# kernel-module-stv090x-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-stv0910-6.1.38-fslc+g085682f3fc7e
# kernel-module-stv0910-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-stv0910-6.1.38-fslc+g085682f3fc7e
# kernel-module-stv0910-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-stv6110-6.1.38-fslc+g085682f3fc7e
# kernel-module-stv6110-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-stv6110-6.1.38-fslc+g085682f3fc7e
# kernel-module-stv6110-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-stv6110x-6.1.38-fslc+g085682f3fc7e
# kernel-module-stv6110x-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-stv6110x-6.1.38-fslc+g085682f3fc7e
# kernel-module-stv6110x-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-stv6111-6.1.38-fslc+g085682f3fc7e
# kernel-module-stv6111-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-stv6111-6.1.38-fslc+g085682f3fc7e
# kernel-module-stv6111-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tc90522-6.1.38-fslc+g085682f3fc7e
# kernel-module-tc90522-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tc90522-6.1.38-fslc+g085682f3fc7e
# kernel-module-tc90522-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tda10021-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda10021-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tda10021-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda10021-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tda10023-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda10023-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tda10023-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda10023-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tda10048-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda10048-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tda10048-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda10048-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tda1004x-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda1004x-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tda1004x-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda1004x-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tda10071-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda10071-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tda10071-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda10071-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tda10086-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda10086-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tda10086-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda10086-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tda18271c2dd-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda18271c2dd-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tda18271c2dd-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda18271c2dd-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tda665x-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda665x-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tda665x-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda665x-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tda8083-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda8083-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tda8083-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda8083-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tda8261-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda8261-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tda8261-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda8261-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tda826x-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda826x-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tda826x-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda826x-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-ts2020-6.1.38-fslc+g085682f3fc7e
# kernel-module-ts2020-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-ts2020-6.1.38-fslc+g085682f3fc7e
# kernel-module-ts2020-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tua6100-6.1.38-fslc+g085682f3fc7e
# kernel-module-tua6100-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tua6100-6.1.38-fslc+g085682f3fc7e
# kernel-module-tua6100-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-ves1820-6.1.38-fslc+g085682f3fc7e
# kernel-module-ves1820-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-ves1820-6.1.38-fslc+g085682f3fc7e
# kernel-module-ves1820-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-ves1x93-6.1.38-fslc+g085682f3fc7e
# kernel-module-ves1x93-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-ves1x93-6.1.38-fslc+g085682f3fc7e
# kernel-module-ves1x93-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-zd1301-demod-6.1.38-fslc+g085682f3fc7e
# kernel-module-zd1301-demod-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-zd1301-demod-6.1.38-fslc+g085682f3fc7e
# kernel-module-zd1301-demod-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-zl10036-6.1.38-fslc+g085682f3fc7e
# kernel-module-zl10036-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-zl10036-6.1.38-fslc+g085682f3fc7e
# kernel-module-zl10036-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-zl10039-6.1.38-fslc+g085682f3fc7e
# kernel-module-zl10039-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-zl10039-6.1.38-fslc+g085682f3fc7e
# kernel-module-zl10039-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-zl10353-6.1.38-fslc+g085682f3fc7e
# kernel-module-zl10353-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-zl10353-6.1.38-fslc+g085682f3fc7e
# kernel-module-zl10353-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-cxd2880-6.1.38-fslc+g085682f3fc7e
# kernel-module-cxd2880-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-cxd2880-6.1.38-fslc+g085682f3fc7e
# kernel-module-cxd2880-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-drx39xyj-6.1.38-fslc+g085682f3fc7e
# kernel-module-drx39xyj-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-drx39xyj-6.1.38-fslc+g085682f3fc7e
# kernel-module-drx39xyj-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-adv7180-6.1.38-fslc+g085682f3fc7e
# kernel-module-adv7180-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-adv7180-6.1.38-fslc+g085682f3fc7e
# kernel-module-adv7180-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-ov2680-6.1.38-fslc+g085682f3fc7e
# kernel-module-ov2680-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-ov2680-6.1.38-fslc+g085682f3fc7e
# kernel-module-ov2680-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-ov5640-6.1.38-fslc+g085682f3fc7e
# kernel-module-ov5640-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-ov5640-6.1.38-fslc+g085682f3fc7e
# kernel-module-ov5640-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-ov5645-6.1.38-fslc+g085682f3fc7e
# kernel-module-ov5645-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-ov5645-6.1.38-fslc+g085682f3fc7e
# kernel-module-ov5645-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-coda-vpu-6.1.38-fslc+g085682f3fc7e
# kernel-module-coda-vpu-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-coda-vpu-6.1.38-fslc+g085682f3fc7e
# kernel-module-coda-vpu-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-imx-vdoa-6.1.38-fslc+g085682f3fc7e
# kernel-module-imx-vdoa-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-imx-vdoa-6.1.38-fslc+g085682f3fc7e
# kernel-module-imx-vdoa-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-cxd2880-spi-6.1.38-fslc+g085682f3fc7e
# kernel-module-cxd2880-spi-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-cxd2880-spi-6.1.38-fslc+g085682f3fc7e
# kernel-module-cxd2880-spi-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-e4000-6.1.38-fslc+g085682f3fc7e
# kernel-module-e4000-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-e4000-6.1.38-fslc+g085682f3fc7e
# kernel-module-e4000-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-fc0011-6.1.38-fslc+g085682f3fc7e
# kernel-module-fc0011-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-fc0011-6.1.38-fslc+g085682f3fc7e
# kernel-module-fc0011-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-fc0012-6.1.38-fslc+g085682f3fc7e
# kernel-module-fc0012-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-fc0012-6.1.38-fslc+g085682f3fc7e
# kernel-module-fc0012-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-fc0013-6.1.38-fslc+g085682f3fc7e
# kernel-module-fc0013-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-fc0013-6.1.38-fslc+g085682f3fc7e
# kernel-module-fc0013-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-fc2580-6.1.38-fslc+g085682f3fc7e
# kernel-module-fc2580-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-fc2580-6.1.38-fslc+g085682f3fc7e
# kernel-module-fc2580-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-it913x-6.1.38-fslc+g085682f3fc7e
# kernel-module-it913x-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-it913x-6.1.38-fslc+g085682f3fc7e
# kernel-module-it913x-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-m88rs6000t-6.1.38-fslc+g085682f3fc7e
# kernel-module-m88rs6000t-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-m88rs6000t-6.1.38-fslc+g085682f3fc7e
# kernel-module-m88rs6000t-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-max2165-6.1.38-fslc+g085682f3fc7e
# kernel-module-max2165-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-max2165-6.1.38-fslc+g085682f3fc7e
# kernel-module-max2165-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-mc44s803-6.1.38-fslc+g085682f3fc7e
# kernel-module-mc44s803-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-mc44s803-6.1.38-fslc+g085682f3fc7e
# kernel-module-mc44s803-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-msi001-6.1.38-fslc+g085682f3fc7e
# kernel-module-msi001-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-msi001-6.1.38-fslc+g085682f3fc7e
# kernel-module-msi001-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-mt2060-6.1.38-fslc+g085682f3fc7e
# kernel-module-mt2060-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-mt2060-6.1.38-fslc+g085682f3fc7e
# kernel-module-mt2060-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-mt2063-6.1.38-fslc+g085682f3fc7e
# kernel-module-mt2063-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-mt2063-6.1.38-fslc+g085682f3fc7e
# kernel-module-mt2063-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-mt20xx-6.1.38-fslc+g085682f3fc7e
# kernel-module-mt20xx-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-mt20xx-6.1.38-fslc+g085682f3fc7e
# kernel-module-mt20xx-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-mt2131-6.1.38-fslc+g085682f3fc7e
# kernel-module-mt2131-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-mt2131-6.1.38-fslc+g085682f3fc7e
# kernel-module-mt2131-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-mt2266-6.1.38-fslc+g085682f3fc7e
# kernel-module-mt2266-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-mt2266-6.1.38-fslc+g085682f3fc7e
# kernel-module-mt2266-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-mxl301rf-6.1.38-fslc+g085682f3fc7e
# kernel-module-mxl301rf-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-mxl301rf-6.1.38-fslc+g085682f3fc7e
# kernel-module-mxl301rf-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-mxl5005s-6.1.38-fslc+g085682f3fc7e
# kernel-module-mxl5005s-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-mxl5005s-6.1.38-fslc+g085682f3fc7e
# kernel-module-mxl5005s-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-mxl5007t-6.1.38-fslc+g085682f3fc7e
# kernel-module-mxl5007t-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-mxl5007t-6.1.38-fslc+g085682f3fc7e
# kernel-module-mxl5007t-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-qm1d1b0004-6.1.38-fslc+g085682f3fc7e
# kernel-module-qm1d1b0004-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-qm1d1b0004-6.1.38-fslc+g085682f3fc7e
# kernel-module-qm1d1b0004-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-qm1d1c0042-6.1.38-fslc+g085682f3fc7e
# kernel-module-qm1d1c0042-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-qm1d1c0042-6.1.38-fslc+g085682f3fc7e
# kernel-module-qm1d1c0042-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-qt1010-6.1.38-fslc+g085682f3fc7e
# kernel-module-qt1010-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-qt1010-6.1.38-fslc+g085682f3fc7e
# kernel-module-qt1010-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-r820t-6.1.38-fslc+g085682f3fc7e
# kernel-module-r820t-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-r820t-6.1.38-fslc+g085682f3fc7e
# kernel-module-r820t-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-si2157-6.1.38-fslc+g085682f3fc7e
# kernel-module-si2157-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-si2157-6.1.38-fslc+g085682f3fc7e
# kernel-module-si2157-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tda18212-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda18212-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tda18212-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda18212-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tda18218-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda18218-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tda18218-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda18218-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tda18250-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda18250-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tda18250-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda18250-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tda18271-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda18271-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tda18271-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda18271-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tda827x-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda827x-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tda827x-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda827x-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tda8290-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda8290-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tda8290-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda8290-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tda9887-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda9887-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tda9887-6.1.38-fslc+g085682f3fc7e
# kernel-module-tda9887-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tea5761-6.1.38-fslc+g085682f3fc7e
# kernel-module-tea5761-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tea5761-6.1.38-fslc+g085682f3fc7e
# kernel-module-tea5761-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tea5767-6.1.38-fslc+g085682f3fc7e
# kernel-module-tea5767-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tea5767-6.1.38-fslc+g085682f3fc7e
# kernel-module-tea5767-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tua9001-6.1.38-fslc+g085682f3fc7e
# kernel-module-tua9001-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tua9001-6.1.38-fslc+g085682f3fc7e
# kernel-module-tua9001-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tuner-simple-6.1.38-fslc+g085682f3fc7e
# kernel-module-tuner-simple-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tuner-simple-6.1.38-fslc+g085682f3fc7e
# kernel-module-tuner-simple-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-tuner-types-6.1.38-fslc+g085682f3fc7e
# kernel-module-tuner-types-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-tuner-types-6.1.38-fslc+g085682f3fc7e
# kernel-module-tuner-types-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-xc2028-6.1.38-fslc+g085682f3fc7e
# kernel-module-xc2028-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-xc2028-6.1.38-fslc+g085682f3fc7e
# kernel-module-xc2028-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-xc4000-6.1.38-fslc+g085682f3fc7e
# kernel-module-xc4000-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-xc4000-6.1.38-fslc+g085682f3fc7e
# kernel-module-xc4000-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-xc5000-6.1.38-fslc+g085682f3fc7e
# kernel-module-xc5000-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-xc5000-6.1.38-fslc+g085682f3fc7e
# kernel-module-xc5000-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-uvcvideo-6.1.38-fslc+g085682f3fc7e
# kernel-module-uvcvideo-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-uvcvideo-6.1.38-fslc+g085682f3fc7e
# kernel-module-uvcvideo-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-v4l2-jpeg-6.1.38-fslc+g085682f3fc7e
# kernel-module-v4l2-jpeg-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-v4l2-jpeg-6.1.38-fslc+g085682f3fc7e
# kernel-module-v4l2-jpeg-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-cdc-eem-6.1.38-fslc+g085682f3fc7e
# kernel-module-cdc-eem-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-cdc-eem-6.1.38-fslc+g085682f3fc7e
# kernel-module-cdc-eem-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-pegasus-6.1.38-fslc+g085682f3fc7e
# kernel-module-pegasus-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-pegasus-6.1.38-fslc+g085682f3fc7e
# kernel-module-pegasus-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-rtl8150-6.1.38-fslc+g085682f3fc7e
# kernel-module-rtl8150-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-rtl8150-6.1.38-fslc+g085682f3fc7e
# kernel-module-rtl8150-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-ath-6.1.38-fslc+g085682f3fc7e
# kernel-module-ath-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-ath-6.1.38-fslc+g085682f3fc7e
# kernel-module-ath-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-ath10k-core-6.1.38-fslc+g085682f3fc7e
# kernel-module-ath10k-core-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-ath10k-core-6.1.38-fslc+g085682f3fc7e
# kernel-module-ath10k-core-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-ath10k-sdio-6.1.38-fslc+g085682f3fc7e
# kernel-module-ath10k-sdio-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-ath10k-sdio-6.1.38-fslc+g085682f3fc7e
# kernel-module-ath10k-sdio-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-brcmfmac-6.1.38-fslc+g085682f3fc7e
# kernel-module-brcmfmac-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-brcmfmac-6.1.38-fslc+g085682f3fc7e
# kernel-module-brcmfmac-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-brcmutil-6.1.38-fslc+g085682f3fc7e
# kernel-module-brcmutil-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-brcmutil-6.1.38-fslc+g085682f3fc7e
# kernel-module-brcmutil-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-mwifiex-6.1.38-fslc+g085682f3fc7e
# kernel-module-mwifiex-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-mwifiex-6.1.38-fslc+g085682f3fc7e
# kernel-module-mwifiex-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-mwifiex-pcie-6.1.38-fslc+g085682f3fc7e
# kernel-module-mwifiex-pcie-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-mwifiex-pcie-6.1.38-fslc+g085682f3fc7e
# kernel-module-mwifiex-pcie-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-mwifiex-sdio-6.1.38-fslc+g085682f3fc7e
# kernel-module-mwifiex-sdio-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-mwifiex-sdio-6.1.38-fslc+g085682f3fc7e
# kernel-module-mwifiex-sdio-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-wl12xx-6.1.38-fslc+g085682f3fc7e
# kernel-module-wl12xx-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-wl12xx-6.1.38-fslc+g085682f3fc7e
# kernel-module-wl12xx-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-wl18xx-6.1.38-fslc+g085682f3fc7e
# kernel-module-wl18xx-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-wl18xx-6.1.38-fslc+g085682f3fc7e
# kernel-module-wl18xx-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-wlcore-6.1.38-fslc+g085682f3fc7e
# kernel-module-wlcore-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-wlcore-6.1.38-fslc+g085682f3fc7e
# kernel-module-wlcore-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-wlcore-sdio-6.1.38-fslc+g085682f3fc7e
# kernel-module-wlcore-sdio-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-wlcore-sdio-6.1.38-fslc+g085682f3fc7e
# kernel-module-wlcore-sdio-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-rn5t618-power-6.1.38-fslc+g085682f3fc7e
# kernel-module-rn5t618-power-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-rn5t618-power-6.1.38-fslc+g085682f3fc7e
# kernel-module-rn5t618-power-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-siox-bus-gpio-6.1.38-fslc+g085682f3fc7e
# kernel-module-siox-bus-gpio-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-siox-bus-gpio-6.1.38-fslc+g085682f3fc7e
# kernel-module-siox-bus-gpio-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-siox-core-6.1.38-fslc+g085682f3fc7e
# kernel-module-siox-core-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-siox-core-6.1.38-fslc+g085682f3fc7e
# kernel-module-siox-core-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-cdc-acm-6.1.38-fslc+g085682f3fc7e
# kernel-module-cdc-acm-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-cdc-acm-6.1.38-fslc+g085682f3fc7e
# kernel-module-cdc-acm-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-g-audio-6.1.38-fslc+g085682f3fc7e
# kernel-module-g-audio-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-g-audio-6.1.38-fslc+g085682f3fc7e
# kernel-module-g-audio-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-g-ether-6.1.38-fslc+g085682f3fc7e
# kernel-module-g-ether-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-g-ether-6.1.38-fslc+g085682f3fc7e
# kernel-module-g-ether-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-g-ffs-6.1.38-fslc+g085682f3fc7e
# kernel-module-g-ffs-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-g-ffs-6.1.38-fslc+g085682f3fc7e
# kernel-module-g-ffs-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-g-mass-storage-6.1.38-fslc+g085682f3fc7e
# kernel-module-g-mass-storage-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-g-mass-storage-6.1.38-fslc+g085682f3fc7e
# kernel-module-g-mass-storage-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-g-ncm-6.1.38-fslc+g085682f3fc7e
# kernel-module-g-ncm-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-g-ncm-6.1.38-fslc+g085682f3fc7e
# kernel-module-g-ncm-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-g-serial-6.1.38-fslc+g085682f3fc7e
# kernel-module-g-serial-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-g-serial-6.1.38-fslc+g085682f3fc7e
# kernel-module-g-serial-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-g-zero-6.1.38-fslc+g085682f3fc7e
# kernel-module-g-zero-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-g-zero-6.1.38-fslc+g085682f3fc7e
# kernel-module-g-zero-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-gadgetfs-6.1.38-fslc+g085682f3fc7e
# kernel-module-gadgetfs-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-gadgetfs-6.1.38-fslc+g085682f3fc7e
# kernel-module-gadgetfs-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-ehset-6.1.38-fslc+g085682f3fc7e
# kernel-module-ehset-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-ehset-6.1.38-fslc+g085682f3fc7e
# kernel-module-ehset-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-usbtest-6.1.38-fslc+g085682f3fc7e
# kernel-module-usbtest-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-usbtest-6.1.38-fslc+g085682f3fc7e
# kernel-module-usbtest-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-ftdi-sio-6.1.38-fslc+g085682f3fc7e
# kernel-module-ftdi-sio-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-ftdi-sio-6.1.38-fslc+g085682f3fc7e
# kernel-module-ftdi-sio-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-option-6.1.38-fslc+g085682f3fc7e
# kernel-module-option-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-option-6.1.38-fslc+g085682f3fc7e
# kernel-module-option-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-usb-wwan-6.1.38-fslc+g085682f3fc7e
# kernel-module-usb-wwan-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-usb-wwan-6.1.38-fslc+g085682f3fc7e
# kernel-module-usb-wwan-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-usbserial-6.1.38-fslc+g085682f3fc7e
# kernel-module-usbserial-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-usbserial-6.1.38-fslc+g085682f3fc7e
# kernel-module-usbserial-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-da9063-wdt-6.1.38-fslc+g085682f3fc7e
# kernel-module-da9063-wdt-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-da9063-wdt-6.1.38-fslc+g085682f3fc7e
# kernel-module-da9063-wdt-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-binfmt-misc-6.1.38-fslc+g085682f3fc7e
# kernel-module-binfmt-misc-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-binfmt-misc-6.1.38-fslc+g085682f3fc7e
# kernel-module-binfmt-misc-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-msdos-6.1.38-fslc+g085682f3fc7e
# kernel-module-msdos-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-msdos-6.1.38-fslc+g085682f3fc7e
# kernel-module-msdos-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-isofs-6.1.38-fslc+g085682f3fc7e
# kernel-module-isofs-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-isofs-6.1.38-fslc+g085682f3fc7e
# kernel-module-isofs-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-nls-iso8859-15-6.1.38-fslc+g085682f3fc7e
# kernel-module-nls-iso8859-15-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-nls-iso8859-15-6.1.38-fslc+g085682f3fc7e
# kernel-module-nls-iso8859-15-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-udf-6.1.38-fslc+g085682f3fc7e
# kernel-module-udf-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-udf-6.1.38-fslc+g085682f3fc7e
# kernel-module-udf-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-crc-itu-t-6.1.38-fslc+g085682f3fc7e
# kernel-module-crc-itu-t-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-crc-itu-t-6.1.38-fslc+g085682f3fc7e
# kernel-module-crc-itu-t-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-crc7-6.1.38-fslc+g085682f3fc7e
# kernel-module-crc7-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-crc7-6.1.38-fslc+g085682f3fc7e
# kernel-module-crc7-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-libcrc32c-6.1.38-fslc+g085682f3fc7e
# kernel-module-libcrc32c-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-libcrc32c-6.1.38-fslc+g085682f3fc7e
# kernel-module-libcrc32c-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-bnep-6.1.38-fslc+g085682f3fc7e
# kernel-module-bnep-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-bnep-6.1.38-fslc+g085682f3fc7e
# kernel-module-bnep-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-snd-hwdep-6.1.38-fslc+g085682f3fc7e
# kernel-module-snd-hwdep-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-snd-hwdep-6.1.38-fslc+g085682f3fc7e
# kernel-module-snd-hwdep-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-snd-usb-audio-6.1.38-fslc+g085682f3fc7e
# kernel-module-snd-usb-audio-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-snd-usb-audio-6.1.38-fslc+g085682f3fc7e
# kernel-module-snd-usb-audio-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%post -n kernel-module-snd-usbmidi-lib-6.1.38-fslc+g085682f3fc7e
# kernel-module-snd-usbmidi-lib-6.1.38-fslc+g085682f3fc7e - postinst
#!/bin/sh
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	# image.bbclass will call depmodwrapper after everything is installed,
	# no need to do it here as well
	:
fi



%postun -n kernel-module-snd-usbmidi-lib-6.1.38-fslc+g085682f3fc7e
# kernel-module-snd-usbmidi-lib-6.1.38-fslc+g085682f3fc7e - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
set -e
if [ -z "$D" ]; then
	depmod -a 6.1.38-fslc+g085682f3fc7e
else
	depmodwrapper -a -b $D 6.1.38-fslc+g085682f3fc7e
fi
fi

%files -n kernel-dbg
%defattr(-,-,-,-)
%dir "/boot"
%dir "/lib"
%dir "/boot/.debug"
"/boot/.debug/vmlinux-6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/sound"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/net"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/lib"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/sound/usb"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/sound/core"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/sound/usb/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/sound/usb/.debug/snd-usbmidi-lib.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/sound/usb/.debug/snd-usb-audio.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/sound/core/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/sound/core/.debug/snd-hwdep.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/net/bluetooth"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/net/bluetooth/bnep"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/net/bluetooth/bnep/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/net/bluetooth/bnep/.debug/bnep.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs/nls"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs/isofs"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs/fat"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs/udf"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs/.debug"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs/nls/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs/nls/.debug/nls_iso8859-15.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs/isofs/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs/isofs/.debug/isofs.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs/fat/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs/fat/.debug/msdos.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs/udf/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs/udf/.debug/udf.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs/.debug/binfmt_misc.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/power"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/siox"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/watchdog"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/gpio"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/gpu"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/irqchip"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/input"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/dma"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/i2c"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/power/supply"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/power/supply/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/power/supply/.debug/rn5t618_power.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/misc"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/class"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/serial"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/misc/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/misc/.debug/ehset.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/misc/.debug/usbtest.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/class/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/class/.debug/cdc-acm.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy/.debug/g_ncm.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy/.debug/g_mass_storage.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy/.debug/g_ether.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy/.debug/gadgetfs.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy/.debug/g_serial.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy/.debug/g_ffs.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy/.debug/g_zero.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy/.debug/g_audio.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/serial/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/serial/.debug/usb_wwan.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/serial/.debug/ftdi_sio.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/serial/.debug/usbserial.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/serial/.debug/option.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/siox/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/siox/.debug/siox-bus-gpio.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/siox/.debug/siox-core.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/watchdog/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/watchdog/.debug/da9063_wdt.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/v4l2-core"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/usb"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/spi"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/platform"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/i2c"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/v4l2-core/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/v4l2-core/.debug/v4l2-jpeg.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/usb/uvc"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/usb/uvc/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/usb/uvc/.debug/uvcvideo.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/mt2063.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/mt2131.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/tda9887.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/tea5767.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/max2165.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/tda8290.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/r820t.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/mxl301rf.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/mt2060.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/tda18271.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/tda18212.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/fc0013.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/tda18218.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/mt2266.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/si2157.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/qm1d1c0042.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/fc0012.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/tua9001.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/xc2028.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/e4000.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/tda18250.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/fc0011.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/qt1010.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/fc2580.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/tda827x.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/mxl5007t.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/xc4000.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/xc5000.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/msi001.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/qm1d1b0004.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/mxl5005s.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/it913x.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/tuner-types.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/m88rs6000t.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/tuner-simple.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/mt20xx.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/mc44s803.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/.debug/tea5761.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/spi/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/spi/.debug/cxd2880-spi.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/drx39xyj"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/cxd2880"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/drx39xyj/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/drx39xyj/.debug/drx39xyj.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/cxd2880/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/cxd2880/.debug/cxd2880.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/itd1000.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/lg2160.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/mn88472.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/cx24113.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/au8522_common.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/dib8000.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/zl10353.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/tda10021.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/s5h1420.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/lnbp22.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/cx24116.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/nxt200x.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/au8522_decoder.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/atbm8830.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/dib0070.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/af9033.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/cx22702.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/stv0367.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/bcm3510.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/a8293.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/tda10023.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/lnbh29.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/s5h1432.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/cx24110.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/stb6100.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/mb86a20s.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/tda10071.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/s5h1411.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/zd1301_demod.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/mn88473.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/horus3a.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/isl6421.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/dib7000m.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/ds3000.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/cx24123.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/ves1820.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/cx24117.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/lgdt330x.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/lgdt3306a.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/isl6405.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/mt352.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/stv6110x.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/l64781.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/or51132.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/helene.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/cxd2841er.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/tda8083.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/stv0288.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/tc90522.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/ec100.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/lgdt3305.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/cx22700.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/drxd.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/sp887x.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/si21xx.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/stv0910.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/stv0900.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/mn88443x.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/s921.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/au8522_dig.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/tda10086.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/rtl2832_sdr.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/si2168.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/tda8261.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/s5h1409.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/sp2.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/cxd2820r.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/dib7000p.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/si2165.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/tda18271c2dd.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/stb6000.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/stv0299.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/mt312.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/stv090x.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/stv0297.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/m88rs2000.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/ves1x93.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/zl10039.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/nxt6000.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/tua6100.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/tda665x.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/rtl2830.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/ts2020.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/mxl692.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/cxd2099.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/tda826x.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/rtl2832.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/drxk.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/dibx000_common.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/tda10048.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/dib3000mb.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/stb0899.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/ix2505v.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/dib3000mc.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/zl10036.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/mxl5xx.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/stv6110.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/mb86a16.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/dib9000.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/m88ds3103.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/lnbp21.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/stv6111.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/dib0090.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/lnbh25.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/cx24120.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/ascot2e.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/dvb-pll.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/tda1004x.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/af9013.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/lgs8gl5.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/lgs8gxx.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/or51211.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/.debug/isl6423.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/platform/chips-media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/platform/chips-media/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/platform/chips-media/.debug/imx-vdoa.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/platform/chips-media/.debug/coda-vpu.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/i2c/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/i2c/.debug/adv7180.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/i2c/.debug/ov2680.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/i2c/.debug/ov5645.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/i2c/.debug/ov5640.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/gpio/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/gpio/.debug/gpio-siox.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/gpu/drm"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/gpu/drm/bridge"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/gpu/drm/bridge/synopsys"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/gpu/drm/bridge/synopsys/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/gpu/drm/bridge/synopsys/.debug/dw-hdmi-ahb-audio.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/irqchip/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/irqchip/.debug/irq-imx-mu-msi.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/usb"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/usb/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/usb/.debug/rtl8150.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/usb/.debug/cdc_eem.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/usb/.debug/pegasus.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/broadcom"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ath"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ti"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/marvell"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/broadcom/brcm80211"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/broadcom/brcm80211/brcmfmac"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/broadcom/brcm80211/brcmutil"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/broadcom/brcm80211/brcmfmac/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/broadcom/brcm80211/brcmfmac/.debug/brcmfmac.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/broadcom/brcm80211/brcmutil/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/broadcom/brcm80211/brcmutil/.debug/brcmutil.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ath/ath10k"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ath/.debug"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ath/ath10k/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ath/ath10k/.debug/ath10k_sdio.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ath/ath10k/.debug/ath10k_core.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ath/.debug/ath.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ti/wl18xx"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ti/wl12xx"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ti/wlcore"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ti/wl18xx/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ti/wl18xx/.debug/wl18xx.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ti/wl12xx/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ti/wl12xx/.debug/wl12xx.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ti/wlcore/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ti/wlcore/.debug/wlcore.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ti/wlcore/.debug/wlcore_sdio.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/marvell/mwifiex"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/marvell/mwifiex/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/marvell/mwifiex/.debug/mwifiex.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/marvell/mwifiex/.debug/mwifiex_pcie.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/marvell/mwifiex/.debug/mwifiex_sdio.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/input/serio"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/input/mouse"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/input/serio/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/input/serio/.debug/serport.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/input/mouse/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/input/mouse/.debug/psmouse.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/dma/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/dma/.debug/imx-sdma.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/dma/.debug/dmatest.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/i2c/algos"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/i2c/algos/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/i2c/algos/.debug/i2c-algo-pca.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/i2c/algos/.debug/i2c-algo-pcf.ko"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/lib/.debug"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/lib/.debug/libcrc32c.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/lib/.debug/crc-itu-t.ko"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/lib/.debug/crc7.ko"

%files -n kernel
%defattr(-,-,-,-)

%files -n kernel-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/modules.builtin.modinfo"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/modules.order"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/modules.builtin"

%files -n kernel-vmlinux
%defattr(-,-,-,-)
%dir "/boot"
"/boot/vmlinux-6.1.38-fslc+g085682f3fc7e"

%files -n kernel-image-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)

%files -n kernel-dev
%defattr(-,-,-,-)
%dir "/boot"
"/boot/System.map-6.1.38-fslc+g085682f3fc7e"
"/boot/Module.symvers-6.1.38-fslc+g085682f3fc7e"
"/boot/config-6.1.38-fslc+g085682f3fc7e"

%files -n kernel-modules
%defattr(-,-,-,-)

%files -n kernel-image-zimage-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/boot"
"/boot/zImage-6.1.38-fslc+g085682f3fc7e"

%files -n kernel-devicetree
%defattr(-,-,-,-)
%dir "/boot"
"/boot/imx6dl-sabresd.dtb"
"/boot/imx6qp-sabresd.dtb"
"/boot/imx6q-sabresd.dtb"

%files -n kernel-module-dmatest-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/dma"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/dma/dmatest.ko"

%files -n kernel-module-imx-sdma-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/dma"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/dma/imx-sdma.ko"

%files -n kernel-module-gpio-siox-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/gpio"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/gpio/gpio-siox.ko"

%files -n kernel-module-dw-hdmi-ahb-audio-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/gpu"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/gpu/drm"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/gpu/drm/bridge"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/gpu/drm/bridge/synopsys"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/gpu/drm/bridge/synopsys/dw-hdmi-ahb-audio.ko"

%files -n kernel-module-i2c-algo-pca-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/i2c"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/i2c/algos"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/i2c/algos/i2c-algo-pca.ko"

%files -n kernel-module-i2c-algo-pcf-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/i2c"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/i2c/algos"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/i2c/algos/i2c-algo-pcf.ko"

%files -n kernel-module-psmouse-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/input"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/input/mouse"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/input/mouse/psmouse.ko"

%files -n kernel-module-serport-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/input"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/input/serio"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/input/serio/serport.ko"

%files -n kernel-module-irq-imx-mu-msi-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/irqchip"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/irqchip/irq-imx-mu-msi.ko"

%files -n kernel-module-a8293-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/a8293.ko"

%files -n kernel-module-af9013-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/af9013.ko"

%files -n kernel-module-af9033-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/af9033.ko"

%files -n kernel-module-ascot2e-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/ascot2e.ko"

%files -n kernel-module-atbm8830-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/atbm8830.ko"

%files -n kernel-module-au8522-common-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/au8522_common.ko"

%files -n kernel-module-au8522-decoder-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/au8522_decoder.ko"

%files -n kernel-module-au8522-dig-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/au8522_dig.ko"

%files -n kernel-module-bcm3510-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/bcm3510.ko"

%files -n kernel-module-cx22700-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/cx22700.ko"

%files -n kernel-module-cx22702-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/cx22702.ko"

%files -n kernel-module-cx24110-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/cx24110.ko"

%files -n kernel-module-cx24113-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/cx24113.ko"

%files -n kernel-module-cx24116-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/cx24116.ko"

%files -n kernel-module-cx24117-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/cx24117.ko"

%files -n kernel-module-cx24120-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/cx24120.ko"

%files -n kernel-module-cx24123-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/cx24123.ko"

%files -n kernel-module-cxd2099-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/cxd2099.ko"

%files -n kernel-module-cxd2820r-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/cxd2820r.ko"

%files -n kernel-module-cxd2841er-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/cxd2841er.ko"

%files -n kernel-module-dib0070-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/dib0070.ko"

%files -n kernel-module-dib0090-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/dib0090.ko"

%files -n kernel-module-dib3000mb-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/dib3000mb.ko"

%files -n kernel-module-dib3000mc-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/dib3000mc.ko"

%files -n kernel-module-dib7000m-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/dib7000m.ko"

%files -n kernel-module-dib7000p-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/dib7000p.ko"

%files -n kernel-module-dib8000-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/dib8000.ko"

%files -n kernel-module-dib9000-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/dib9000.ko"

%files -n kernel-module-dibx000-common-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/dibx000_common.ko"

%files -n kernel-module-drxd-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/drxd.ko"

%files -n kernel-module-drxk-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/drxk.ko"

%files -n kernel-module-ds3000-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/ds3000.ko"

%files -n kernel-module-dvb-pll-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/dvb-pll.ko"

%files -n kernel-module-ec100-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/ec100.ko"

%files -n kernel-module-helene-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/helene.ko"

%files -n kernel-module-horus3a-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/horus3a.ko"

%files -n kernel-module-isl6405-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/isl6405.ko"

%files -n kernel-module-isl6421-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/isl6421.ko"

%files -n kernel-module-isl6423-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/isl6423.ko"

%files -n kernel-module-itd1000-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/itd1000.ko"

%files -n kernel-module-ix2505v-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/ix2505v.ko"

%files -n kernel-module-l64781-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/l64781.ko"

%files -n kernel-module-lg2160-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/lg2160.ko"

%files -n kernel-module-lgdt3305-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/lgdt3305.ko"

%files -n kernel-module-lgdt3306a-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/lgdt3306a.ko"

%files -n kernel-module-lgdt330x-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/lgdt330x.ko"

%files -n kernel-module-lgs8gl5-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/lgs8gl5.ko"

%files -n kernel-module-lgs8gxx-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/lgs8gxx.ko"

%files -n kernel-module-lnbh25-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/lnbh25.ko"

%files -n kernel-module-lnbh29-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/lnbh29.ko"

%files -n kernel-module-lnbp21-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/lnbp21.ko"

%files -n kernel-module-lnbp22-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/lnbp22.ko"

%files -n kernel-module-m88ds3103-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/m88ds3103.ko"

%files -n kernel-module-m88rs2000-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/m88rs2000.ko"

%files -n kernel-module-mb86a16-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/mb86a16.ko"

%files -n kernel-module-mb86a20s-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/mb86a20s.ko"

%files -n kernel-module-mn88443x-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/mn88443x.ko"

%files -n kernel-module-mn88472-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/mn88472.ko"

%files -n kernel-module-mn88473-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/mn88473.ko"

%files -n kernel-module-mt312-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/mt312.ko"

%files -n kernel-module-mt352-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/mt352.ko"

%files -n kernel-module-mxl5xx-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/mxl5xx.ko"

%files -n kernel-module-mxl692-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/mxl692.ko"

%files -n kernel-module-nxt200x-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/nxt200x.ko"

%files -n kernel-module-nxt6000-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/nxt6000.ko"

%files -n kernel-module-or51132-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/or51132.ko"

%files -n kernel-module-or51211-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/or51211.ko"

%files -n kernel-module-rtl2830-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/rtl2830.ko"

%files -n kernel-module-rtl2832-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/rtl2832.ko"

%files -n kernel-module-rtl2832-sdr-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/rtl2832_sdr.ko"

%files -n kernel-module-s5h1409-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/s5h1409.ko"

%files -n kernel-module-s5h1411-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/s5h1411.ko"

%files -n kernel-module-s5h1420-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/s5h1420.ko"

%files -n kernel-module-s5h1432-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/s5h1432.ko"

%files -n kernel-module-s921-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/s921.ko"

%files -n kernel-module-si2165-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/si2165.ko"

%files -n kernel-module-si2168-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/si2168.ko"

%files -n kernel-module-si21xx-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/si21xx.ko"

%files -n kernel-module-sp2-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/sp2.ko"

%files -n kernel-module-sp887x-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/sp887x.ko"

%files -n kernel-module-stb0899-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/stb0899.ko"

%files -n kernel-module-stb6000-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/stb6000.ko"

%files -n kernel-module-stb6100-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/stb6100.ko"

%files -n kernel-module-stv0288-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/stv0288.ko"

%files -n kernel-module-stv0297-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/stv0297.ko"

%files -n kernel-module-stv0299-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/stv0299.ko"

%files -n kernel-module-stv0367-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/stv0367.ko"

%files -n kernel-module-stv0900-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/stv0900.ko"

%files -n kernel-module-stv090x-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/stv090x.ko"

%files -n kernel-module-stv0910-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/stv0910.ko"

%files -n kernel-module-stv6110-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/stv6110.ko"

%files -n kernel-module-stv6110x-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/stv6110x.ko"

%files -n kernel-module-stv6111-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/stv6111.ko"

%files -n kernel-module-tc90522-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/tc90522.ko"

%files -n kernel-module-tda10021-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/tda10021.ko"

%files -n kernel-module-tda10023-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/tda10023.ko"

%files -n kernel-module-tda10048-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/tda10048.ko"

%files -n kernel-module-tda1004x-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/tda1004x.ko"

%files -n kernel-module-tda10071-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/tda10071.ko"

%files -n kernel-module-tda10086-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/tda10086.ko"

%files -n kernel-module-tda18271c2dd-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/tda18271c2dd.ko"

%files -n kernel-module-tda665x-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/tda665x.ko"

%files -n kernel-module-tda8083-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/tda8083.ko"

%files -n kernel-module-tda8261-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/tda8261.ko"

%files -n kernel-module-tda826x-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/tda826x.ko"

%files -n kernel-module-ts2020-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/ts2020.ko"

%files -n kernel-module-tua6100-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/tua6100.ko"

%files -n kernel-module-ves1820-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/ves1820.ko"

%files -n kernel-module-ves1x93-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/ves1x93.ko"

%files -n kernel-module-zd1301-demod-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/zd1301_demod.ko"

%files -n kernel-module-zl10036-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/zl10036.ko"

%files -n kernel-module-zl10039-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/zl10039.ko"

%files -n kernel-module-zl10353-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/zl10353.ko"

%files -n kernel-module-cxd2880-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/cxd2880"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/cxd2880/cxd2880.ko"

%files -n kernel-module-drx39xyj-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/drx39xyj"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/dvb-frontends/drx39xyj/drx39xyj.ko"

%files -n kernel-module-adv7180-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/i2c"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/i2c/adv7180.ko"

%files -n kernel-module-ov2680-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/i2c"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/i2c/ov2680.ko"

%files -n kernel-module-ov5640-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/i2c"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/i2c/ov5640.ko"

%files -n kernel-module-ov5645-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/i2c"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/i2c/ov5645.ko"

%files -n kernel-module-coda-vpu-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/platform"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/platform/chips-media"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/platform/chips-media/coda-vpu.ko"

%files -n kernel-module-imx-vdoa-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/platform"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/platform/chips-media"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/platform/chips-media/imx-vdoa.ko"

%files -n kernel-module-cxd2880-spi-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/spi"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/spi/cxd2880-spi.ko"

%files -n kernel-module-e4000-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/e4000.ko"

%files -n kernel-module-fc0011-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/fc0011.ko"

%files -n kernel-module-fc0012-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/fc0012.ko"

%files -n kernel-module-fc0013-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/fc0013.ko"

%files -n kernel-module-fc2580-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/fc2580.ko"

%files -n kernel-module-it913x-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/it913x.ko"

%files -n kernel-module-m88rs6000t-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/m88rs6000t.ko"

%files -n kernel-module-max2165-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/max2165.ko"

%files -n kernel-module-mc44s803-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/mc44s803.ko"

%files -n kernel-module-msi001-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/msi001.ko"

%files -n kernel-module-mt2060-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/mt2060.ko"

%files -n kernel-module-mt2063-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/mt2063.ko"

%files -n kernel-module-mt20xx-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/mt20xx.ko"

%files -n kernel-module-mt2131-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/mt2131.ko"

%files -n kernel-module-mt2266-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/mt2266.ko"

%files -n kernel-module-mxl301rf-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/mxl301rf.ko"

%files -n kernel-module-mxl5005s-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/mxl5005s.ko"

%files -n kernel-module-mxl5007t-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/mxl5007t.ko"

%files -n kernel-module-qm1d1b0004-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/qm1d1b0004.ko"

%files -n kernel-module-qm1d1c0042-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/qm1d1c0042.ko"

%files -n kernel-module-qt1010-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/qt1010.ko"

%files -n kernel-module-r820t-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/r820t.ko"

%files -n kernel-module-si2157-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/si2157.ko"

%files -n kernel-module-tda18212-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/tda18212.ko"

%files -n kernel-module-tda18218-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/tda18218.ko"

%files -n kernel-module-tda18250-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/tda18250.ko"

%files -n kernel-module-tda18271-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/tda18271.ko"

%files -n kernel-module-tda827x-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/tda827x.ko"

%files -n kernel-module-tda8290-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/tda8290.ko"

%files -n kernel-module-tda9887-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/tda9887.ko"

%files -n kernel-module-tea5761-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/tea5761.ko"

%files -n kernel-module-tea5767-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/tea5767.ko"

%files -n kernel-module-tua9001-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/tua9001.ko"

%files -n kernel-module-tuner-simple-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/tuner-simple.ko"

%files -n kernel-module-tuner-types-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/tuner-types.ko"

%files -n kernel-module-xc2028-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/xc2028.ko"

%files -n kernel-module-xc4000-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/xc4000.ko"

%files -n kernel-module-xc5000-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/tuners/xc5000.ko"

%files -n kernel-module-uvcvideo-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/usb"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/usb/uvc"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/usb/uvc/uvcvideo.ko"

%files -n kernel-module-v4l2-jpeg-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/v4l2-core"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/media/v4l2-core/v4l2-jpeg.ko"

%files -n kernel-module-cdc-eem-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/usb"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/usb/cdc_eem.ko"

%files -n kernel-module-pegasus-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/usb"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/usb/pegasus.ko"

%files -n kernel-module-rtl8150-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/usb"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/usb/rtl8150.ko"

%files -n kernel-module-ath-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ath"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ath/ath.ko"

%files -n kernel-module-ath10k-core-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ath"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ath/ath10k"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ath/ath10k/ath10k_core.ko"

%files -n kernel-module-ath10k-sdio-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ath"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ath/ath10k"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ath/ath10k/ath10k_sdio.ko"

%files -n kernel-module-brcmfmac-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/broadcom"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/broadcom/brcm80211"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/broadcom/brcm80211/brcmfmac"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/broadcom/brcm80211/brcmfmac/brcmfmac.ko"

%files -n kernel-module-brcmutil-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/broadcom"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/broadcom/brcm80211"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/broadcom/brcm80211/brcmutil"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/broadcom/brcm80211/brcmutil/brcmutil.ko"

%files -n kernel-module-mwifiex-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/marvell"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/marvell/mwifiex"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/marvell/mwifiex/mwifiex.ko"

%files -n kernel-module-mwifiex-pcie-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/marvell"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/marvell/mwifiex"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/marvell/mwifiex/mwifiex_pcie.ko"

%files -n kernel-module-mwifiex-sdio-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/marvell"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/marvell/mwifiex"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/marvell/mwifiex/mwifiex_sdio.ko"

%files -n kernel-module-wl12xx-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ti"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ti/wl12xx"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ti/wl12xx/wl12xx.ko"

%files -n kernel-module-wl18xx-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ti"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ti/wl18xx"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ti/wl18xx/wl18xx.ko"

%files -n kernel-module-wlcore-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ti"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ti/wlcore"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ti/wlcore/wlcore.ko"

%files -n kernel-module-wlcore-sdio-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ti"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ti/wlcore"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/net/wireless/ti/wlcore/wlcore_sdio.ko"

%files -n kernel-module-rn5t618-power-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/power"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/power/supply"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/power/supply/rn5t618_power.ko"

%files -n kernel-module-siox-bus-gpio-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/siox"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/siox/siox-bus-gpio.ko"

%files -n kernel-module-siox-core-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/siox"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/siox/siox-core.ko"

%files -n kernel-module-cdc-acm-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/class"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/class/cdc-acm.ko"

%files -n kernel-module-g-audio-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy/g_audio.ko"

%files -n kernel-module-g-ether-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy/g_ether.ko"

%files -n kernel-module-g-ffs-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy/g_ffs.ko"

%files -n kernel-module-g-mass-storage-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy/g_mass_storage.ko"

%files -n kernel-module-g-ncm-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy/g_ncm.ko"

%files -n kernel-module-g-serial-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy/g_serial.ko"

%files -n kernel-module-g-zero-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy/g_zero.ko"

%files -n kernel-module-gadgetfs-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/gadget/legacy/gadgetfs.ko"

%files -n kernel-module-ehset-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/misc"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/misc/ehset.ko"

%files -n kernel-module-usbtest-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/misc"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/misc/usbtest.ko"

%files -n kernel-module-ftdi-sio-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/serial"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/serial/ftdi_sio.ko"

%files -n kernel-module-option-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/serial"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/serial/option.ko"

%files -n kernel-module-usb-wwan-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/serial"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/serial/usb_wwan.ko"

%files -n kernel-module-usbserial-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/serial"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/usb/serial/usbserial.ko"

%files -n kernel-module-da9063-wdt-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/watchdog"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/drivers/watchdog/da9063_wdt.ko"

%files -n kernel-module-binfmt-misc-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs/binfmt_misc.ko"

%files -n kernel-module-msdos-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs/fat"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs/fat/msdos.ko"

%files -n kernel-module-isofs-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs/isofs"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs/isofs/isofs.ko"

%files -n kernel-module-nls-iso8859-15-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs/nls"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs/nls/nls_iso8859-15.ko"

%files -n kernel-module-udf-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs/udf"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/fs/udf/udf.ko"

%files -n kernel-module-crc-itu-t-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/lib"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/lib/crc-itu-t.ko"

%files -n kernel-module-crc7-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/lib"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/lib/crc7.ko"

%files -n kernel-module-libcrc32c-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/lib"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/lib/libcrc32c.ko"

%files -n kernel-module-bnep-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/net"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/net/bluetooth"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/net/bluetooth/bnep"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/net/bluetooth/bnep/bnep.ko"

%files -n kernel-module-snd-hwdep-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/sound"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/sound/core"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/sound/core/snd-hwdep.ko"

%files -n kernel-module-snd-usb-audio-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/sound"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/sound/usb"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/sound/usb/snd-usb-audio.ko"

%files -n kernel-module-snd-usbmidi-lib-6.1.38-fslc+g085682f3fc7e
%defattr(-,-,-,-)
%dir "/lib"
%dir "/lib/modules"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/sound"
%dir "/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/sound/usb"
"/lib/modules/6.1.38-fslc+g085682f3fc7e/kernel/sound/usb/snd-usbmidi-lib.ko"

