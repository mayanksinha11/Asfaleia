# This script receives and processes the data that the NODEMCU module (that has the MQ6 gas leak sensor attached to it) sends via MQTT protocol
import paho.mqtt.client as mqtt
from twilio.rest import Client
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)


def on_connect(client, userdata, flags, rc):  
    #Mqtt Topic
    client.subscribe("esp/tes")

 

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    if msg.payload == "0":
        print("Gas leak detected")
        

        from twilio.rest import Client
        #initiating call via Twilio web service
        account_sid = "ACf6e9b7ca6a43c5436d05fa8de1a84817"
        auth_token = "6947b59c0b9b521089487c499acf8681"
        client = Client(account_sid, auth_token)
        print "calling....."
        
        call = client.calls.create(
        to="The number to be called",
        from_="Your Twilio number",
        url="http://demo.twilio.com/docs/voice.xml"
        )
        print("Switching on exhaust")
        i=1
        # switching On the Realy module to which the exhaust fan is attached
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

client.connect("The IP of the raspberry Pi,on which the MQtt server is running  ", 1883, 60)
 
client.loop_forever()
GPIO.cleanup();
