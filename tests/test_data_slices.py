from typing import Dict, Tuple

import pytest
from joblib import load
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.pipeline import Pipeline

from src import get_data
from src.evaluate_model import DataEntry
from src.train import read_data, transform_to_matrix_vector


@pytest.fixture
def trained_model():
    """Fixture that provides the trained model."""
    yield load("output/trained_model.joblib")


@pytest.fixture
def test_data():
    """Fixture that provides the test data."""
    _, X_test, _, y_test = load("output/train_test_data.joblib")
    yield X_test, y_test


@pytest.fixture
def corpus_words():
    """Fixture that provides the data."""
    yield load("output/preprocessed_data.joblib")


@pytest.fixture
def corpus():
    """Fixture that provides the corpus data."""
    corpus = load("output/preprocessed_data.joblib")
    data = read_data()
    X, _ = transform_to_matrix_vector(corpus, data)
    yield X


@pytest.fixture
def criterion_fixture(request):
    """Fixture that defines the data slice criterion."""
    criteria = [
        lambda x: len(x) < 5,
        lambda x: len(x) < 15,
        lambda x: len(x) > 5,
        lambda x: len(x) > 10,
        lambda x: len(x) > 25,
    ]
    return criteria[request.param]


@pytest.fixture
def get_data_dataset():
    """Get the dataset."""
    yield get_data.read_data()


def evaluate_model(
    model: Pipeline,
    test_data: Tuple[DataEntry, DataEntry],
    criterion,
    corpus,
    corpus_words,
) -> Tuple[DataEntry, float, Dict[str, float]]:
    """
    Evaluate the model's performance on the test data.

    Args:
        model: The trained model.
        test_data: Tuple containing the test input data (X_test) and the test target labels (y_test).
        criterion: The criterion for dividing the data into subpopulations.
        corpus: The corpus represented as a matrix
        corpus_words: The corpus represented as unprocessed sentences

    Returns:
        A tuple containing the confusion matrix, overall accuracy, and accuracy scores for subpopulations.

    """
    X_test, y_test = test_data
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    def find_row_in_matrix(matrix, row):
        for i, res in enumerate(matrix):
            if all(x == y for x, y in zip(res, row)):
                return i
        return -1

    # Get the mappings from the corpus to the X_train filtered by criterion
    subpopulation_indices = [
        find_row_in_matrix(X_test, element)
        for index, element in enumerate(corpus)
        if find_row_in_matrix(X_test, element) != -1 and criterion(corpus_words[index])
    ]

    # Calculate accuracy score for the subpopulation based on the provided criterion
    sub_accuracy = accuracy_score(
        y_test[subpopulation_indices], y_pred[subpopulation_indices]
    )

    return confusion_matrix(y_test, y_pred), accuracy, {"Subpopulation": sub_accuracy}


@pytest.mark.parametrize(
    "criterion_fixture", [0, 1, 2, 3, 4], indirect=["criterion_fixture"]
)
def test_evaluate_model(
    trained_model, test_data, criterion_fixture, corpus, corpus_words
):
    """
    Test the evaluate_model function.

    Args:
        trained_model: The trained model provided by the fixture.
        test_data: The test data provided by the fixture.
        criterion_fixture: The criterion for dividing the data into subpopulations.

    """
    X_test, y_test = test_data
    _, accuracy, accuracy_scores = evaluate_model(
        trained_model,
        test_data=(X_test, y_test),
        criterion=criterion_fixture,
        corpus=corpus,
        corpus_words=corpus_words,
    )

    # Assertions for overall accuracy
    assert isinstance(accuracy, float)
    assert 0.65 <= accuracy <= 1.0

    # Assertions for accuracy score of the subpopulation
    assert isinstance(accuracy_scores, dict)
    assert "Subpopulation" in accuracy_scores
    sub_accuracy = accuracy_scores["Subpopulation"]
    assert isinstance(sub_accuracy, float)
    assert 0.6 <= sub_accuracy <= 1.0
