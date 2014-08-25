#!/usr/bin/python
# -*- coding: utf-8 -*-
#import serial
import RPi.GPIO as GPIO
import time
import os, sys
# Set the numbering sequence of the pins, then set pins ten and twelve
#to output, and pin eight to input.
GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.IN) # HIGH || LOW type switch
GPIO.setwarnings(False)
statement=False
from twython import Twython
#fill in personal oAuth Twitter app crendentials below
APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN =''
OAUTH_TOKEN_SECRET=''
 

twitter = Twython(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)

while True:

	if(GPIO.input(8)==GPIO.LOW and statement==False): # if the door is opened
		os.system("fswebcam -D 3 -F 1 -r 640x480 --no-banner --png --save /home/pi/test.png")
		photo = open('/home/pi/test.png', 'rb')
		twitter.update_status_with_media(status='Raspberry Pi & Python security cam tweet', media=photo)
		print('DOOR OPENED, TWEET SENT')
		time.sleep(5)
	elif(GPIO.input(8)==GPIO.HIGH) : 
		print('DOOR CLOSED')
		time.sleep(2)
#end program


#     Daniel Jay Bertner Security Camera for the Raspberry Pi 2014
