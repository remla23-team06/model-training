"""Get data from the historic dump and save it to a file."""
import pandas as pd
# Importing dataset
dataset = pd.read_csv(
    "data/a1_RestaurantReviews_HistoricDump.tsv",
    delimiter="\t",
    quoting=3,
    dtype={'text': 'string', 'score': 'Int8'},
)

# Select columns from dataset

dataset = dataset[['Review', 'Liked']]

print(dataset)

# Save data in a file for later use
dataset.to_csv("output/dataset.csv", index=False)
