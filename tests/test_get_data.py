"""Tests for get_data.py"""
import pandas as pd


def test_input() -> None:
    """Test that the input dataset is not empty"""
    dataset = pd.read_csv(
        "data/a1_RestaurantReviews_HistoricDump.tsv", delimiter="\t", quoting=3
    )
    assert dataset.shape != (0, 0)


if __name__ == "__main__":
    test_input()
    print("Everything passed")
