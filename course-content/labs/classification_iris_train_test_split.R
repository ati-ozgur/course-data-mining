library("e1071")
df = iris
train_test_split_percentage = 0.66

train_rows = sample(nrow(df), nrow(df)*train_test_split_percentage)

train_data = df[train_rows,]
test_data = df[-train_rows,]

model = naiveBayes(Species~.,data=train_data)
predicted_values = predict(model,test_data[,1:4])


correctly_predicted = sum(predicted_values == test_data[,"Species"])
print(paste("Correctly predicted",correctly_predicted))

accuracy = correctly_predicted / nrow(test_data)
print(paste("accuracy",accuracy))
