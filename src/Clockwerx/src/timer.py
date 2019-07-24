#!/usr/bin/env python
import os
import time
import sys

send = "irsend SEND_ONCE lircd.conf KEY_"

digit1 = send + sys.argv[1]
digit2 = send + sys.argv[2]
digit3 = send + sys.argv[3]
digit4 = send + sys.argv[4]
digit5 = send + sys.argv[5]
digit6 = send + sys.argv[6]

cd_set = send + "CD-SET"
mode = send + "MODE"
play = send + "PLAY"

#Set timer with provided perameters
os.system(cd_set)
os.system(cd_set)
os.system(mode)
os.system(mode)
os.system(digit1)
os.system(digit2)
os.system(mode)
os.system(digit3)
os.system(digit4)
os.system(mode)
os.system(digit5)
os.system(digit6)
os.system(play)
