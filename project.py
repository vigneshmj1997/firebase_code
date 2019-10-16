



import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
cred=credentials.Certificate("/home/pi/Desktop/iot3-7d5b8-firebase-adminsdk-.json")
firebase_admin.initialize_app(cred,{"databaseURL":'https://iot.firebaseio.com/'})

ref=db.reference()
tem=None
second=None
while(True):
	tem=ref.get()
	print(tem)
	if(tem["2131165222"]=="on"):
		GPIO.output(18,GPIO.HIGH)
			
	if(tem["2131165222"]!="on"):
		GPIO.output(18,GPIO.LOW)

	if(tem["2131165227"]=="on"):
		GPIO.output(22,GPIO.HIGH)
	if(tem["2131165227"]!="on"):
		GPIO.output(22,GPIO.LOW)
	if(tem["2131165231"]=="on"):
		GPIO.output(24,GPIO.HIGH)
	if(tem["2131165231"]!="on"):
		GPIO.output(24,GPIO.LOW)
	if(tem["2131165225"]=="on"):
		GPIO.output(25,GPIO.HIGH)
	if(tem["2131165225"]!="on"):
		GPIO.output(25,GPIO.LOW)
	if(tem["2131165223"]=="on"):
		GPIO.output(6,GPIO.HIGH)
	if(tem["2131165223"]!="on"):
		GPIO.output(6,GPIO.LOW)
	if(tem["2131165224"]=="on"):
		GPIO.output(17,GPIO.HIGH)
	if(tem["2131165224"]!="on"):
		GPIO.output(17,GPIO.LOW)
