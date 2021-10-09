from src.utils.utils import read_yaml,create_directory
import argparse
import pandas as pd
import os

def get_data(path_to_config):
    config = read_yaml(path_to_config)
    data_source = config["data"]["source"]

    # read data from source
    df = pd.read_csv(data_source,sep=";")
    print(df.head())

    # save in local storage
    artifact_dir = os.path.join(config["artifacts"]["storage_dir"],config["artifacts"]["raw_local_dir"])
    create_directory(dir_paths=[artifact_dir])

    artifact_file = os.path.join(artifact_dir,config["artifacts"]["raw_local_file"])
    df.to_csv(artifact_file,sep=",",index=False)

    

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")
    parsed_args = args.parse_args()

    config = get_data(parsed_args.config)

