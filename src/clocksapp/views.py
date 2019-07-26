from django.shortcuts import render

# Create your views here.

import os
import time
import sys
"""
#Test
def austin(request):
    return HttpResponse('Hi')
"""
#Press power button on clock
def powerBtn(request):
    os.system('sudo kill $(pidof lircd)')
    time.sleep(1)
    os.system('sudo lircd --device /dev/lirc0')
    time.sleep(1)
    os.system('irsend SEND_ONCE lircd.conf KEY_POWER')
    return HttpResponse('')

#Set timer on clock
def timer(request):
    #Assign string for simplified command construction
    send = "irsend SEND_ONCE lircd.conf KEY_"

    #Convert provided ints to string to access each digit
    time = str(request.GET.get('time'))

#    hour = str(request.GET.get('hour'))
#    min = str(request.GET.get('min'))
#    sec = str(request.GET.get('sec'))

#    hour = str(hour)
#    min = str(min)
#    sec = str(sec)

    #Compose Time digits
    digit1 = send + time[0]
    digit2 = send + time[1]
    digit3 = send + time[3]
    digit4 = send + time[4]
    digit5 = send + time[6]
    digit6 = send + time[7]

    #Compose Control command
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
