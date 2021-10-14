library("e1071")
df = iris
model = naiveBayes(Species~.,data=df)
predicted_values = predict(model,df[,1:4])


correctly_predicted = sum(predicted_values == df[,"Species"])
print(paste("Correctly predicted",correctly_predicted))

accuracy = correctly_predicted / nrow(df)
print(paste("accuracy",accuracy))
