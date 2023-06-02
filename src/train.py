"""Train the model and export it to later use in prediction."""
import pandas as pd
from joblib import dump, load
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# load the preprocessed data
corpus = load("output/preprocessed_data.joblib")
dataset = pd.read_csv("output/dataset.csv",
                      dtype={'text': 'string', 'score': 'Int8'})

dataset = dataset[['Review', 'Liked']]

# Data transformation
cv = CountVectorizer(max_features=1420)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, -1].values

# Dividing dataset into training and test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=0
)

# Model fitting (Naive Bayes)
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Exporting NB Classifier to later use in prediction
dump(
    [classifier, X_train, X_test, y_train, y_test],
    "output/trained_model_and_data.joblib",
)
