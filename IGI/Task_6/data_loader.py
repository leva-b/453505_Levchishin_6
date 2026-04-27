import os
import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter

def load_automobile_dataset(filepath=None, force_download=False, local_file="automobile_data.csv"):
    """
    Load Automobile Dataset.
    Parameters:
    filepath - load from specific file (if exists)
    force_download - True: download from Kaggle, False: use local file if exists
    local_file - path to local file
    """
    if filepath and os.path.exists(filepath):
        print(f"Loading from: {filepath}")
        return pd.read_csv(filepath)
    
    if not force_download and os.path.exists(local_file):
        print(f"Using local file: {local_file}")
        return pd.read_csv(local_file)
    
    print("Downloading from Kaggle...")
    df = kagglehub.load_dataset(
        KaggleDatasetAdapter.PANDAS,
        "toramky/automobile-dataset",
        "Automobile_data.csv"
    )
    df.to_csv(local_file, index=False)
    print(f"Saved to: {local_file}")
    return df