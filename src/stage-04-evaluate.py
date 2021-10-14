import argparse
import os

import joblib
import pandas as pd
import numpy as np
from scipy.sparse.construct import rand
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from src.utils.utils import create_directory, read_yaml, save_metrics


def eval_with_metrics(actual, predictions):
    mse = mean_squared_error(actual, predictions)
    rmse = np.sqrt(mean_squared_error(actual, predictions))
    mae = mean_absolute_error(actual, predictions)
    r2 = r2_score(actual, predictions)

    return {"mse": mse, "rmse": rmse, "mae": mae, "r2": r2}


def evaluate(path_to_config, path_to_params):
    config = read_yaml(path_to_config)

    split_data_dir = os.path.join(
        config["artifacts"]["storage_dir"], config["artifacts"]["split_data_dir"]
    )

    test_file = os.path.join(split_data_dir, config["artifacts"]["test_file"])

    print(f"Read training file: {test_file}")
    df = pd.read_csv(test_file)

    y_test = df.pop("quality")
    X_test = df

    model_file_dir = os.path.join(
        config["artifacts"]["storage_dir"], config["artifacts"]["model_dir"]
    )

    model_file_path = os.path.join(
        model_file_dir, config["artifacts"]["model_save_file_name"]
    )

    print(f"Loading Model from: {model_file_dir}")
    rfr = joblib.load(model_file_path)

    y_preds = rfr.predict(X_test)

    metrics = eval_with_metrics(y_test, y_preds)

    print(f"MSE: {metrics['mse']}")
    print(f"RMSE: {metrics['rmse']}")
    print(f"MAE: {metrics['mse']}")
    print(f"R2: {metrics['r2']}")

    metrics_dir = os.path.join(config["artifacts"]["storage_dir"],config["artifacts"]["eval_metrics"])
    create_directory([metrics_dir])
    metrics_file_path = os.path.join(metrics_dir, config["artifacts"]["metrics_file"])
    save_metrics(metrics,metrics_file_path)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()

    evaluate(parsed_args.config, parsed_args.params)
