from joblib import load, dump
from sklearn.metrics import confusion_matrix, accuracy_score

# Load the classifier and data
[classifier, X_train, X_test, y_train, y_test] = load('output/trained_model_and_data.joblib')

# Model performance
y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
accuracy_score = accuracy_score(y_test, y_pred)

print(cm)
print(accuracy_score)
dump([cm, accuracy_score], 'output/evaluation.joblib')
