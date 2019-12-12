import os
import glob
import cv2
import sklearn

skip_frames = 30
cap_frames = [60, 180]

def frame_extraction(video):
	if video.endswith('.MOV'):
		cap = cv2.VideoCapture('data/'+video)
		
		pose = video[9:video.find('.')-1]
		if pose[-1:].isdigit():
			pose = video[9:video.find('.')-2]
		print("current pose:", pose)
		try:
			os.mkdir("data/frames/"+pose)
		except:
			print("File already exists")
		fr_count = 0
		ret = 1

		while ret:
			ret,frame = cap.read()
			#if fr_count % skip_frames == 0:
			if fr_count in cap_frames:
				cv2.imwrite("data/frames/"+pose+"/"+video[:-4]+"_frame%d.png" % fr_count, frame)
			fr_count += 1
			if cv2.waitKey(10) & 0xFF == ord('q'):
				break

		cap.release()
	#cv2.destroyAllWindows()

def data_prep(pose=None):
	video_f = os.listdir('data')
	video_f.sort()
	for vid in video_f:
		if pose:
			if pose in vid:
				frame_extraction(vid)
		else:
			frame_extraction(vid)


def main():
	data_prep()


	#x_train, x_test, y_train, y_test = train_test_split(pca_hands,y, test_size=.4, random_state=1997)

	#svm = sklearn.SVC(kernel='linear', probability=True, random_state=1997)

	#svm.fit(y_train, y_train)

	#predicted_labels = svm.predict(x_test)

	#accuracy = accuracy_score(y_test, predicted_labels)
	#print('Accuracy: ', accuracy)
			

	# model = svm.SVM(my_feats, my_classes)

if __name__ == '__main__':
	main()