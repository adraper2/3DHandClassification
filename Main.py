import os
import glob
import svm
import cv2

skip_frames = 1

def frame_extraction(video):
	if video.endswith('.MOV'):
		cap = cv2.VideoCapture('data/'+video)
		
		pose = video[9:video.find('.')-2]
		print("current pose:", pose)
		try:
			os.mkdir("data/"+pose)
		except:
			print("File already exists")
		fr_count = 0
		ret = 1

		while ret:
			ret,frame = cap.read()
			if fr_count % skip_frames == 0:
				cv2.imwrite("data/"+pose+"/"+video[:-4]+"_frame%d.png" % fr_count, frame)
			fr_count += 1
			if cv2.waitKey(10) & 0xFF == ord('q'):
				break

		cap.release()
	#cv2.destroyAllWindows()

def data_prep(pose=None):
	for vid in os.listdir('data'):
		if pose:
			if pose in vid:
				frame_extraction(vid)
		else:
			frame_extraction(vid)


def main():
	data_prep('fist')
			

	# model = svm.SVM(my_feats, my_classes)

if __name__ == '__main__':
	main()