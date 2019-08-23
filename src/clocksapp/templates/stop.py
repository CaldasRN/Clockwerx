#!/usr/bin/env python
import os

#Assign string for simplified command construction
send = "irsend SEND_ONCE lircd.conf KEY_"

#Compose Control command
cd_set = send + "CD-SET"
ret = send + "RETURN"

#Stop any active timers and show clock
os.system(cd_set)
os.system(cd_set)
os.system(cd_set)
os.system(ret)
