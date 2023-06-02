"""Data Preprocessing"""
import os
import re

import nltk
import pandas as pd
from joblib import dump
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Load the data from the file
print(os.getcwd())
dataset = pd.read_csv("output/dataset.csv",
                      dtype={'a': 'string', 'b': 'Int8'})

# Select columns from dataset

dataset = dataset[['Review', 'Liked']]
nltk.download("stopwords")
ps = PorterStemmer()
all_stopwords = stopwords.words("english")
all_stopwords.remove("not")

corpus = []
for i in range(0, 900):
    REVIEW_STR = re.sub("[^a-zA-Z]", " ", dataset["Review"][i])
    REVIEW_STR = REVIEW_STR.lower()
    REVIEW_LIST = REVIEW_STR.split()
    REVIEW_LIST = [
        ps.stem(word) for word in REVIEW_LIST if not word in set(all_stopwords)
    ]
    REVIEW_LIST = " ".join(REVIEW_LIST)
    corpus.append(REVIEW_LIST)

dump(corpus, "output/preprocessed_data.joblib")
print(corpus)
