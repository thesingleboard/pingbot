#!/bin/python
import os
import socket
import time
import calendar

#git URL
GITURL = os.getenv('GITURL',None)

#hostname
HOSTNAME = socket.gethostname()

#Git Username
GITUSER = os.getenv('GITUSER',None)

#GIT user token. Needs to be generated in Git or can be plain password.
GITTOKEN = os.getenv('GITTOKEN',None)

#GIT root direcrtory. Directory where git clones repos to
GITROOT = os.getenv('GITROOT',os.environ['HOME'])

#ip file name path within the gitroot
IPFILE = os.getenv('HOSTS',hosts)

"""
#The GPIO pins to use for sensors
PINS = os.getenv('PINS',None)
#Take comma seperated string and turn into list so it can be used.
PINS = PINS.split(',')

#Time to sleep in seconds
SLEEP = os.getenv('SLEEP',None)

# on the PiOLED this pin isnt used
RST = os.getenv('RST',None)

#The time interval
INTERVAL = os.getenv('INTERVAL',10)
INTERVAL = int(INTERVAL)

#physical network name wlan0 or eth0
PHYSNET = os.getenv('PHYSNET',None)

#mgtt broker host, IP or URL
MQTTBROKER = os.getenv('MQTTBROKER',None)

MQTTPORT = os.getenv('MQTTPORT',None)
MQTTPORT = int(MQTTPORT)

SSLCERTPATH = os.getenv('SSLCERTPATH',None)

SSLCERT = os.getenv('SSLCERT',None)

#defaults to one hour interval
STATUSINTERVAL = os.getenv('STATUSINTERVAL',3600)

#get the epoc time 
STARTOFTIME = calendar.timegm(time.gmtime())

#DC = 23
#SPI_PORT = 0
#SPI_DEVICE = 0
"""

CONFIG = {  'GITURL':GITURL,
            'HOSTNAME':HOSTNAME,
            'GITUSER':GITUSER,
            'GITTOKEN':GITTOKEN,
            'GITROOT':GITROOT
            }