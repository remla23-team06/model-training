from typing import Tuple
import pytest
from joblib import load
from numpy import int64
from numpy.typing import NDArray
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, accuracy_score

DataEntry = NDArray[int64]


@pytest.fixture
def trained_model():
    yield load("output/trained_model.joblib")


@pytest.fixture
def test_data():
    _, X_test, _, y_test = load("output/train_test_data.joblib")
    yield X_test, y_test


def test_evaluate_model(trained_model: Pipeline, test_data: Tuple[DataEntry, DataEntry]):
    X_test, y_test = test_data
    y_pred = trained_model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)
    assert isinstance(cm, np.ndarray)
    assert isinstance(accuracy, float)
