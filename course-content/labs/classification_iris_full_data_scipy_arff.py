import numpy as np 
from scipy.io.arff import loadarff


from sklearn.naive_bayes import GaussianNB


data, meta = loadarff("../datasets/iris.arff")
columns = ["sepallength","sepalwidth","petallength","petalwidth"]

X_full = data[columns]
y_full = data["class"]

X_full = np.array(X_full.tolist())

clf = GaussianNB()
clf.fit(X_full,y_full)

y_pred = clf.predict(X_full)

accuracy = (y_full == y_pred).sum() / X_full.shape[0]

print("Accuracy is ", accuracy)
