import pandas as pd
from pathlib import Path
import os

RAW_DIR  = Path("data/raw")
PROCESSED_DIR = Path("data/processed")

def load_feather_files() : 
    """ Load the raw csv files from kaggle and convert them from feather format.
    - The feather format is known to be easy to upload. For example, a dataset in its csv format that would take
    30 seconds to upload, whould take only 2 seconds if converted to feather.
    """

    ## upload data
    train = pd.read_csv(RAW_DIR / "train.csv")
    test = pd.read_csv(RAW_DIR / "test.csv")
    metadata = pd.read_csv(RAW_DIR / "building_metadata.csv")
    weather_train = pd.read_csv(RAW_DIR / "weather_train.csv")
    weather_test = pd.read_csv(RAW_DIR / "weather_test.csv")

    print(f"train : {train.shape}")
    print(f"test : {test.shape}")
    print(f"metadata : {metadata.shape}")
    print(f"weather_train: {weather_train.shape}")
    print(f"weather_test : {weather_test.shape}")

    ## Save the data in feather format
    train.to_feather(os.path.join(RAW_DIR, "train_feather"))
    test.to_feather(os.path.join(RAW_DIR, "test_feather"))
    weather_train.to_feather(os.path.join(RAW_DIR, "weather_train_feather"))
    weather_test.to_feather(os.path.join(RAW_DIR, "weather_test_feather"))
    
def merge_data():
    """merge the three dataframes into one"""

    train = train.merge(metadata, on="building_id", how="left")
    train = train.merge(weather_train, on=["site_id", "time_stamp"], how="left")

def convert_to_feather(): 
    train.to_feather()



    






