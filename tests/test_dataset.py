import pytest
from pytest_lazyfixture import lazy_fixture

from src import get_data, preprocess_data


@pytest.fixture
def get_data_dataset():
    yield get_data.read_data()


@pytest.fixture
def preprocess_data_dataset():
    yield preprocess_data.read_data()


dataset_fixture = "dataset", [
    lazy_fixture("get_data_dataset"),
    lazy_fixture("preprocess_data_dataset"),
]


@pytest.mark.parametrize(*dataset_fixture)
def test_used_cols(dataset):
    assert dataset.columns.tolist() == ["Review", "Liked"]


@pytest.mark.parametrize(*dataset_fixture)
def test_dtypes(dataset):
    assert dataset.dtypes.to_dict() == {"Review": "string", "Liked": "bool"}


@pytest.mark.parametrize(*dataset_fixture)
def test_not_empty(dataset):
    assert not dataset.empty and dataset.shape != (0, 0)
