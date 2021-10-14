
# Simple classification example on iris dataset using Python scikit-learn

1. [install python and conda](../installation-python-conda.md) on your computer

2. Read [iris dataset](iris.md) page.


3. run following python file in the command line

[classification_iris_full_data.py](classification_iris_full_data.py)


4. All of the classifier will work same in scikit-learn.

	1. create our classifier here in this example s[klearn.naive_bayes.GaussianNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html) class.
	2. use fit method and send the training data
	3. use predict method to find predictions

5. run following python file in the command line

[classification_iris_train_test_split.py](classification_iris_train_test_split.py)


6. Different from the first python run, we are splitting our dataset to train and test in this example.
We should never report the results on training data set as in our [first example](classification_iris_full_data.py).
We should always have a separate test dataset.

