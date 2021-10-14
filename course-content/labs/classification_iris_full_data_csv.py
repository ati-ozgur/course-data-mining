from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
import pandas as pd


df = pd.read_csv("../datasets/iris.csv")
#print(df.head())
columns = ["sepallength","sepalwidth","petallength","petalwidth"]
X_full = df[columns].values
y_full = df["class"].values


clf = GaussianNB()
clf.fit(X_full,y_full)

y_pred = clf.predict(X_full)

accuracy = (y_full == y_pred).sum() / X_full.shape[0]

print("Accuracy is ", accuracy)
