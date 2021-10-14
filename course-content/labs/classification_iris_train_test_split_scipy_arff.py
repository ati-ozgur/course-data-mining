from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from scipy.io.arff import loadarff


data, meta = loadarff("../datasets/iris.arff")
columns = ["sepallength","sepalwidth","petallength","petalwidth"]

X_full = data[columns]
y_full = data["class"]

X_train, X_test, y_train, y_test = train_test_split(X_full, y_full, test_size=0.33, random_state=42)

clf = GaussianNB()
clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)

accuracy = (y_test == y_pred).sum() / X_full.shape[0]

print("Accuracy is ", accuracy)
