import pandas as pd 
import synopsis_scraper
from tqdm import tqdm
import os

def checker(dataframe):
    lock_file = "record.lockfile"
    lock_file_ids = set()
    if os.path.exists(lock_file):
        with open(lock_file, "r") as lf:
            lock_file_ids = set(lf.read().splitlines())
    else:
        with open(lock_file, "w") as lf:
            lf.write(dataframe + "\n")

    print("lock files:", lock_file_ids)