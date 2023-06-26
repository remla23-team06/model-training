"""Tests for preprocess_data.py"""
import os
import re
from pathlib import Path

import pytest
from remlaverlib import Preprocessor

from src.preprocess_data import build_corpus, read_data, write_corpus, slice_data


@pytest.fixture
def dataset():
    """Read the dataset."""
    yield read_data()


@pytest.fixture
def corpus(dataset):
    """Build the corpus."""
    yield build_corpus(preprocessor=Preprocessor(), df=dataset)


def test_slice_data(dataset):
    sliced_data = slice_data(dataset)
    assert sliced_data.columns.tolist() == ["Review", "Liked"]


def test_build_corpus(corpus, dataset):
    """Test building the corpus."""
    assert (
            len(corpus) == dataset.shape[0]
    )  # Corpus has same number of elements as rows in dataset
    assert all(line.islower() or line == "" for line in corpus)
    assert all(not re.match("[^a-zA-Z]", line) for line in corpus)


def test_write_preprocess_data(dataset):
    """Test writing the preprocessed data to the output folder."""
    filepath = Path("output/preprocessed_data.joblib")
    if filepath.is_file():
        os.remove(filepath)
    write_corpus(dataset, filepath=filepath)
    assert Path(filepath).is_file()
