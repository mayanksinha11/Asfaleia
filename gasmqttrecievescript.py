import paho.mqtt.client as mqtt
from twilio.rest import Client
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)


def on_connect(client, userdata, flags, rc):  
    client.subscribe("esp/tes")

 

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    if msg.payload == "0":
        print("Gas leak detected")
        

        from twilio.rest import Client
        
        account_sid = "ACf6e9b7ca6a43c5436d05fa8de1a84817"
        auth_token = "6947b59c0b9b521089487c499acf8681"
        client = Client(account_sid, auth_token)
        print "calling....."
        
        call = client.calls.create(
        to="+919837311207",
        from_="+17206051065",
        url="http://demo.twilio.com/docs/voice.xml"
        )
        print("Switching on exhaust")
        i=1
        while i<100:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(4,GPIO.OUT)
            GPIO.output(4,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(4,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(4,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(4,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(4,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(4,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(4,GPIO.HIGH)
            time.sleep(0.1)
            i=i+1
        time.sleep(300);



       

    if msg.payload == "1":
        print("Everthing is fine, chill")
        time.sleep(1)
        

        
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("192.168.1.102", 1883, 60)
 
client.loop_forever()
GPIO.cleanup();
