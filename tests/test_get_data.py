"""Tests for get_data.py"""
import os
from pathlib import Path

import pytest

from src.get_data import read_data, write_data


@pytest.fixture
def dataset():
    yield read_data()


def test_write_data(dataset):
    filepath = Path("output/dataset.csv")
    if filepath.is_file():
        os.remove(filepath)
    write_data(dataset, output_path=filepath)
    assert Path(filepath).is_file()
