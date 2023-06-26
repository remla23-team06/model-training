import os
import random
import time
from typing import Tuple

import numpy as np
import psutil
import pytest
from joblib import load
from numpy import int64
from numpy.typing import NDArray
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.pipeline import Pipeline

DataEntry = NDArray[int64]


@pytest.fixture
def trained_model():
    """Trained model."""
    yield load("output/trained_model.joblib")


@pytest.fixture
def test_data():
    """Test data."""
    _, X_test, _, y_test = load("output/train_test_data.joblib")
    yield X_test, y_test


def evaluate_model(trained_model: Pipeline, test_data: Tuple[DataEntry, DataEntry]):
    """Evaluate the model."""
    X_test, y_test = test_data
    y_pred = trained_model.predict(X_test)
    c_matrix = confusion_matrix(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)
    return c_matrix, accuracy


def test_evaluate_model(
    trained_model: Pipeline, test_data: Tuple[DataEntry, DataEntry]
):
    """Test the evaluate_model function."""
    c_matrix, accuracy = evaluate_model(trained_model, test_data)
    assert isinstance(c_matrix, np.ndarray)
    assert isinstance(accuracy, float)


def test_evaluate_model_usage(
    trained_model, test_data: Tuple[DataEntry, DataEntry]
) -> None:
    """Test the evaluate_model_usage function."""
    # Load the classifier and data
    test_model_latency(trained_model, test_data)

    # Resource Utilization Test
    memory_usage = psutil.Process(os.getpid()).memory_info().rss
    cpu_usage = psutil.cpu_percent()
    print("Memory Usage:", memory_usage)
    print("CPU Usage:", cpu_usage)
    assert memory_usage > 0, "Memory usage should be greater than zero."
    assert cpu_usage >= 0, "CPU usage should be greater than or equal to zero."
    assert memory_usage < 2000000000, "Memory usage should be less than 2GB"
    assert cpu_usage <= 85, "CPU usage should be less than 85."


def model_latency(trained_model: Pipeline, test_data: Tuple[DataEntry, DataEntry]):
    """Measure the model latency."""
    X_test, _ = test_data

    # Model Latency Test
    num_iterations = 100
    total_latency = 0.0

    num_pairs = 10
    range_start = 1
    range_end = len(X_test)

    random_pairs = [
        [random.randint(range_start, range_end), random.randint(range_start, range_end)]
        for _ in range(num_pairs)
    ]
    random_pairs = [[x, y] if x < y else [y, x] for x, y in random_pairs]

    for _ in range(num_iterations):
        for start, end in random_pairs:
            start_time = time.time()
            _ = trained_model.predict(X_test[start:end])
            end_time = time.time()
            latency = end_time - start_time
            total_latency += latency

    return total_latency / (num_iterations * num_pairs)


def test_model_latency(trained_model: Pipeline, test_data: Tuple[DataEntry, DataEntry]):
    """Test the model latency."""
    average_latency = model_latency(trained_model, test_data)
    print("Average Model Latency:", average_latency)
    assert average_latency > 0, "Average model latency should be greater than zero."
    assert average_latency < 0.5, "Average model should be less than 0.5."
