from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import os
import time
import sys
import requests
from subprocess import check_output

####################################################################
#This part is to convert the Django project into a REST API and to 
#handle.GET and.GET.requests


from clocksapp.models import Timer
from clocksapp.serializers import TimerSerializer
from rest_framework import generics

class TimerListCreate(generics.ListCreateAPIView):
    queryset = Timer.objects.all()
    serializer_class = TimerSerializer


####################################################################


#Assign string for simplified command construction
send = 'irsend SEND_ONCE lircd.conf KEY_'

#Compose Control command
cd_set = send + 'CD-SET'
mode = send + 'MODE'
play = send + 'PLAY'
ret = send + 'RETURN'
t_set = send + 'T-SET'
power = send + 'POWER'
plus = send + '+'
minus = send + '-'

#Press power button on clock
@csrf_exempt
def powerBtn(request):
    os.system('sudo kill $(pidof lircd)')
    time.sleep(1)
    os.system('sudo lircd --device /dev/lirc0')
    time.sleep(1)
    os.system(power)
    return HttpResponse('OK')

#Set timer on clock
@csrf_exempt
def timer(request):

    #Determine which query is used

    if request.method == 'GET' and 'time' in request.GET:
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
        return HttpResponse('OK')

    #Pause Timer
    if request.method == 'GET' and 'pause' in request.GET:
        os.system(play)
        return HttpResponse('OK')

    #Stop Timer and show time
    if request.method == 'GET' and 'stop' in request.GET:
        os.system(cd_set)
        os.system(cd_set)
        os.system(cd_set)
        os.system(ret)
        return HttpResponse('OK')

#Syncronize clock
@csrf_exempt
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
    return HttpResponse('OK')

#Toggle between Military time and Regular time
@csrf_exempt
def milTime(request):

    mil = send + '0'
    os.system(mil)
    return HttpResponse('OK')

#Dim Clock
@csrf_exempt
def dim(request):
    if request.method == 'GET' and 'bright' in request.GET:
        bright = int(request.GET.get('bright'))

        if bright > 0 and bright < 8:
            os.system(minus)
            os.system(minus)
            os.system(minus)
            os.system(minus)
            os.system(minus)
            os.system(minus)
            os.system(minus)

            i = 1
            while i < bright:
                os.system(plus)
                i += 1
    return HttpResponse('OK')

@csrf_exempt
def meshctl(request):

    IPs = '192.168.12.'
    #Range = ['135', '140', '143']
    Range = ['135', '136', '138', '139', '140', '141', '143']
    #Range = ['135', '136', '137', '138', '139', '140', '141', '142', '143']

    myIP = str(check_output(['hostname', '-I']))
    myIP = myIP[2:16]

    if request.method == 'GET' and 'bright' in request.GET:
        Script = 'dim'
        ARG = 'bright=' + request.GET.get('bright')
    
    if request.method == 'GET' and 'time' in request.GET:
        Script = 'timer'
        ARG = 'time=' + request.GET.get('time')

    if request.method == 'GET' and 'pause' in request.GET:
        Script = 'timer'
        ARG = 'pause=1'
    
    if request.method == 'GET' and 'stop' in request.GET:
        Script = 'timer'
        ARG = 'stop=1'

    if request.method == 'GET' and 'power' in request.GET:
        Script = 'power'
        ARG = 'power'
    
    if request.method == 'GET' and 'sync' in request.GET:
        Script = 'sync'
        ARG = 'sync'
    
    if request.method == 'GET' and 'milTime' in request.GET:
        Script = 'milTime'
        ARG = 'milTime'
    
    for x in Range:
        currentIP = IPs + x
        #if currentIP == myIP:
        #    continue
        line = 'http://' + currentIP + '/clocksapp/' + Script + '/?' + ARG
        requests.get(line)
    return HttpResponse('OK')
