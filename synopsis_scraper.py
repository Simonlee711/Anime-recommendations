''' 
A class that scrapes the interent for anime summaries.
'''
__author__ = 'Simon Lee'

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
from IPython.core.interactiveshell import InteractiveShell

from tqdm import tqdm
import requests
import pandas as pd
from bs4 import BeautifulSoup

class synopsis_extractor():
    '''
    A class that will scrape the summaries for us before getting written into the updated csv file
    '''
    def getdata(self, url):
        '''
        link for extract html data
        '''
        r = requests.get(url)
        return r.text

    def synopsis_scrap(self, anime_id):
        '''
        extracts the synopsis portion via keyword 'MAL' and 'Rewrite' and removes all useless crap and returns summary
        '''
        deletions = ['[Written by MAL Rewrite]', 'by MAL_Articles', '\n', '\r', '\'']
        htmldata = self.getdata("https://myanimelist.net/anime/" + anime_id)
        soup = BeautifulSoup(htmldata, 'html.parser')
        data = ''
        summary = ''
        key = ['MAL', 'Rewrite']
        for data in soup.find_all('p'):
            summary = data.get_text()
            if [True for x in key if x in summary]:
                for i in deletions:
                    summary = summary.replace(i,'')
                    print(summary)
                    return summary
            continue
        