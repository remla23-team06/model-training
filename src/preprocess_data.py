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
dataset = pd.read_csv("output/dataset.csv")
nltk.download("stopwords")
ps = PorterStemmer()
all_stopwords = stopwords.words("english")
all_stopwords.remove("not")

corpus = []
for i in range(0, 900):
    REVIEW = re.sub("[^a-zA-Z]", " ", dataset["Review"][i])
    REVIEW = REVIEW.lower()
    REVIEW = REVIEW.split()
    REVIEW = [ps.stem(word) for word in REVIEW if not word in set(all_stopwords)]
    REVIEW = " ".join(REVIEW)
    corpus.append(REVIEW)

dump(corpus, "output/preprocessed_data.joblib")
print(corpus)
