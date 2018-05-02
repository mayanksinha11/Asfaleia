import RPi.GPIO as GPIO
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from SimpleCV import Image, Camera

# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token can be found at https://www.twilio.com/console
account_sid = "AC0ae86014fe91789e86a3e4195125709f"
auth_token = "0b3c35d9918e9d4fa12d1d454f7e60ba"
client = Client(account_sid, auth_token)



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# setting up output for the buzzer
GPIO.setup(17,GPIO.OUT)
# setting up input from the PIR sensor
GPIO.setup(18,GPIO.IN)
#setting up input from the face recognition script
GPIO.setup(24,GPIO.IN)
#setting up input from fingerprint sensor module
GPIO.setup(21,GPIO.IN)

try:
    time.sleep(2)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(17,GPIO.LOW)
    while True:
        # condition of authentication from both th fingerprint sensor module and the face recognition module
        if GPIO.input(21) and GPIO.input(24):
            GPIO.output(17,GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(17,GPIO.LOW)
            time.sleep(0.2)
            GPIO.output(17,GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(17,GPIO.LOW)    
            print("Hello user, the system is halted for 30 seconds")
            time.sleep(30)
            # conditon for the PIR motion sensor 
        if GPIO.input(18):
            print("Motion detected, clicking picture")
            import pygame.camera
            pygame.camera.init()
            cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
            cam.start()
            img = cam.get_image()
            import pygame.image
            pygame.image.save(img, "motion.jpg")
            cam.stop()
            print("Calling and sending an email")
            # Start a phone call
            call = client.calls.create(
            to="the number on which you want to call",
            from_="your number as alloted to you by the Twilio web service",
            url="http://demo.twilio.com/docs/voice.xml"
            )
            print("Firing Alarm")
            i=1
            print(call.sid)
            #smtp to send the photo clicked of the intruder to the user via mail
            email_user = 'User email address'
            email_send = 'receiver email address'
            subject =' Motion detected intruder alert- see the attached image'
            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['To'] = email_send
            msg['Subject'] = subject
            body = 'Intruder alert'
            msg.attach(MIMEText(body,'plain'))
            filename='motion.jpg'
            attachment =open(filename,'rb')
            print("Uploading photo and Prepairing to send email, This may take a moment...")
            part = MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',"attachment; filename= "+filename)
            msg.attach(part)
            text =msg.as_string()
            server =smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(email_user,'User email password')
            server.sendmail(email_user,email_send,text)
            server.quit
            print("Email sent")
            #firing alarm via the piezo buzzer
            while i<6:
                GPIO.output(17,GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(17,GPIO.LOW)
                time.sleep(0.2)
                GPIO.output(17,GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(17,GPIO.LOW)
                time.sleep(0.2)
                GPIO.output(17,GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(17,GPIO.LOW)
                time.sleep(0.2)
                GPIO.output(17,GPIO.LOW)
                time.sleep(0.2)
                i=i+1             
        else:
            print ("Motion not detected")
            time.sleep(4)
        time.sleep(0.2)

except:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
   
