#!/usr/bin/env python
import os
import time

send = "irsend SEND_ONCE lircd.conf KEY_"
pause = send + "PLAY"

#Pause the timer
os.system(pause)
