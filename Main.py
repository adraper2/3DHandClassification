import os
import svm

def frame_extraction(video):
	print('codey code code')

def main():
	vids = os.listdir('data')
	for vid in vids:
		success,image = cv2.VideoCapture('data/'+vid).read()
		fr_count = 0
		success = True
		while success:
			success,image = vidcap.read()
			if count % 5 == 0:
				cv2.imwrite("data/frames/frame%d.png" % count, image)
			fr_count += 1
	# model = svm.SVM(my_feats, my_classes)

if __name__ == '__main__':
	main()