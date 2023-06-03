"""Tests for preprocess_data.py"""
import os
import re
from pathlib import Path

import pytest
from nltk import PorterStemmer

from src.preprocess_data import build_corpus, get_stop_words, read_data, write_corpus


@pytest.fixture
def dataset():
    yield read_data()


@pytest.fixture
def all_stopwords():
    yield get_stop_words()


def test_stopwords(all_stopwords):
    assert len(all_stopwords) > 0
    assert "not" not in all_stopwords


@pytest.fixture
def corpus(dataset, all_stopwords):
    yield build_corpus(
        ps=PorterStemmer(),
        df=dataset,
        stop_words=all_stopwords,
        no_of_lines=dataset.shape[0],  # Rows in dataset
    )


def test_build_corpus(corpus, dataset):
    assert (
        len(corpus) == dataset.shape[0]
    )  # Corpus has same number of elements as rows in dataset
    assert all([line.islower() or line == "" for line in corpus])
    assert all([not re.match("[^a-zA-Z]", line) for line in corpus])


def test_write_preprocess_data(dataset):
    filepath = Path("output/preprocessed_data.joblib")
    if filepath.is_file():
        os.remove(filepath)
    write_corpus(dataset, filepath=filepath)
    assert Path(filepath).is_file()
