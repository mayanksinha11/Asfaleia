"""Raspberry Pi Face Recognition Treasure Box
Treasure Box Script
Copyright 2013 Tony DiCola 
"""
import cv2
import RPi.GPIO as GPIO
import config
import face
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
i=2;

if __name__ == '__main__':
	
	print 'Loading training data...'
	model = cv2.createEigenFaceRecognizer()
	model.load(config.TRAINING_FILE)
	print 'Training data loaded!'

	camera = config.get_camera()
	
	while True:
		
		if i==2:
			if i==1:
				
				
				print ''
			else:
				print 'Camera on, looking for face...'
			
				image = camera.read()
				
				image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
				
				result = face.detect_single(image)
				if result is None:
					print 'Could not detect single face!  Check the image in capture.pgm' \
						  ' to see what was captured and try again with only one face visible.'
					continue
				x, y, w, h = result
				
				crop = face.resize(face.crop(image, x, y, w, h))
				
				label, confidence = model.predict(crop)
				print 'Predicted {0} face with confidence {1} (lower is more confident).'.format(
					'POSITIVE' if label == config.POSITIVE_LABEL else 'NEGATIVE', 
					confidence)
				if label == config.POSITIVE_LABEL and confidence < config.POSITIVE_THRESHOLD:
					print 'Recognized face!'
					GPIO.output(24,GPIO.HIGH)
					time.sleep(10)
					GPIO.output(24,GPIO.LOW)
					break
					
				else:
					print 'Did not recognize face!'
