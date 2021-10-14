from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB

X_full, y_full = load_iris(return_X_y=True)


clf = GaussianNB()
clf.fit(X_full,y_full)

y_pred = clf.predict(X_full)

accuracy = (y_full == y_pred).sum() / X_full.shape[0]

print("Accuracy is ", accuracy)
