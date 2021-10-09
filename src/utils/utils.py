from typing import ForwardRef
import yaml
import os
import sys
import pprint


def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.load(yaml_file,Loader=yaml.FullLoader)
    return content


def create_directory(dir_paths: list):
    for dir_path in dir_paths:
        os.makedirs(dir_path,exist_ok=True)
        print(f"creating director:{dir_path}")


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(read_yaml(sys.argv[1]))