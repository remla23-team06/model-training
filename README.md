# model-training

## mllint
You can run mllint to check what it says about data version control

## DVC
We will prepare a pipeline

### stage 1: get_data
`dvc run -n get_data -d src/get_data.py -o output/dataset.txt python src/get_data.py`

### stage 2: preprocess_data
`dvc run -n preprocess_data -d src/preprocess_data.py -o output/preprocessed_data.joblib python src/preprocess_data.py`

### stage 3: train
`dvc run -n train -d src/train.py -o output/trained_model_and_data.joblib python src/train.py`

### stage 4: evaluate_model
`dvc run -n evaluate_model -d src/evaluate_model.py -o output/evaluation.joblib python src/evaluate_model.py`