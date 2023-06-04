import pytest
from pytest_lazyfixture import lazy_fixture
import nltk
from nltk.corpus import wordnet
import requests
import random
import os

from src import preprocess_data, get_data


def submit_review(review_data: str, server_url: str):
    """
    Submits a review to the server for sentiment analysis.

    Args:
        review_data (str): The review text to be analyzed.

    Returns:
        int or None: The sentiment value of the review if the request is successful,
                     or None if an error occurs.

    Raises:
        requests.exceptions.RequestException: If an error occurs while sending the request.
    """
    payload = {
        "data": review_data
    }
    response = requests.post(server_url + "/predict", data=payload, timeout=1.5)
    if response.status_code == 200:
        response_data = response.json()
        sentiment = response_data.get('sentiment', 0)
        return sentiment == 1
    else:
        return None


# Generate a mutant by modifying random words in the input review
def generate_mutant(review, mutate_count):
    """
    Generates a mutant version of the input review by applying random mutations to a specified number of words.

    Parameters:
    review (str): The review text.
    mutate_count (int): The number of words to be mutated.

    Returns:
    str: The mutant review text.
    """
    words = review.split()

    if mutate_count > len(words):
        mutate_count = len(words)

    indices = random.sample(range(len(words)), mutate_count)
    mutated_words = words.copy()

    for idx in indices:
        word = words[idx]
        synonyms = []

        for synset in wordnet.synsets(word):
            for lemma in synset.lemmas():
                synonym = lemma.name()
                if synonym != word:
                    synonyms.append(synonym)

        if synonyms:
            mutated_words[idx] = random.choice(synonyms)

    mutant_review = ' '.join(mutated_words)
    return mutant_review


# Test the sentiment analysis model with original and mutant reviews
def get_assertion_model(review, liked, mutate_count, server_url):
    """
    Test the sentiment analysis model using mutamorphic testing.

    Parameters:
    review (str): The review text.
    liked (bool): The expected sentiment label (True for positive, False for negative).
    mutate_count (int): The number of words to be mutated.
    """
    original_sentiment = submit_review(review, server_url)
    mutant_review = generate_mutant(review, mutate_count)
    mutant_sentiment = submit_review(mutant_review, server_url)

    if original_sentiment != mutant_sentiment:
        pytest.skip("Mutation detected! From : {0}; To: {1}".format(review, mutant_review))


@pytest.fixture
def get_data_dataset():
    yield get_data.read_data()


@pytest.fixture
def preprocess_data_dataset():
    yield preprocess_data.read_data()


@pytest.fixture
def download_wordnet():
    nltk.download('wordnet')


@pytest.fixture
def mutate_words_count():
    return int(os.environ.get("MUTATE_COUNT", "1"))


@pytest.fixture
def model_service_url():
    return str(os.environ.get("MODEL_SERVICE_URL", "http://localhost:8000"))


dataset_fixture = "dataset", [
    lazy_fixture("get_data_dataset"),
    lazy_fixture("preprocess_data_dataset"),
]


@pytest.mark.usefixtures("download_wordnet")
@pytest.mark.parametrize(*dataset_fixture)
def test_sentiment_analysis(dataset, mutate_words_count, model_service_url):
    review_column = dataset["Review"]
    liked_column = dataset["Liked"]

    for review, liked in zip(review_column, liked_column):
        get_assertion_model(review, liked, mutate_words_count, model_service_url)


def pytest_addoption(parser):
    parser.addoption(
        "--mutate-count",
        action="store",
        default=1,
        help="Number of words to mutate in each review."
    )

# poetry run pytest -s tests/test_mutamorphic.py
