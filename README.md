# Next step
Create docker container to facilitate expansion and maintenance

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
Make sure that the gpio_out_pin parameter points to the pin controlling the IR LED (in this case, it's pin 17). 

Next, open the file /etc/lirc/hardware.conf as before with sudo and add the following configuration to the file:
```
LIRCD_ARGS="--uinput"
LOAD_MODULES=true
DRIVER="default"
DEVICE="/dev/lirc0"
MODULES="lirc_rpi"
LIRCD_CONF=""
LIRCMD_CONF=""
```
Finally, open the file /boot/config.txt and add:

`dtoverlay=lirc-rpi,gpio_in_pin=18,gpio_out_pin=17`

Now, reboot the Raspberry Pi using the

`sudo reboot`

Once rebooted, ssh back into the RPi and replace the /etc/lirc/lircd.conf file with the provided lircd.conf file and restart LIRC with:

`sudo /etc/init.d/lirc restart`

Now create the device:

`sudo lircd --device /dev/lirc0`

### Apache2 + Django


Update Software:

```
sudo apt-get update
sudo apt-get upgrade
```

Install Apache2:

```
sudo apt-get install apache2 -y

sudo apt-get install libapache2-mod-wsgi-py3

sudo apt-get install libapache2-mod-wsgi # if using Python2
```

Install Pip & Django:

```
sudo apt-get install python-setuptools python-dev build-essential

sudo easy_install pip 

sudo pip install django==X.Y.Z #where X.Y.Z is the version number

sudo pip install django==1.10.3

sudo pip install virtualenv 

```

Start Django Project in the virtual environment:
```
cd ~/

mkdir clock && cd clock

mkdir Clockwerx && cd Clockwerx

virtualenv -p python3 .

source bin/activate

pip install django==1.10.3

django-admin.py startproject Clockwerx

mv /home/pi/clock/Clockwerx/Clockwerx /home/pi/clock/Clockwerx/src
```

Apache2 Settings:

```
sudo nano /etc/apache2/sites-available/000-default.conf
```
Note: If errors happen with below, just do the following and it will re-install apache:

```
sudo apt-get purge apache2 # removes apache2

sudo apt-get install apache2 -y # reinstalls it

```

```     
<VirtualHost *:80>
    ServerName www.example.com

    ServerAdmin webmaster@localhost

    Alias /static /home/pi/clock/Clockwerx/static
        <Directory /home/pi/clock/Clockwerx/static>
           Require all granted
         </Directory>

    <Directory /home/pi/clock/Clockwerx/src/Clockwerx>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess Clockwerx python-path=/home/pi/clock/Clockwerx/src:/home/pi/clock/Clockwerx/lib/python2.7/site-packages
    WSGIProcessGroup Clockwerx
    WSGIScriptAlias / /home/pi/clock/Clockwerx/src/Clockwerx/wsgi.py


    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>

```

Restart Apache:

```
# Restart in two ways:
sudo apachectl restart
sudo service apache2 restart


# Start Apache in two ways:
sudo apachectl start
sudo service apache2 start

# Stop Apache in two ways:
sudo apachectl stop
sudo service apache2 stop
```

Set Ownership of Database to Pi user for Django
```
sudo adduser $USER www-data
sudo chown www-data:www-data /home/$USER/clock/Clockwerx    
sudo chown www-data:www-data /home/$USER/clock/Clockwerx/src/db.sqlite3
sudo chmod -R 775 ~/clock/Clockwerx

# if above fails, try (thanks Mike!):
sudo chown -R www-data:www-data ~/clock/Clockwerx
sudo chown www-data:www-data /home/pi/clock/Clockwerx/src
# or if a new project
sudo chown -R www-data:www-data ~/clock/<your-virtuaenv-name>
sudo chown www-data:www-data /home/pi/clock/<your-virtuaenv-name>/src/
```

Enabling module wsgi
```
sudo a2enmod wsgi
```

# Set TimeZone and Sync RPi
To update the RPi to the correct timezone, run the following commands
```
timedatectl set-ntp 1
timedatectl set-timezone "America/New_York"
```

# Add auto-update cron job
Edit the root crontab:
```
sudo crontab -e 
```
and add the following line:
```
32 02 * * * /home/pi/clock/Clockwerx/update_system
```
The update_system script can be run manually (as root) at any time to update system packages and the Clockwerx code.