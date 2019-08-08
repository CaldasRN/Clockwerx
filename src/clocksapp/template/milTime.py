#!/usr/bin/env python
import os

#Assign string for simplified command construction
send = "irsend SEND_ONCE lircd.conf KEY_"

mil = send + '0'
os.system(mil)
