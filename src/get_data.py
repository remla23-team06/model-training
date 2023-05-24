import pandas as pd

# Importing dataset
dataset = pd.read_csv('data/a1_RestaurantReviews_HistoricDump.tsv', delimiter='\t', quoting=3)
# Display dataset
print(dataset)
# save data in a file for later use
dataset.to_csv('output/dataset.csv', index=False)