import joblib
import pytest

from src.evaluate_model import evaluate_model
from src.train import train_model, read_data, read_corpus
from src.preprocess_data import preprocess_pipeline

THRESHOLD = 0.03


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
    yield joblib.load('output/trained_model.joblib')


@pytest.fixture
def train_test_data():
    yield joblib.load('output/train_test_data.joblib')


def test_nondeterminism_robustness(preprocess, trained_model, train_test_data, corpus, dataset):
    X_train, X_test, y_train, y_test = train_test_data
    original_confusion_matrix, original_score = evaluate_model(trained_model,
                                                               test_data=(X_test, y_test))
    for seed in range(500):
        model_variant, (X_train, X_test, y_train, y_test) = train_model(corpus, dataset, seed)
        confusion_matrix, accuracy_score = evaluate_model(model_variant, test_data=(X_test, y_test))
        assert abs(original_score - accuracy_score) <= THRESHOLD