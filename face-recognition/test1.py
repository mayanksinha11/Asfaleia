import cv2
import config
import face

print 'Loading training data...'
model = cv2.createEigenFaceRecognizer()
model.load(config.TRAINING_FILE)
print 'Training data loaded!'
# Initialize camera and box.
camera = config.get_camera()
while True:
        n=raw_input()
        print 'press c for taking photo'
        if n=='c':
                image = camera.read()
                image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
                result = face.detect_single(image)
                if result is None:
                        print 'Could not detect face'
                continue
        x, y, w, h = result
        crop = face.resize(face.crop(image, x, y, w, h))
        label, confidence = model.predict(crop)
        print 'Predicted {0} face with confidence {1} (lower is more confident).'.format(
					'POSITIVE' if label == config.POSITIVE_LABEL else 'NEGATIVE', 
					confidence)
        if label == config.POSITIVE_LABEL and confidence < config.POSITIVE_THRESHOLD:
                print 'Recognized face!'
        else:
                print 'Did not recognize face!'


                              


					
				
					
