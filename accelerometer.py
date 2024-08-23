#!/usr/bin/python

import time
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # This command is to Disable Warning....!!!!

import requests
import json
import Adafruit_ADS1x15
import smtplib
import requests
import json
buzzer = 20
GPIO.setup(20, GPIO.OUT)
import sys
import urlopen
import urllib

from time import sleep
# Enter Your API key here
User1API = '90ZTHLRU35UTOEO8' 

# URL where we will send the data, Don't change it
baseURL1 = 'https://api.thingspeak.com/update?api_key=%s' % User1API
# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()
VALMAX = 15000
GAIN = 1
adcValue = 0;
offsetVoltage = 100;
msg="Accident Detected"

def sms_send():
    url="https://www.fast2sms.com/dev/bulk"
    params={
  
        "authorization":"fvaKUPuNimZCWE8MOpB9YjLGs4nyeg6lzRqS71JXH5QFw3cktDIm3puGNrOFLP2Bq0AzjDfsWtVCTe6x",
        "sender_id":"SMSINI",
        "message":msg,
        "language":"english",
        "route":"p",
        "numbers":"9607181257"
    }
    rs=requests.get(url,params=params)

def mail():
    
        import smtplib
        from email.message import EmailMessage
        import imghdr

        Sender_Email = "projectandroidengg@gmail.com"
        Reciever_Email = "srcdocs190@gmil.com"
        Password ='9689544204'
        newMessage = EmailMessage()    #creating an object of EmailMessage class
        newMessage['Subject'] = "Test Email from women safety" #Defining email subject
        newMessage['From'] = Sender_Email  #Defining sender email
        newMessage['To'] = Reciever_Email  #Defining reciever email


        import requests 
        api_address = "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
                
        import json
        location_req_url='http://api.ipstack.com/103.51.95.183?access_key=a7003977af457525708100fca423928d'
        r = requests.get(location_req_url)
        location_obj = json.loads(r.text)
                
        lat = location_obj['latitude']
        lon = location_obj['longitude']
        latitude = lat
        longitude = lon
        print(str(latitude))
        print(str(longitude))


        newMessage.set_content('Hi,Accident detected.Please help me urgently... \n Here I attached my location: \n Latitude is:'+str(latitude)+'\n Langitude is:'+str(longitude)) #Defining email body

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            
            smtp.login(Sender_Email, Password)              
            smtp.send_message(newMessage)

def mapp( x, in_min, in_max, out_min, out_max) :
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;

def sensor_position ():
	pos = 0
	x = adc.read_adc(0, gain=GAIN)
	y = adc.read_adc(1, gain=GAIN)
	z = adc.read_adc(2, gain=GAIN)

	Xval = mapp (x,0,VALMAX,0,255)
	Yval = mapp (y,0,VALMAX,0,255)
	Zval = mapp (z,0,VALMAX,0,255)
	print ("X:"+str (Xval))
	print ("Y:"+str (Yval))
	print ("Z:"+str (Zval))
	conn = baseURL1 + '&field3=%s&field4=%s&field5=%s' % (Xval,Yval,Zval)
	request = urllib.request.Request(conn)
	responce = urllib.request.urlopen(request)
	responce.close()
	time.sleep(2)
	if (Xval > 235 or Xval < 210) :
		pos = 1	
		return pos	
	if (Yval > 230 or Yval < 205) :
		pos = 1
		return pos
	else:
		pos = 0
		return pos
	
	
# Main loop.
while True:
	pos = sensor_position()
	
	if pos == 1 :
		print("Accident Detected")
		sms_send()
		#mail()
		GPIO.output(20, True)
		time.sleep(0.5)
		GPIO.output(20, False)
		
	else :
		print("Normal Condition")	
		
	time.sleep(1)


