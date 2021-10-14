from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split


X_full, y_full = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X_full, y_full, test_size=0.33, random_state=42)

clf = GaussianNB()
clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)

accuracy = (y_test == y_pred).sum() / X_full.shape[0]

print("Accuracy is ", accuracy)
