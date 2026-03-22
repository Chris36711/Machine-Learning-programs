from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
import pandas as pd

print("Decision Tree Program Started")

data = {
    "Hours":[1,2,3,4,5,6,7,8,2,3,4,5],
    "Sleep":[8,7,6,6,5,5,4,4,7,6,6,5],
    "Play":[1,1,0,0,0,1,1,1,1,0,0,1],
    "Pass":[0,0,0,1,1,1,1,1,0,0,1,1]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)

X = df[["Hours","Sleep","Play"]]
y = df["Pass"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.3,random_state=1
)

model = DecisionTreeClassifier(max_depth=3)

print("Training model")
model.fit(X_train,y_train)

pred = model.predict(X_test)

print("Predicted:",pred)
print("Actual:",y_test.values)

acc = accuracy_score(y_test,pred)
print("Accuracy:",acc)

cm = confusion_matrix(y_test,pred)
print("Confusion Matrix")
print(cm)

rep = classification_report(y_test,pred)
print("Report")
print(rep)

print("Program Completed")
 
