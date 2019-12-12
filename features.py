# this file produces the feature vectors and labels for the model

import os
import skimage
import sklearn
from skimage.color import rgb2grey
from skimage.feature import hog
import numpy as np
from PIL import Image

# concats hog features ontop of a flattened RGB image vector 
def features(image):
	print('flattening image')
	features = image.flatten()
	print('converting to gray scale')
	grey_image = rgb2grey(image)
	print('getting hog features')
	hog_features = hog(grey_image, block_norm='L2-Hys', pixels_per_cell=(128, 128)) # may need to mess with cell size
	features = np.hstack(hog_features)
	return features

# creates labels from image file names
def get_labels():
	labels = []

	poses = os.listdir('data/frames')
	poses.sort()
	poses = [x for x in poses if '.' not in x]

	print(poses)

	for pose in poses:
			images_f = os.listdir('data/frames/'+pose)
			images_f.sort()
			images_f = [x for x in images_f if '.DS_Store' not in x]
			for img_f in images_f:
				labels.append(pose)
	print("got",len(labels), "labels")
	return labels

def get_features_list():
	image_size = 1280, 720
	features_df = []

	poses = os.listdir('data/frames')
	poses.sort()
	poses = [x for x in poses if '.' not in x]

	for pose in poses:
		images_f = os.listdir('data/frames/'+pose)
		images_f.sort() 
		images_f = [x for x in images_f if '.DS_Store' not in x]
		for img_f in images_f:
			print('opening image')
			image = Image.open('data/frames/'+pose +'/'+img_f)
			print('resizing image')
			image = image.resize(image_size, Image.ANTIALIAS)
			print('converting to np array')
			image = np.array(image)
			print('calculating features')
			image_features = features(image)
			features_df.append(image_features)
			print('got', len(image_features), 'features')

	features_df = np.array(features_df)
	print("got feature shape of", features_df.shape)
	return features_df


def main():

	features_df = get_features_list()
	np.save('features_df.npy', features_df)

	labels = get_labels()
	np.save('labels_df.npy', labels)

	print("\nFeatures and labels saved")

if __name__ == '__main__':
	main()