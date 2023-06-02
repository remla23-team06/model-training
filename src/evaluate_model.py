"""Evaluate the model and save the results to a file."""
from typing import Tuple

from joblib import dump, load
from numpy import ndarray
from sklearn import metrics


# Model performance

def evaluate_model(model, test_data: Tuple[ndarray, ndarray]):
    X_test, y_test = test_data
    y_pred = model.predict(X_test)
    cm = metrics.confusion_matrix(y_test, y_pred)
    accuracy = metrics.accuracy_score(y_test, y_pred)
    return cm, accuracy

def evaluate_model_pipeline():
    # Load the classifier and data
    classifier = load("output/trained_model.joblib")
    [_, X_test, _, y_test] = load(
        "output/train_test_data.joblib"
    )
    confusion_matrix, accuracy_score = evaluate_model(classifier, test_data=(X_test, y_test))
    dump([confusion_matrix, accuracy_score], "output/evaluation.joblib")
    with open("output/accuracy_score.json", "w", encoding="utf8") as f:
        f.write('{"accuracy_score": ' + str(accuracy_score) + "}")


if __name__ == '__main__':
    evaluate_model_pipeline()