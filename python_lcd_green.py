#!/bin/bash
# testing the python language
# to run file use command line : python hello.py

#for working with GPIO: apt-get install python-rpi.gpio

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # set board mode to Broadcom
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

GPIO.output(17,1) #turn on pin 17
GPIO.output(18,1) #turn on pin 18

###### THIS IS FOR WORKING WITH PINS DIRECTLY #######

