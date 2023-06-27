# model-training

[![Coverage Status](https://coveralls.io/repos/github/remla23-team06/model-training/badge.svg?branch=main)](https://coveralls.io/github/remla23-team06/model-training?branch=main)
[![Coverage Status](https://coveralls.io/repos/github/remla23-team06/model-training/badge.svg?branch={branch})](https://coveralls.io/github/remla23-team06/model-training?branch={branch})


## Requirements
- Python 3.10
- Poetry 1.5.0 (to update, click [here](https://python-poetry.org))

_Disclaimer: Poetry can be installed on Linux, Mac, and Windows with WSL (Windows Subsystem for Linux)_ 
```curl -sSL https://install.python-poetry.org | python -```

## Running the project
1. Run `poetry install` to install dependencies
2. Ensure that you are using the correct Python version (3.10) by running `poetry env info`
3. If the Python version is not correct, run `poetry env use 3.10`, and re-rub `poetry install`

## Running DVC (from remote Google Drive storage)
1. DVC is already included in the Poetry dependencies, so no need to install it manually
2. Run `poetry run dvc pull` to pull the data from the remote storage
3. Run `poetry run dvc repro` to reproduce (run) the pipeline

The pipeline has 4 stages: get_data, preprocess_data, train, evaluate_model

## Remote Data Storage
The data utilized in the project is currently stored on Google Drive. Accessing it is part of our pipeline, which executes `get_data()` in `src/get_data/py` to download a `data/` folder with datasets. Reproducing the pipeline (look at the section above) triggers the remote data downloading, as it is the first stage of the pipeline

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

To generate a coverage report, run `poetry run pytest --junitxml=tests-report.xml --cov=tests/ --cov-report=xml`


### Running Pylint
Run `poetry run pylint src` to run all metrics from Pylint, not only those in DSLinter

### Mutamorphic Testing
Mutmorphic tests can be found in the `tests` directory and run as part of the pipeline.
