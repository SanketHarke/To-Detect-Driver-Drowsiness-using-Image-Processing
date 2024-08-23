import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # This command is to Disable Warning....!!!!
import sys
import urlopen
import urllib

from time import sleep
# Enter Your API key here
User1API = '90ZTHLRU35UTOEO8' 

# URL where we will send the data, Don't change it
baseURL1 = 'https://api.thingspeak.com/update?api_key=%s' % User1API
FLAME = 26
buzzer = 20
GPIO.setup(26, GPIO.IN)
GPIO.setup(20, GPIO.OUT)
while True:
    j=GPIO.input(FLAME)
    print(j)
    conn = baseURL1 + '&field2=%s' % (j)
    request = urllib.request.Request(conn)
    responce = urllib.request.urlopen(request)
    responce.close()
    if j==0 :
        print('FLAME Detected!')
        time.sleep(0.5)
        GPIO.output(20, True)
        time.sleep(0.5)
        GPIO.output(20, False)
       
       
    else :
        print ('FLAME Not Detected!')
        time.sleep(0.1)
        GPIO.output(20, False)
