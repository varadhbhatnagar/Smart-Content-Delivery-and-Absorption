import os
import cv2
import numpy as np
from keras.models import  model_from_json
from keras.preprocessing import image
import matplotlib.pyplot as plt
from imutils import face_utils

def ed(video_file):
	font = cv2.FONT_HERSHEY_SIMPLEX

	cascPath = "/home/shriya/hackathon2020_NEC/Smart-Content-Delivery-and-Absorption/SCAD/SCAD/haarcascade_files/haarcascade_frontalface_default.xml"
	eyePath = "/home/shriya/hackathon2020_NEC/Smart-Content-Delivery-and-Absorption/SCAD/SCAD/haarcascade_files/haarcascade_eye.xml"

	faceCascade = cv2.CascadeClassifier(cascPath)
	eyeCascade = cv2.CascadeClassifier(eyePath)
	#=======================================================

	#load model
	print(os.system('pwd'))
	model=model_from_json(open("/home/shriya/hackathon2020_NEC/Smart-Content-Delivery-and-Absorption/SCAD/SCAD/fer.json","r").read())
	#model = 'models/_mini_XCEPTION.102-0.66.hdf5'
	#load weights
	model.load_weights('/home/shriya/hackathon2020_NEC/Smart-Content-Delivery-and-Absorption/SCAD/SCAD/fer.h5')
	frame_count=0
	print("frame count:{}".format(frame_count))
	emotion_score_dict={"neutral":90,"fear":80,"sad":70,"surprise":50,"disgust":40,"angry":30,"happy":10}
	cumulative_score=0
	scores=[]
	video_capture = cv2.VideoCapture(video_file)

	while frame_count<1000 :
		# Capture frame-by-frame
		ret, frame = video_capture.read()
		frame_count=frame_count+1
		print("frame_count:{}".format(frame_count))
		frame_score=0
		if not ret:
			continue
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5,	minSize=(30, 30),flags=cv2.CASCADE_SCALE_IMAGE)
		for (x, y, w, h) in faces:
			cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 1)
			roi_gray = gray[y:y+w, x:x+h]
			roi_color = frame[y:y+h, x:x+w]
			roi_gray=cv2.resize(roi_gray,(48,48))
			img_pixels=image.img_to_array(roi_gray)
			img_pixels=np.expand_dims(img_pixels,axis=0)
			img_pixels/=255

			predictions=model.predict(img_pixels)

			#find max indexed array
			max_index=np.argmax(predictions[0])
			emotions=('angry','disgust','fear','happy','sad','surprise','neutral')

			predicted_emotion=emotions[max_index]
			frame_score=frame_score+emotion_score_dict[predicted_emotion]
			print(predicted_emotion)
			print("emotion_score:{}".format(emotion_score_dict[predicted_emotion]))
			print("frame_score:{}".format(frame_score))
			print("Number of faces:{}".format(len(faces)))
			cv2.putText(frame,predicted_emotion,(int(x),int(y)),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
			resized_img=cv2.resize(frame,(1000,700))

			cv2.putText(frame,'Number of Faces : ' + str(len(faces)),(40, 40), font, 1,(255,0,0),2)
			# Display the resulting frame
			cv2.imshow('Video', resized_img)
		if(len(faces)!=0):
			average_frame_score=frame_score/(len(faces))
		else:
			average_frame_score=frame_score
		print("average_frame_score:{}".format(average_frame_score))
		scores.append(average_frame_score)
		print("scores:{}".format(scores))
		if cv2.waitKey(1) & 0xFF == ord('q'):
			cumulative_score=sum(scores)/frame_count
			print("cumulative_score:{}".format(cumulative_score))
			break
	cumulative_score=sum(scores)/frame_count
	print("cumulative_score:{}".format(cumulative_score))
	video_capture.release()
	cv2.destroyAllWindows()
	return cumulative_score
