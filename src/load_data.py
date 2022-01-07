import os
from get_data import get_data, read_params
import argparse

def load_and_save(config_path):
    config=read_params(config_path)
    df=get_data(config_path)
    new_columns=[col.replace(" ","_") for col in df.columns]
    df.to_csv(config["load_data"]["raw_dataset_csv"],sep=",",index=False,header=new_columns)

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)   