from django.shortcuts import render

# Create your views here.

import os
import time
import sys

#Press power button on clock
def powerBtn(request):
    os.system('sudo kill $(pidof lircd)')
    time.sleep(1)
    os.system('sudo lircd --device /dev/lirc0')
    time.sleep(1)
    os.system('irsend SEND_ONCE lircd.conf KEY_POWER')
    return HttpResponse('')

#Set timer on clock
def timer(request,hour,min,sec):

    send = "irsend SEND_ONCE lircd.conf KEY_"
    hour = str(hour)
    min = str(min)
    sec = str(sec)

    digit1 = send + hour[0]
    digit2 = send + hour[1]
    digit3 = send + min[0]
    digit4 = send + min[1]
    digit5 = send + sec[0]
    digit6 = send + sec[1]

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
    return HttpResponse('')
