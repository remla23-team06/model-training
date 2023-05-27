# model-training

## Requirements
Make sure to run `poetry install` to install all dependencies
Make sure to have Python 3.10 installed

## mllint
You can run mllint to check what it says about data version control `poetry run mllint`
1. Run `isort .`

## DVC
We will prepare a pipeline

### Stage 1: get_data
`dvc run -n get_data -d src/get_data.py -o output/dataset.txt python src/get_data.py`

### Stage 2: preprocess_data
`dvc run -n preprocess_data -d src/preprocess_data.py -o output/preprocessed_data.joblib python src/preprocess_data.py`

### Stage 3: train
`dvc run -n train -d src/train.py -o output/trained_model_and_data.joblib python src/train.py`

### Stage 4: evaluate_model
`dvc run -n evaluate_model -d src/evaluate_model.py -o output/evaluation.joblib python src/evaluate_model.py`

## DVC Remote (GDrive)
Pull the remote data
`dvc pull`
