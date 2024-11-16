import speech_recognition as sr
import os
import time
import os
import RPi.GPIO as GPIO
from random import *
import urllib.request
import requests
import urllib.request
import threading
from time import sleep
import time





print(sr.__version__)
r = sr.Recognizer()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


buttonpin=38
buzzerpin=40
GPIO.setup(buttonpin,GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(buzzerpin,GPIO.OUT)
GPIO.output(buzzerpin,0)

motor1A = 33
motor1B = 31
motor2A = 37
motor2B = 35

GPIO_TRIGGER = 16
GPIO_ECHO = 18

# Set motor pins as output
GPIO.setup(motor1A, GPIO.OUT)
GPIO.setup(motor1B, GPIO.OUT)
GPIO.setup(motor2A, GPIO.OUT)
GPIO.setup(motor2B, GPIO.OUT)

GPIO.output(motor1A, GPIO.LOW)
GPIO.output(motor1B, GPIO.LOW)
GPIO.output(motor2A, GPIO.LOW)
GPIO.output(motor2B, GPIO.LOW)


GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance


def buzzering():
    GPIO.output(buzzerpin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(buzzerpin,GPIO.LOW)



while  True:
    dist = distance()
    print ("Measured Distance = %.1f cm" % dist)
    intdist=int(dist)
    if intdist < 100:
        print(" LESS THAN 100 Centimetemrs")
        print("--- STOP ---")
        GPIO.output(motor1A, GPIO.LOW)
        GPIO.output(motor1B, GPIO.LOW)
        GPIO.output(motor2A, GPIO.LOW)
        GPIO.output(motor2B, GPIO.LOW)
        buzzering()
        
    bpinstat = GPIO.input(buttonpin)
    print(bpinstat)
    if bpinstat==0:
        buzzering()
        try: 
            os.system("rec --encoding signed-integer --bits 16 --channels 1 --rate 16000 /home/rpi/Music/vrecord.wav&")
            #os.system("rec --encoding signed-integer --bits 16 --channels 1 --rate 16000 test1.wav&")
            
            time.sleep(6)
            os.system("sudo killall rec")
            time.sleep(1)
            harvard = sr.AudioFile('/home/rpi/Music/vrecord.wav')
            with harvard as source:
                audio = r.record(source)
            #datarecv=r.recognize_google(audio)
            #cdatarecv=str(datarecv)
            # recognize speech using Wit.ai
            WIT_AI_KEY = "IVSK6ITH37KKE5T4JFIKZ3BMEL26GGR5"  # Wit.ai keys are 32-character uppercase alphanumeric strings
            try:
                datarecv=r.recognize_wit(audio, key=WIT_AI_KEY)
                print("you said ",datarecv)
            except sr.UnknownValueError:
                datarecv="NOT UNDERSTOOD"
                print("Wit.ai could not understand audio")
            except sr.RequestError as e:
                datarecv="ERROR"
                print("Could not request results from Wit.ai service; {0}".format(e))    
                
            print("Predicted Output:",datarecv)
            if datarecv == "Forward":  # Forward
                print("--- FORWARD ---")
                GPIO.output(motor1A, GPIO.HIGH)
                GPIO.output(motor1B, GPIO.LOW)
                GPIO.output(motor2A, GPIO.HIGH)
                GPIO.output(motor2B, GPIO.LOW)
            elif datarecv == "Back":  # Backward
                print("--- BACK ---")
                GPIO.output(motor1A, GPIO.LOW)
                GPIO.output(motor1B, GPIO.HIGH)
                GPIO.output(motor2A, GPIO.LOW)
                GPIO.output(motor2B, GPIO.HIGH)
            elif datarecv == "Left":  # Left
                print("--- LEFT ---")
                GPIO.output(motor1A, GPIO.LOW)
                GPIO.output(motor1B, GPIO.HIGH)
                GPIO.output(motor2A, GPIO.HIGH)
                GPIO.output(motor2B, GPIO.LOW)
                
            elif datarecv == "Right":  # Right
                print("--- RIGHT ---")
                
                GPIO.output(motor1A, GPIO.HIGH)
                GPIO.output(motor1B, GPIO.LOW)
                GPIO.output(motor2A, GPIO.LOW)
                GPIO.output(motor2B, GPIO.HIGH)
                
            elif datarecv == "Stop":  # Stop
                print("--- STOP ---")
                GPIO.output(motor1A, GPIO.LOW)
                GPIO.output(motor1B, GPIO.LOW)
                GPIO.output(motor2A, GPIO.LOW)
                GPIO.output(motor2B, GPIO.LOW)
            
            datarecv=""
            
            
        except Exception as e:
            print("EXCEPTION:",e)
            print("**** FAILED TO RECORD TRY AGAIN ****")
            pass
        
    time.sleep(1)
   
   

