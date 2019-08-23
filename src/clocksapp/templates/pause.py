#!/usr/bin/env python
import os

#Assign string for simplified command construction
send = "irsend SEND_ONCE lircd.conf KEY_"

#Compose Control command
play = send + "PLAY"

os.system(play)
