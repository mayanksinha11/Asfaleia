# Asfaleia
An IOT based home security system.

It has three phases of working:
1- Authentication
2- Intrusion detection
3- Notifying the user

Auhtentication:
This is provided by the face recognition and fingerprint recognition.
The script Test2.py in the face recognition folder is used for the face recognition process. It is used to set an GPIO pin to high( when a familiar face is found)  which is read by the raspberry pi. 
The check_fingerprint.ino script is used to set an GPIO pin to high (when a registered fingerprint is found )which is read by the raspberry pi. 

Intsuion detection:
Motion1.py- script for the PIR sensor which clicks the image of the intruder and sends via an email to the user, and also makes a call on the user's cellphone.

irmqttsenddata.ino, irmqttdatareceivescript.py- Scripts to wirelessly send and receive sensor data between NODEMCU(IR breakbeam sensor attached to it) and the Raspberry Pi.

gasmqttrecievescript.py, gasmqttsend_data.ino- Scripts to wirelessly send and receive sensor data between NODEMCU(MQ6 gas leak sensor attached to it) and the Raspberry Pi.

Notifying the user:
1-by email- SMTP
2-by Call-  web service
