# Iris dataset

Iris data set is a well known example dataset introduced by Fisher in 1936 in his paper "The use of multiple measurements in taxonomic problems".
Iris data set was used as an example of machine learning/statistical learning method named linear discriminant analysis.

See [wikipedia page of iris data set](https://en.wikipedia.org/wiki/Iris_flower_data_set).


Iris data set can be downloaded from [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris)
You can also download it from course repository in the following formats.
 - [csv](iris.csv)
 - [arff](iris.arff)



## R usage

	# dataset load
	iris
	# assign it to data frame
	df = iris
	# see in spreadsheet format, works better in RStudio
	View(df)

## Python scikit learn usage

	from sklearn.datasets import load_iris

	df = load_iris()
	print(df.head())

## Weka usage

Iris data set is among the example datasets of weka distribution.
It can be found in data directory of weka installation.


## Others



## 

