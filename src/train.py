"""Train the model and export it to later use in prediction."""
from pathlib import Path
from typing import Any, List, Tuple, Union

import numpy as np
import pandas as pd
from joblib import dump, load
from numpy.typing import NDArray
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline

DataEntry = NDArray[np.int64]


# load the preprocessed data
def read_corpus(filepath: Union[str, Path] = "output/preprocessed_data.joblib") -> Any:
    return load(filepath)


def read_data(filepath: Union[str, Path] = "output/dataset.csv") -> pd.DataFrame:
    return pd.read_csv(filepath, dtype={"text": "string", "score": "bool"})


def transform_to_matrix_vector(
    input_data: List[str], output_data: pd.DataFrame
) -> Tuple[DataEntry, DataEntry]:
    # Data transformation
    cv = CountVectorizer(max_features=1420)
    transformed_input = cv.fit_transform(input_data).toarray()
    transformed_output = output_data.iloc[:, -1].values
    return transformed_input, transformed_output


def create_train_test_split(X_input: DataEntry, y_output: DataEntry, seed: int) -> Any:
    # Dividing dataset into training and test set
    return train_test_split(X_input, y_output, test_size=0.20, random_state=seed)


def save_model(
    model: Pipeline, filepath: Union[str, Path] = "output/trained_model.joblib"
) -> None:
    dump(model, filepath)


def save_data(
    data: List[DataEntry], filepath: Union[str, Path] = "output/train_test_data.joblib"
) -> None:
    dump(data, filepath)


def train_model(
    local_corpus: List[str], local_dataset: pd.DataFrame, seed: int
) -> Tuple[GaussianNB, List[DataEntry]]:
    X, y = transform_to_matrix_vector(local_corpus, local_dataset)
    X_train, X_test, y_train, y_test = create_train_test_split(X, y, seed)

    # Model fitting (Naive Bayes)
    classifier = GaussianNB()
    classifier.fit(X_train, y_train)

    return classifier, [X_train, X_test, y_train, y_test]


def train_pipeline() -> None:
    corpus: List[str] = read_corpus()
    dataset: pd.DataFrame = read_data()
    dataset = dataset[["Review", "Liked"]]
    model, data = train_model(corpus, dataset, 0)
    # Exporting NB Classifier to later use in prediction
    save_model(model)
    save_data(data)


if __name__ == "__main__":
    train_pipeline()
