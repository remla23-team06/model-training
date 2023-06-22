"""Get data from the historic dump and save it to a file."""
from pathlib import Path
from typing import Union

import pandas as pd
import gdown

def get_data() -> None:
    """Retrieve data folder with data files from Google Drive"""
    # Reference: https://pypi.org/project/gdown/
    url = "https://drive.google.com/drive/folders/10tQq1dbW2F5b3rPy8EZi_ejAaq6IkIGG"
    gdown.download_folder(url, quiet=True, use_cookies=False)


def read_data() -> pd.DataFrame:
    """Importing dataset"""
    return pd.read_csv(
        "data/a1_RestaurantReviews_HistoricDump.tsv",
        delimiter="\t",
        quoting=3,
        dtype={"Review": "string", "Liked": "bool"},
    )


def slice_data(df: pd.DataFrame) -> pd.DataFrame:
    """Select columns from dataset"""
    return df[["Review", "Liked"]]


def write_data(
    df: pd.DataFrame, output_path: Union[str, Path] = "output/dataset.csv"
) -> None:
    """Save data in a file for later use"""
    df.to_csv(output_path, index=False)


def get_data_pipeline() -> None:
    """The pipeline that DVC will execute for the get_data stage."""
    get_data()
    dataset = read_data()
    print(dataset.dtypes.to_dict())
    dataset = slice_data(dataset)
    print(dataset)
    write_data(dataset)


if __name__ == "__main__":
    get_data_pipeline()
