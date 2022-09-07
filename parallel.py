'''
A progress checking file that checks if a file is in the lockfile or not.

A lockfile helps keep progress as we write out our data containing the synopsis after undergoing webscraping.
'''

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

    if dataframe in lock_file_ids:
        print("{} already exists in training set. Skipping...".format(dataframe))
        return True
    else:
        with open(lock_file, "a+") as lf:
            lf.write(dataframe + "\n")
            return False
