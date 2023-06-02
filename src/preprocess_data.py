"""Data Preprocessing"""
import os
import re
from typing import List

import nltk
import pandas as pd
from joblib import dump
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


# Load the data from the file

def read_data() -> pd.DataFrame:
    return pd.read_csv("output/dataset.csv",
                       dtype={'Review': 'string', 'Liked': 'bool'})


def slice_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Select columns from dataset
    """
    return df[['Review', 'Liked']]


def get_stop_words() -> List[str]:
    nltk.download("stopwords")
    retrieved_stopwords = stopwords.words("english")
    retrieved_stopwords.remove("not")
    return retrieved_stopwords


def build_corpus(
        ps: PorterStemmer,
        df: pd.DataFrame,
                 stop_words: List[str],
                 no_of_lines: int) -> List[str]:
    corpus = []
    for i in range(no_of_lines):
        review_str = re.sub("[^a-zA-Z]", " ", df["Review"][i])
        review_str = review_str.lower()
        review_list = review_str.split()
        review_list = [
            ps.stem(word) for word in review_list if word not in set(stop_words)
        ]
        review_list = " ".join(review_list)
        corpus.append(review_list)
    return corpus


def write_corpus(corpus: List[str]) -> None:
    dump(corpus, "output/preprocessed_data.joblib")


if __name__ == '__main__':
    all_stopwords = get_stop_words()
    dataset = read_data()
    dataset = slice_data(dataset)
    word_corpus = build_corpus(
        ps=PorterStemmer(),
        df=dataset,
        stop_words=all_stopwords,
        no_of_lines=dataset.shape[0])
    print(len(word_corpus))
    write_corpus(word_corpus)
