from scipy.sparse.construct import rand
from src.utils.utils import read_yaml, create_directory
import argparse
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib


def train(path_to_config, path_to_params):
    config = read_yaml(path_to_config)
    params = read_yaml(path_to_params)

    split_data_dir = os.path.join(
        config["artifacts"]["storage_dir"], config["artifacts"]["split_data_dir"]
    )

    train_file = os.path.join(split_data_dir, config["artifacts"]["train_file"])
    # test_file = os.path.join(split_data_dir, config["artifacts"]["test_file"])

    print(f"Read training file: {train_file}")
    df = pd.read_csv(train_file)

    y_train = df.pop("quality")
    X_train = df

    rfr = RandomForestRegressor(
        n_estimators=params["model_params"]["RandomForestRegressor"]["hyper_params"][
            "n_estimator"
        ],
        max_depth=params["model_params"]["RandomForestRegressor"]["hyper_params"][
            "max_depth"
        ],
        oob_score=params["model_params"]["RandomForestRegressor"]["hyper_params"][
            "use_oob"
        ],
        random_state=params["base"]["random_state"],
    )

    rfr.fit(X_train, y_train)
    print("Model Training Complete!")
    print(f"Out of Bag Error: {rfr.oob_score_}")

    model_file_dir = os.path.join(
        config["artifacts"]["storage_dir"], config["artifacts"]["model_dir"]
    )

    create_directory([model_file_dir])

    model_file_path = os.path.join(
        model_file_dir, config["artifacts"]["model_save_file_name"]
    )
    print("Saving model......")
    joblib.dump(rfr, model_file_path)
    print(f"Model saved to {model_file_path}")


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()

    train(parsed_args.config, parsed_args.params)
