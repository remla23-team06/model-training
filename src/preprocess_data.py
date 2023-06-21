"""Data Preprocessing"""
from pathlib import Path
from typing import Union

import pandas as pd
from joblib import dump
from remlaverlib import Preprocessor

# Load the data from the file


def read_data() -> pd.DataFrame:
    """Load data from dataset and select columns and corresponding datatypes"""
    return pd.read_csv(
        "output/dataset.csv", dtype={"Review": "string", "Liked": "bool"}
    )


def slice_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Select columns from dataset
    """
    return df[["Review", "Liked"]]


def build_corpus(preprocessor: Preprocessor, df: pd.DataFrame) -> list[str]:
    """
    Stem each review and add it to the corpus
    :param preprocessor: preprocessor from remlaverlib
    :param df: the dataframe containing input data
    :return list[str]: the corpus
    """
    corpus = []
    no_of_lines: int = df.shape[0]
    for i in range(no_of_lines):
        stemmed_review = preprocessor.process_input(df["Review"][i])
        corpus.append(stemmed_review)
    return corpus


def write_corpus(
    corpus: list[str], filepath: Union[str, Path] = "output/preprocessed_data.joblib"
) -> None:
    """Write corpus to joblib file"""
    dump(corpus, filepath)


def preprocess_pipeline() -> None:
    """The preprocessing pipeline that DVC executes for the preprocess stage."""
    preprocessor = Preprocessor()
    dataset = read_data()
    dataset = slice_data(dataset)
    word_corpus = build_corpus(preprocessor=preprocessor, df=dataset)
    print(len(word_corpus))
    write_corpus(word_corpus)


if __name__ == "__main__":
    preprocess_pipeline()
