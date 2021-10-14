
# Simple classification example on iris dataset using R

1. [install R and RStudio](../installation-r-and-r-studio-r-tools.md) on your computer

2. Read [iris dataset](iris.md) page.


3. install e1071 package in R

	install.packages("e1071")


4. run following R file in the RStudio

[classification_iris_full_data.R](classification_iris_full_data.R)

5. In our R codes, we will follow the same approach always.
Our classification codes will call the function and give which column should be predicted.
Here we are trying to predict Species.
Using data argument we set our data set.

	model = naiveBayes(Species~.,data=df)


For prediction, we use predict function and give our model and test data.

	predict(model,data)

In this file, we use following line, since only first 4 columns contains our X values. Our target is 5th column; therefore, we exclude it from our data frame.

	predict(model,df[,1:4])



5. run following R file in the RStudio

[classification_iris_train_test_split.R](classification_iris_train_test_split.R)

Since R do not have formal train test split function.
We use sample function of R to sample rows from R data frame.
Using negative indexing we get test data as in the below code.

	test_data = df[-train_rows,]

Other differences in our code to use train and test data in our model and predict codes.
Since we have to use train and test data in our calls.

	model = naiveBayes(Species~.,data=train_data)
	predicted_values = predict(model,test_data[,1:4])


	correctly_predicted = sum(predicted_values == test_data[,"Species"])
