from src.utils.utils import read_yaml, create_directory
import argparse
import pandas as pd
import os
from sklearn.model_selection import train_test_split


def get_data(path_to_config, path_to_params):
    config = read_yaml(path_to_config)
    params = read_yaml(path_to_params)

    artifact_dir = os.path.join(
        config["artifacts"]["storage_dir"], config["artifacts"]["raw_local_dir"]
    )
    artifact_file = os.path.join(artifact_dir, config["artifacts"]["raw_local_file"])

    # Load data from Stage 01
    print(f"Loading data from {artifact_file}")
    df = pd.read_csv(artifact_file)

    print("Splitting dataset into Train and Test sets")
    train, test = train_test_split(
        df,
        test_size=params["base"]["test_size"],
        random_state=params["base"]["random_state"],
    )

    print(f"Train Shape: {train.shape}")
    print(f"Test Shape:{test.shape}")

    split_data_dir = os.path.join(
        config["artifacts"]["storage_dir"], config["artifacts"]["split_data_dir"]
    )

    create_directory([split_data_dir])

    train_file = os.path.join(split_data_dir, config["artifacts"]["train_file"])
    test_file = os.path.join(split_data_dir, config["artifacts"]["test_file"])

    print(f"Saving data to {train_file}")
    train.to_csv(train_file, index=False)
    print(f"Saving data to {test_file}")
    test.to_csv(test_file, index=False)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()

    get_data(parsed_args.config, parsed_args.params)