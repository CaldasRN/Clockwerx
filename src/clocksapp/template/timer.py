#!/usr/bin/env python
import os
import time
import sys

send = "irsend SEND_ONCE lircd.conf KEY_"

digit1 = send + sys.argv[1][0]
digit2 = send + sys.argv[1][1]
digit3 = send + sys.argv[1][3]
digit4 = send + sys.argv[1][4]
digit5 = send + sys.argv[1][6]
digit6 = send + sys.argv[1][7]

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
