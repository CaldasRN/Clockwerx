#!/usr/bin/env python
import os
import sys

#Assign string for simplified command construction
send = "irsend SEND_ONCE lircd.conf KEY_"

dim = int(sys.argv[1])
i = 1

#Compose Control command
plus = send + "+"
minus = send + "-"

if dim > 0 and dim < 8:
    os.system(minus)
    os.system(minus)
    os.system(minus)
    os.system(minus)
    os.system(minus)
    os.system(minus)
    os.system(minus)
    while i < dim:
        os.system(plus)
        i += 1
