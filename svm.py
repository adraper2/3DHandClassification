from sklearn import svm

class SVM(features, classes):
	def __init__(self, features, classes):
		self.features = features
		self.classes = classes
		self.clf = None

	def build(self, k_type='linear'):
		self.clf = svm.SVC(kernel=k_type).fit(self.features, self.classes)
		return clf

	def predict(self, new_features)
		if self.clf != None:
			return self.clf.predict(new_features)
		else:
			print("Error model not built yet")
			exit(-1)

def main():
	my_feats = []
	my_classes = []
	my_clf = SVM(my_feats, my_classes)
	my_clf.build(k_type='linear')


if __name__ == '__main__':
	main()