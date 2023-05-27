import pandas as pd

"""Test input"""


def test_input():
    dataset = pd.read_csv(
        "data/a1_RestaurantReviews_HistoricDump.tsv", delimiter="\t", quoting=3
    )
    assert dataset.shape != (0, 0)


if __name__ == "__main__":
    test_input()
    print("Everything passed")
