import joblib
import pytest
import numpy as np
from sklearn.naive_bayes import GaussianNB

from src.evaluate_model import evaluate_model
from src.preprocess_data import preprocess_pipeline
from src.train import read_corpus, read_data, train_model, transform_to_matrix_vector, create_train_test_split

THRESHOLD = 0.06


@pytest.fixture
def preprocess():
    """Processes the data."""
    preprocess_pipeline()


@pytest.fixture
def corpus():
    """Get the corpus."""
    return read_corpus()


@pytest.fixture
def dataset():
    """Get the dataset."""
    return read_data()


@pytest.fixture
def trained_model():
    """Get the trained model."""
    yield joblib.load("output/trained_model.joblib")


@pytest.fixture
def train_test_data():
    """Get the train test data."""
    yield joblib.load("output/train_test_data.joblib")


def test_nondeterminism_robustness(
        preprocess, trained_model, train_test_data, corpus, dataset
):
    """Test the robustness of the model against nondeterminism."""
    _, X_test, _, y_test = train_test_data
    _, original_score = evaluate_model(trained_model, test_data=(X_test, y_test))
    for seed in [1, 2]:
        model_variant, (_, X_test, _, y_test) = train_model(corpus, dataset, seed)
        _, accuracy_score = evaluate_model(model_variant, test_data=(X_test, y_test))
        assert abs(original_score - accuracy_score) <= THRESHOLD


def test_transform_to_matrix_vector(corpus, dataset):
    X_input, y_output = transform_to_matrix_vector(corpus, dataset)
    assert isinstance(X_input, np.ndarray)
    assert isinstance(y_output, np.ndarray)


def test_create_train_test_split(dataset):
    seed = 1
    X_input, y_output = dataset
    max_length = min(len(X_input), len(y_output))
    X_train, X_test, y_train, y_test = create_train_test_split(X_input[:max_length], y_output[:max_length], seed)
    assert isinstance(X_train, list)
    assert isinstance(X_test, list)
    assert isinstance(y_train, list)
    assert isinstance(y_test, list)


def test_train_model():
    corpus = read_corpus()
    dataset = read_data()
    dataset = dataset[["Review", "Liked"]]
    model, _ = train_model(corpus, dataset, 0)
    assert isinstance(model, GaussianNB)