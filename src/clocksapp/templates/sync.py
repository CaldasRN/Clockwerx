#!/usr/bin/env python
from datetime import datetime
import os
import time
import sys

#Assign string for simplified command construction
send = "irsend SEND_ONCE lircd.conf KEY_"

#Compose Control command
mode = send + "MODE"
ret = send + "RETURN"
t_set = send + "T-SET"

#Syncronize clock
def sync(request):

    #Get current time from RPi
    currentTime = str(datetime.now())
    month = int(currentTime[5]) * 10 + int(currentTime[6])

    if month < 3 or month > 10:
        #Convert from UTC time to EST time
        Easttime = str((int(currentTime[11]) * 10 + int(currentTime[12]) + 19) % 24)
        #Ensure 2 digit result
        if int(Easttime) < 10:
            Easttime = '0' + Easttime
    else:
        #Convert from UTC time to EDT time
        Easttime = str((int(currentTime[11]) * 10 + int(currentTime[12]) + 20) % 24)
        #Ensure 2 digit result
        if int(Easttime) < 10:
            Easttime = '0' + Easttime

    #Compose Time digits
    digit1 = send + Easttime[0]
    digit2 = send + Easttime[1]
    digit3 = send + currentTime[14]
    digit4 = send + currentTime[15]
    digit5 = send + currentTime[17]
    digit6 = send + currentTime[18]

    #Set clock to current time
    os.system(t_set)
    os.system(digit1)
    os.system(digit2)
    os.system(mode)
    os.system(digit3)
    os.system(digit4)
    os.system(mode)
    os.system(digit5)
    os.system(digit6)
    os.system(ret)
    return HttpResponse('Time')
