# processes point clouds from SfM Colmap text files
# the goal of this file is to create a mask to segment images for training

import os
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def plot3D(x_ls, y_ls, z_ls):
	fig = plt.figure()
	ax = plt.axes(projection='3d')
	ax.scatter3D(x_ls, y_ls, z_ls)
	ax.view_init(60, 150)
	fig.savefig('temp.png')

def main():
	cloud_list = os.listdir('point_clouds')
	#for ls in cloud_list:
	ls = 'shaka_points3D.txt'
	with open('point_clouds/'+ls) as f:
		next(f)
		next(f)
		next(f)
		# id, (x,y,z), (r,g,b)
		df = pd.DataFrame([line.split(' ')[0:7] for line in f])
	df.columns = ['id', 'x', 'y', 'z', 'r', 'g', 'b']
	df = df.apply(pd.to_numeric)
	fig = plt.figure().gca(projection='3d')
	fig.view_init(60, 150)
	#fig.scatter(df['x'], df['y'], df['z'])
	#df=df[df['z'] > 3]
	print(df)
	fig.scatter(df['x'], df['y'])
	fig.set_xlabel('X')
	fig.set_ylabel('Y')
	#fig.set_zlabel('Z')
	print('got')
	plt.show()
	print('here')

		#file.close()

if __name__ == '__main__':
	main()