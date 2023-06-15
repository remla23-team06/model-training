import joblib
import pytest

from src.evaluate_model import evaluate_model
from src.preprocess_data import preprocess_pipeline
from src.train import read_corpus, read_data, train_model

THRESHOLD = 0.06


@pytest.fixture
def preprocess():
    preprocess_pipeline()


@pytest.fixture
def corpus():
    return read_corpus()


@pytest.fixture
def dataset():
    return read_data()


@pytest.fixture
def trained_model():
    yield joblib.load("output/trained_model.joblib")


@pytest.fixture
def train_test_data():
    yield joblib.load("output/train_test_data.joblib")


def test_nondeterminism_robustness(
    preprocess, trained_model, train_test_data, corpus, dataset
):
    _, X_test, _, y_test = train_test_data
    original_confusion_matrix, original_score = evaluate_model(
        trained_model, test_data=(X_test, y_test)
    )
    for seed in [1, 2]:
        model_variant, (X_train, X_test, y_train, y_test) = train_model(
            corpus, dataset, seed
        )
        _, accuracy_score = evaluate_model(
            model_variant, test_data=(X_test, y_test)
        )
        assert abs(original_score - accuracy_score) <= THRESHOLD
