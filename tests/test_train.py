import joblib
import pytest

from src.evaluate_model import evaluate_model
from src.preprocess_data import preprocess_pipeline
from src.train import read_corpus, read_data, train_model

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


def test_nondeterminism_robustness(trained_model, train_test_data, corpus, dataset):
    """Test the robustness of the model against nondeterminism."""
    _, X_test, _, y_test = train_test_data
    _, original_score = evaluate_model(trained_model, test_data=(X_test, y_test))
    for seed in [1, 2]:
        model_variant, (_, X_test, _, y_test) = train_model(corpus, dataset, seed)
        _, accuracy_score = evaluate_model(model_variant, test_data=(X_test, y_test))
        assert abs(original_score - accuracy_score) <= THRESHOLD
