ZynqMP-FPGA-Linux Example (0) for UltraZed
===========================================

ZynqMP-FPGA-Linux Example (0) binary and test code for UltraZed-EG-IOCC

## Requirement

 * Board: UltraZed-EG-IOCC
 * OS: ZynqMP-FPGA-Linux ([https://github.com/ikwzm/ZynqMP-FPGA-Linux](https://github.com/ikwzm/ZynqMP-FPGA-Linux)) v0.1.2

## Boot UltraZed-EG-IOCC and login fpga user

fpga'password is "fpga".

```
debian-fpga login: fpga
Password:
fpga@debian-fpga:~$
```
## Download this repository

```shell
fpga@debian-fpga:~$ mkdir examples
fpga@debian-fpga:~$ cd examples
fpga@debian-fpga:~/examples$ git clone https://github.com/ikwzm/ZynqMP-FPGA-Linux-Example-0-UltraZed gpio
fpga@debian-fpga:~/examples$ cd gpio
fpga@debian-fpga:~/examples/gpio$
```

## Setup

### Convert to Binary file from Bitstream file

```shell
fpga@debian-fpga:~/examples/gpio$ python3 fpga-bit-to-bin.py -f design_1_wrapper.bit design_1_wrapper.bin
Design name: b'design_1_wrapper;UserID=0XFFFFFFFF;Version=2017.2.1\x00'
Full bitstream
Partname b'xczu3eg-sfva625-1-i\x00'
Date b'2017/12/24\x00'
Time b'10:39:58\x00'
Found binary data: 5568668
Flipping data...
Writing data...
```

### Copy FPGA Binary file to /lib/firmware

```shell
fpga@debian-fpga:~/examples/gpio$ sudo cp design_1_wrapper.bin /lib/firmware
```

### Configuration FPGA with Device Tree Overlay

```shell
fpga@debian-fpga:~/examples/gpio$ dtc -I dts -O dtb -o fpga-load.dtb fpga-load.dts
fpga@debian-fpga:~/examples/gpio$ sudo mkdir /config/device-tree-overlays/fpga
fpga@debian-fpga:~/examples/gpio$ sudo cp fpga-load.dtb /config/device-tree/overlays/fpga/dtbo
[ 1462.560122] fpga_manager fpga0: writing design_1_wrapper.bin to Xilinx ZynqMP FPGA Manager
```

### Configuraiton PL Clock 0

```shell
fpga@debian-fpga:~/examples/gpio$ dtc -I dts -O dtb -o fclk0-zynqmp.dtb fclk0-zynqmp.dts
fpga@debian-fpga:~/examples/gpio$ sudo mkdir /config/device-tree-overlays/fclk0
fpga@debian-fpga:~/examples/gpio$ sudo cp fclk0-zynqmp.dtb /config/device-tree/overlays/fclk0/dtbo
[ 1830.238976] fclkcfg amba:fclk0: driver installed.
[ 1830.243617] fclkcfg amba:fclk0: device name    : fclk0
[ 1830.248737] fclkcfg amba:fclk0: clock  name    : pl0
[ 1830.253678] fclkcfg amba:fclk0: clock  rate    : 99999999
[ 1830.259085] fclkcfg amba:fclk0: clock  enabled : 1
[ 1830.263833] fclkcfg amba:fclk0: remove rate    : 1000000
[ 1830.269125] fclkcfg amba:fclk0: remove enable  : 0
```

### Install Uio Device Tree

```shell
fpga@debian-fpga:~/examples/gpio$ dtc -I dts -O dtb -o uio.dtb uio.dts
fpga@debian-fpga:~/examples/gpio$ sudo mkdir /config/device-tree/overlays/uio
fpga@debian-fpga:~/examples/gpio$ sudo cp uio.dtb /config/device-tree/overlays/uio/dtbo
```

## Flash the LED 

```shell
fpga@debian-fpga:~/examples/gpio$ sudo python3 led_on.py
```

