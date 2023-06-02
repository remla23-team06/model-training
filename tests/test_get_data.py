"""Tests for get_data.py"""
import os
from pathlib import Path

import pytest

from src.get_data import read_data, write_data


def test_read_data():
    read_data()


@pytest.fixture
def dataset():
    yield read_data()


def test_used_cols(dataset):
    assert dataset.columns.tolist() == ['Review', 'Liked']


def test_dtypes(dataset):
    assert dataset.dtypes.to_dict() == {'Review': 'string', 'Liked': 'bool'}


def test_not_empty(dataset):
    assert not dataset.empty and dataset.shape != (0, 0)


def test_write_data(dataset):
    filepath = Path("output/dataset.csv")
    if filepath.is_file():
        os.remove(filepath)
    write_data(dataset, output_path=filepath)
    assert Path(filepath).is_file()
