# Clockwerx
Use RPi to Record buttons from clock remote to control clock with Rpi 'IR Remote Shield v1.0' over the network

## Load Image to SD Card
Insert SD card into computer and identify SD card device name

`sudo fdisk -l`

The SD card will be listed as something like:

`Disk /dev/mmcblk0: 29.7 GiB, 31914983424 bytes, 62333952 sectors`

Install Jessie Image onto SD card of RPi

`sudo dd if=2017-07-05-raspbian-jessie.img of=/dev/mmcblk0 bs=4M status=progress conv=fsync`

Eject SD card from computer and put into Rpi

Boot the RPi and connect the RPi to your network, then enable ssh on RPI:

`sudo raspi-config`

Select 'Interfacing Options' and select 'SSH' to enable

On PC ssh into RPi

`ssh pi@<RPI IP Address>`

If you get this warning:
```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ECDSA key sent by the remote host is
SHA256:E<given SHA256 key>o.
Please contact your system administrator.
Add correct host key in /home/user/.ssh/known_hosts to get rid of this message.
Offending ECDSA key in /home/user/.ssh/known_hosts:6
  remove with:
  ssh-keygen -f "/home/user/.ssh/known_hosts" -R "<RPi IP Address>"
ECDSA host key for 192.168.1.194 has changed and you have requested strict checking.
Host key verification failed.
```
Execute the command as directed

`ssh-keygen -f "/home/user/.ssh/known_hosts" -R "<RPi IP Address>"`

Then run ssh again. The default password for user pi is 'raspberry'.

Update and upgrade programs
```
sudo apt-get update

sudo apt-get -y upgrade
```

## Installing and Configuring the LIRC Package
To control a device with an IR receiver, the IR LED transmitter must send a specific signal sequence, and the LIRC package, which emulates the infrared signals of many remote controls, is the perfect tool for the job. LIRC is available in the Raspbian software repositories, so installing it on Raspberry Pi is just a matter of running

`sudo apt-get install lirc`

If needed install vim (or what ever editor you prefer)

`sudo apt-get install vim`

Once you've done that, you need to enable and configure the lirc_rpi kernel module. To do so, open modules in an editor

`sudo vim /etc/modules`

and add the lines below to the file:
```
lirc_dev
lirc_rpi gpio_out_pin=17 gpio_in_pin=18
```
Make sure that the gpio_out_pin parameter points to the pin controlling the IR LED (in this case, it's pin 17). Next, open the file /etc/lirc/hardware.conf as before with sudo and add the following configuration to the file:
```
LIRCD_ARGS="--uinput"
LOAD_MODULES=true
DRIVER="default"
DEVICE="/dev/lirc0"
MODULES="lirc_rpi"
LIRCD_CONF=""
LIRCMD_CONF=""
```
Now, reboot the Raspberry Pi using the

`sudo reboot`

Next, replace the /etc/lirc/lircd.conf file with the provided lircd.conf file and restart LIRC with:

`sudo /etc/init.d/lirc restart`
