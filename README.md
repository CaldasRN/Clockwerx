# Clockwerx
Use RPi to Record buttons from clock remote to control clock with Rpi 'IR Remote Shield v1.0' over the network

## Load Image to SD Card
#Insert SD card into computer

#Identify SD card device name

`sudo fdisk -l`

#SD card will be list as something like:

`Disk /dev/mmcblk0: 29.7 GiB, 31914983424 bytes, 62333952 sectors`

#Install Jessie Image onto SD card of RPi

`sudo dd if=2017-07-05-raspbian-jessie.img of=/dev/mmcblk0 bs=4M status=progress conv=fsync`

#eject SD card from computer and put into Rpi

#boot the RPi

#connect RPi to network

#enable ssh on RPI:

`sudo raspi-config`

#select 'Interfacing Options' and select 'SSH' to enable

#On PC ssh into RPi

`ssh pi@<RPI IP Address>`

#if you get this warning:

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

#execute the command as directed

`ssh-keygen -f "/home/user/.ssh/known_hosts" -R "<RPi IP Address>"`

#then run ssh again

#the default password for user pi is 'raspberry'

#Update and upgrade programs
```
sudo apt-get update

sudo apt-get -y upgrade
```

#Install vim (or what ever editor you prefer)
`sudo apt-get install vim`
