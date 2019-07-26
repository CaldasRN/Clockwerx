from django.shortcuts import render
from datetime import datetime
import os
import time
import sys

#Assign string for simplified command construction
send = "irsend SEND_ONCE lircd.conf KEY_"

#Compose Control command
cd_set = send + "CD-SET"
mode = send + "MODE"
play = send + "PLAY"
ret = send + "RETURN"
t_set = send + "T-SET"
power = send + "POWER"

#Press power button on clock
def powerBtn(request):
    os.system('sudo kill $(pidof lircd)')
    time.sleep(1)
    os.system('sudo lircd --device /dev/lirc0')
    time.sleep(1)
    os.system(power)
    return HttpResponse('Power')

#Set timer on clock
def timer(request):

    #Get Time String
    time = request.GET.get('time')

    #Compose Time digits
    digit1 = send + time[0]
    digit2 = send + time[1]
    digit3 = send + time[3]
    digit4 = send + time[4]
    digit5 = send + time[6]
    digit6 = send + time[7]

    #Set timer with provided parameters
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
    return HttpResponse('Timer')

#Syncronize clock
def sync(request):

    #Get current time from RPi
    currentTime = str(datetime.now())
    month = int(currentTime[5]) * 10 + int(currentTime[6])

    if month < 3 or month > 10:
        #Convert form UTC time to EST time
        Easttime = str((int(currentTime[11]) * 10 + int(currentTime[12]) + 19) % 24)
    else:
        #Convert form UTC time to EDT time
        Easttime = str((int(currentTime[11]) * 10 + int(currentTime[12]) + 20) % 24)

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

#Pause Timer
def pause(request):

    os.system(play)
    return HttpResponse('Pause')

#Stop Timer and show time
def stop(request):

    os.system(cd_set)
    os.system(cd_set)
    os.system(cd_set)
    os.system(ret)
    return HttpResponse('Stop')

#Toggle between Military time and Regular time
def milTime(request):

    mil = send + '0'
    os.system(mil)
    return HttpResponse('MilTime')
