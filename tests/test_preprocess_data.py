"""Tests for preprocess_data.py"""
import re

import pytest
from nltk import PorterStemmer

from src.preprocess_data import read_data as preprocess_read_data, get_stop_words, build_corpus


def test_read_data():
    preprocess_read_data()


@pytest.fixture
def dataset():
    yield preprocess_read_data()


def test_used_cols(dataset):
    assert dataset.columns.tolist() == ['Review', 'Liked']


def test_dtypes(dataset):
    assert dataset.dtypes.to_dict() == {'Review': 'string', 'Liked': 'bool'}


def test_not_empty(dataset):
    assert not dataset.empty and dataset.shape != (0, 0)


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
        no_of_lines=dataset.shape[0]  # Rows in dataset
    )


def test_build_corpus(corpus, dataset):
    assert len(corpus) == dataset.shape[0]  # Corpus has same number of elements as rows in dataset
    assert all([line.islower() or line == '' for line in corpus])
    assert all([not re.match("[^a-zA-Z]", line) for line in corpus])
