#!/usr/bin/env python
import os
import time
import sys

digit1 = "irsend SEND_ONCE /home/pi/lircd.conf KEY_" + sys.argv[1]
digit2 = "irsend SEND_ONCE /home/pi/lircd.conf KEY_" + sys.argv[2]
digit3 = "irsend SEND_ONCE /home/pi/lircd.conf KEY_" + sys.argv[3]
digit4 = "irsend SEND_ONCE /home/pi/lircd.conf KEY_" + sys.argv[4]
digit5 = "irsend SEND_ONCE /home/pi/lircd.conf KEY_" + sys.argv[5]
digit6 = "irsend SEND_ONCE /home/pi/lircd.conf KEY_" + sys.argv[6]



#Set timer for 10 min
os.system('irsend SEND_ONCE /home/pi/lircd.conf KEY_CD-SET')
os.system('irsend SEND_ONCE /home/pi/lircd.conf KEY_CD-SET')
os.system('irsend SEND_ONCE /home/pi/lircd.conf KEY_MODE')
os.system('irsend SEND_ONCE /home/pi/lircd.conf KEY_MODE')
os.system(digit1)
os.system(digit2)
os.system('irsend SEND_ONCE /home/pi/lircd.conf KEY_MODE')
os.system(digit3)
os.system(digit4)
os.system('irsend SEND_ONCE /home/pi/lircd.conf KEY_MODE')
os.system(digit5)
os.system(digit6)
os.system('irsend SEND_ONCE /home/pi/lircd.conf KEY_PLAY')
