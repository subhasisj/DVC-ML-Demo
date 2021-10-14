from typing import ForwardRef
import yaml
import os
import sys
import pprint
import json


def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.load(yaml_file, Loader=yaml.FullLoader)
    return content


def create_directory(dir_paths: list):
    for dir_path in dir_paths:
        os.makedirs(dir_path, exist_ok=True)
        print(f"creating directory: {dir_path}")


def save_metrics(metrics: dict, save_path: str) -> None:
    with open(save_path, "w") as out:
        json.dump(metrics, out, indent=4)
    print(f"saving metrics to {save_path}")


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(read_yaml(sys.argv[1]))
