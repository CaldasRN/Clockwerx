#!/usr/bin/env python
import os
import time

#Press power button on clock
os.system('sudo kill $(pidof lircd)')
time.sleep(1)
os.system('sudo lircd --device /dev/lirc0')
time.sleep(1)
os.system('irsend SEND_ONCE lircd.conf KEY_POWER')
