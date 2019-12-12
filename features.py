import os
import skimage
import sklearn
from skimage.color import rgb2grey
from skimage.feature import hog
import numpy as np
from PIL import Image


def features(image):
	features = image.flatten()
	grey_image = rgb2grey(image)
	hog_features = hog(grey_image, block_norm='L2-Hys', pixels_per_cell=(16, 16))
	features = np.hstack(hog_features)
	return features

def get_labels():
	labels = []

	poses = os.listdir('data/frames')
	poses.sort()
	poses = [x for x in poses if '.' not in x]

	for pose in poses:
			images_f = os.listdir('data/frames/'+pose)
			images_f.sort()
			for img_f in images_f:
				labels.append(pose)
	print("got labels")
	return labels

def get_features_list():
	features_df = []

	poses = os.listdir('data/frames')
	poses.sort()
	poses = [x for x in poses if '.' not in x]

	for pose in poses:
		images_f = os.listdir('data/frames/'+pose)
		images_f.sort() 
		images_f = [x for x in images_f if '.DS_Store' not in x]
		for img_f in images_f:
			image = np.array(Image.open('data/frames/'+pose +'/'+img_f))
			image_features = features(image)
			features_df.append(image_features)

	features_df = np.array(features_df)
	print("got features")
	return features_df


def main():

	features_df = get_features_list()
	labels = get_labels()
	#print(labels)

	print('got this far')

	#ss = preprocessing.StandardScalar()

	#hands_standard = ss.fit_transform(feature_df)
	#pca = decomposition.PCA(n_components=500)

	#pca_hands = ss.fit_transform(hands_standard)

	



if __name__ == '__main__':
	main()