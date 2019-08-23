#!/usr/bin/env python
import os
import sys
import paramiko
import time
# from subprocess import check_output

def ConnectRunCode(currentIP, script):

    # Connect to remote host
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(currentIP, username='pi', password='raspberry')

    # Setup sftp connection and transmit this script
    #sftp = client.open_sftp()
    #sftp.put(__file__, '/tmp/myscript.py')
    #sftp.close()

    # Run the transmitted script remotely without args and show its output.
    # SSHClient.exec_command() returns the tuple (stdin,stdout,stderr)
    stdout = client.exec_command('python /home/pi/clock/Clockwerx/src/clocksapp/templates/' + script)[1]
    for line in stdout:
        # Process each line in the remote output
        print line

    client.close()

def meshloop(Range,IPs,script):

    try:    
        
        for x in Range:
            currentIP = IPs + x
            print (currentIP)
            ConnectRunCode(currentIP, script)
    except IndexError:
        pass

def main():
    print os.name

if __name__ == '__main__':

    host = "swx-u-RPi-"
    RPi = ["spare", "tours", "conconrd", "stalingrad", "marathon", "blacksea", "normandy", "auditorium", "events"]
    IPs = "192.168.12."
    Range = ["135", "143"]
    #Range = ["135", "136", "137", "138", "139", "140", "141", "142", "143"]
    Scripts = ["power", "pause", "stop", "sync", "milTime"]
 
    if (sys.argv[1] in Scripts):
        script = sys.argv[1] + '.py'
        meshloop(Range, IPs, script)
    elif (len(sys.argv) > 2 and sys.argv[1] == "dim"):
        script = sys.argv[1] + '.py ' + sys.argv[2]
        meshloop(Range, IPs, script)
    elif (len(sys.argv) > 2 and sys.argv[1] == "timer"):
        script = sys.argv[1] + '.py ' + sys.argv[2]
        meshloop(Range, IPs, script)
        #time.sleep( 5 )
        print "First Pause"
        meshloop(Range, IPs, "pause.py")
        time.sleep(1)
        print "Second Sleep"
        meshloop(reversed(Range), IPs, 'pause.py')

    else:
        sys.exit(1)
    
    sys.exit(0)

    # No cmd-line args provided, run script normally
    main()
