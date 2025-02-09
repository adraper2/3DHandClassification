import os
import glob
import cv2
import features
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# yucky looking sklearn modules import
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support

# select whether you would like every x frame or just the ones from a specific list
skip_frames = 30
cap_frames = [60, 180]

# method to extract frames from the videos captured
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

# cycles through each file and then sends the video to frame_extraction
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
	
	# data processing
	#### uncomment this if data/frames contains no subfolders of poses and no frames for each pose ####
	#data_prep()

	#feature selection
	# try:
	# 	features_df = features.get_features_list()
	# 	np.save('features_df.npy', features_df)
	
	# 	labels = features.get_labels()
	# 	np.save('labels_df.npy', labels)
	
	# 	print("\nFeatures and labels saved")
	# except:
	# 	print("Something went wrong with feature selection")

	try:
		labels
		features
	except NameError:
		print("features do not exist right now, lets try loading them")
		try:
			features_df = np.load('features_df.npy') # make sure you run features.py first if this doesn't exist
			labels = np.load('labels_df.npy') # make sure you run features.py first if this doesn't exist
			print('Features df shape is: ', features_df.shape)
			print("Number of labels for model:", len(labels), "(Should match first column of features_df)\n\n")
		except:
			print("labels.npy and/or features_dy.npy do not exist.\nRun features.py first.")

	# get PCA for feature vectors
	ss = StandardScaler() # Centers and scales each feature using mean and variance	
	hands_standard = ss.fit_transform(features_df)
	pca = PCA(n_components=500)
	pca_hands = ss.fit_transform(hands_standard)

	# model training and prediction (withheld 50% of the data for testing)
	x_train, x_test, y_train, y_test = train_test_split(pca_hands,labels, test_size=.5, random_state=19)
	model = SVC(kernel='linear', probability=True, random_state=19)
	model.fit(x_train, y_train)

	predicted_labels = model.predict(x_test)

	# final model output
	accuracy = accuracy_score(y_test, predicted_labels)
	print('Model accuracy: ', accuracy)
	prf = precision_recall_fscore_support(y_test, predicted_labels, average = 'macro')
	print("Model precision:", prf[0])
	print("Model recall:", prf[1])
	print("Model F-score:", prf[2])

	df_confusion = pd.crosstab(y_test, predicted_labels, rownames=['Actual'], colnames=['Predicted'], margins=True)
	df_confusion_norm = df_confusion / df_confusion.sum(axis=1)
	print('\nConfusion Matrix')
	print(df_confusion)
	print('\nNormalized Confusion Matrix')
	print(df_confusion_norm)

	

if __name__ == '__main__':
	main()