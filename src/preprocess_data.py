from joblib import dump, load
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pandas as pd
import re
import os

# Data Preprocessing
# load the data from the file
print(os.getcwd())
dataset = pd.read_csv('output/dataset.csv')
nltk.download('stopwords')
ps = PorterStemmer()
all_stopwords = stopwords.words('english')
all_stopwords.remove('not')

corpus = []
for i in range(0, 900):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
    review = ' '.join(review)
    corpus.append(review)
    
dump(corpus, 'output/preprocessed_data.joblib')
print(corpus)