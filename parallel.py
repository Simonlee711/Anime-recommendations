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

def synopsis_adder(dataframe):
        '''
        A function that takes a small chunk of a csv file and parallel computes the summaries and saves the csv file
        '''
        checker()
        obj = synopsis_scraper.synopsis_extractor()
        df = pd.read_csv('data/'+dataframe)
        for anime in tqdm(df['anime_id']):
            synopsis = obj.synopsis_scraper(anime)
            df['synopsis'][df['index']] = synopsis
        df.to_csv('data/'+dataframe)
        print("Dataframe has been updated with synopsis")        
        return df