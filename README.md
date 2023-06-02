# model-training

## Requirements
- Python 3.10
- Poetry

## Running the project
1. Run `poetry install` to install dependencies
2. Ensure that you are using the correct Python version (3.10) by running `poetry env info`
3. If the Python version is not correct, run `poetry env use 3.10`, and re-rub `poetry install`

## Running DVC (from remote Google Drive storage)
1. DVC is already included in the Poetry dependencies, so no need to install it manually
2. Run `poetry run dvc pull` to pull the data from the remote storage
3. Run `poetry run dvc repro` to reproduce (run) the pipeline

The pipeline has 4 stages: get_data, preprocess_data, train, evaluate_model

## Running DVC metrics
There is a metric for the model accuracy, which is calculated by the `evaluate_model` stage.
1. Run `poetry run dvc metrics show` to show the metrics
2. Run `poetry run dvc metrics diff` to show the metrics diff

## Running Metrics

### DSLinter
To run only metrics from DSLinter, run:
`poetry run pylint src/`

You will get a report.txt file with the metrics.

### Running Mllint
Run `poetry run mllint` to run all the linters

If you want to generate a report, run `poetry run mllint --output report.md`


### Running Pytest
Run `poetry run pytest` to run tests located in the tests folder


### Running Pylint
Run `poetry run pylint src` to run all metrics from Pylint, not only those in DSLinter