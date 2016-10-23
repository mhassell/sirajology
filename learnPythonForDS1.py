from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import numpy as np

# height, weight, shoe size
X = np.array([[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],
     [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40],
     [159, 55, 37], [171, 75, 42], [181, 85, 43]])

# target data
Y = ['male', 'female', 'female', 'female', 'male', 'male', 
     'male', 'female', 'male', 'female', 'male']

# make a decision tree
classifier = tree.DecisionTreeClassifier()

# train it
classifier.fit(X,Y)

# now predict on a new data point
print 'Tree prediction: %s' % classifier.predict(np.array([190, 70, 42]))

##### now try with KNN #####
neigh3 = KNeighborsClassifier(n_neighbors=3)  # this seems like it might be a lot of regularization for such a small data set
neigh3.fit(X, Y)

print '3-NN prediction: %s' % neigh3.predict(np.array([190, 70, 42])) 

# let's try with 1-NN
neigh1 = KNeighborsClassifier(n_neighbors=1)  # this seems like it might be a lot of regularization for such a small data set
neigh1.fit(X, Y)

print '1-NN prediction: %s' % neigh1.predict(np.array([190, 70, 42]))

##### Also try with SVC #####

svclass = SVC()
svclass.fit(X,Y)

print 'SVC prediction: %s' % svclass.predict(np.array([190, 70, 42]))

##### Finally, try a neural network #####

from sklearn.neural_network import MLPClassifier

neural = MLPClassifier()
neural.fit(X,Y)

print 'Neural net prediction: %s' % neural.predict(np.array([190, 70, 42]))
