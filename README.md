# model-training

## Requirements
- Python 3.10
- Poetry

## Running the project
1. Run `poetry install` to install dependencies
2. Ensure that you are using the correct Python version (3.10) by running `poetry env info`
3. If the Python version is not correct, run `poetry env use 3.10`, and re-rub `poetry install`

### mllint
Run `poetry run mllint` to run all the linters

### pytest
Run `poetry run pytest`


### pylint
Run `poetry run pylint src`

## Running DVC (from remote Google Drive storage)
1. DVC is already included in the Poetry dependencies, so no need to install it manually
2. Run `poetry run dvc pull` to pull the data from the remote storage
3. Run `poetry run dvc repro` to reproduce (run) the pipeline

The pipeline has 4 stages: get_data, preprocess_data, train, evaluate_model
