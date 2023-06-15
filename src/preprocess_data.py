"""Data Preprocessing"""
import os
import re
from pathlib import Path
from typing import List, Union

import nltk
import pandas as pd
from joblib import dump
from nltk.corpus import stopwords
from remlaverlib import Preprocessor


# Load the data from the file


def read_data() -> pd.DataFrame:
    return pd.read_csv(
        "output/dataset.csv", dtype={"Review": "string", "Liked": "bool"}
    )


def slice_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Select columns from dataset
    """
    return df[["Review", "Liked"]]


def get_stop_words() -> List[str]:
    nltk.download("stopwords")
    retrieved_stopwords: List[str] = stopwords.words("english")
    retrieved_stopwords.remove("not")
    return retrieved_stopwords


def build_corpus(preprocessor: Preprocessor, df: pd.DataFrame) -> List[str]:
    corpus = []
    no_of_lines: int = df.shape[0]
    for i in range(no_of_lines):
        stemmed_review = preprocessor.process_input(df["Review"][i])
        corpus.append(stemmed_review)
    return corpus


def write_corpus(
        corpus: List[str], filepath: Union[str, Path] = "output/preprocessed_data.joblib"
) -> None:
    dump(corpus, filepath)


def preprocess_pipeline() -> None:
    preprocessor = Preprocessor()
    dataset = read_data()
    dataset = slice_data(dataset)
    word_corpus = build_corpus(
        preprocessor=preprocessor,
        df=dataset
    )
    print(len(word_corpus))
    write_corpus(word_corpus)


if __name__ == "__main__":
    preprocess_pipeline()
